#!/usr/bin/env python3
"""Chunk the joint_fires_corpus extracted text files using the same
tokenizer + chunk_text() helpers as the existing mentor corpus.

Input:  joint_fires_corpus/extracted/<bucket>/<slug>.txt
Output: joint_fires_corpus/chunks/chunks.jsonl
        joint_fires_corpus/chunks/chunk_stats.json

Schema matches existing corpus (doc_id, bucket, source_path, chunk_idx,
n_chunks_in_doc, n_tokens, text, is_bibliography).

All buckets are prefixed with "jf_" to avoid collisions with the existing
mentor-corpus buckets (e.g. existing "joint_doctrine" -> our "jf_joint_doctrine").
"""

import csv
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

# Reuse the existing chunking pipeline
sys.path.insert(0, "/home/user/workspace/dataset")
from extract_and_chunk import chunk_text, TOK, normalize_text  # noqa: E402

ROOT = Path("/home/user/workspace/joint_fires_corpus")
EXTRACTED = ROOT / "extracted"
CHUNKS_DIR = ROOT / "chunks"
CHUNKS_DIR.mkdir(parents=True, exist_ok=True)
OUT = CHUNKS_DIR / "chunks.jsonl"
STATS = CHUNKS_DIR / "chunk_stats.json"
LOG = ROOT / "manifest" / "download_log.csv"

MIN_CHARS = 600  # docs shorter than this are too tiny to chunk meaningfully

# Build slug -> (title, url, bucket) lookup from log
slug_meta: dict[tuple[str, str], dict] = {}
with open(LOG) as f:
    for r in csv.DictReader(f):
        if r.get("status") != "ok":
            continue
        # extracted_path is the extracted file; derive slug from basename
        path = r.get("extracted_path") or r.get("path") or ""
        if not path:
            continue
        slug = Path(path).stem
        bucket = r.get("bucket") or "unknown"
        slug_meta[(bucket, slug)] = {
            "title": (r.get("title") or "").strip() or slug,
            "url": (r.get("url") or "").strip(),
            "org": (r.get("org") or "").strip(),
            "year": (r.get("year") or "").strip(),
            "section": (r.get("section") or "").strip(),
            "subsection": (r.get("subsection") or "").strip(),
            "license": (r.get("license") or "").strip(),
            "bucket_orig": bucket,
        }


def safe_id(s: str, n: int = 100) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")
    return s[:n] or "untitled"


def is_bib_chunk(text: str) -> bool:
    """Crude bibliography/notes detector — many short lines that look like cites."""
    lines = [ln.strip() for ln in text.split("\n") if ln.strip()]
    if not lines:
        return False
    cite_re = re.compile(r"^(\d+\.\s|\[\d+\]|[A-Z][a-z]+,\s+[A-Z]\.)")
    cite_count = sum(1 for ln in lines if cite_re.match(ln))
    return cite_count / max(len(lines), 1) > 0.45 and len(lines) > 6


def main():
    n_docs = 0
    n_chunks = 0
    n_skipped = 0
    n_tokens = 0
    bucket_chunks: Counter = Counter()
    bucket_tokens: Counter = Counter()

    # Truncate output
    OUT.write_text("")

    with open(OUT, "a", encoding="utf-8") as fout:
        for bucket_dir in sorted(EXTRACTED.iterdir()):
            if not bucket_dir.is_dir():
                continue
            orig_bucket = bucket_dir.name
            bucket = f"jf_{orig_bucket}"
            for txt_path in sorted(bucket_dir.glob("*.txt")):
                slug = txt_path.stem
                meta = slug_meta.get((orig_bucket, slug), {})
                title = meta.get("title") or slug
                url = meta.get("url") or ""
                org = meta.get("org") or ""
                year = meta.get("year") or ""

                raw = txt_path.read_text(encoding="utf-8", errors="ignore")
                if len(raw) < MIN_CHARS:
                    n_skipped += 1
                    continue
                text = normalize_text(raw)

                # Prefix doc with title + provenance header for citation context
                header = f"# {title}\n"
                if org:
                    header += f"Publisher: {org}"
                    if year:
                        header += f" ({year})"
                    header += "\n"
                if url:
                    header += f"Source: {url}\n"
                header += "\n"
                doc_text = header + text

                chunks = chunk_text(doc_text)
                if not chunks:
                    n_skipped += 1
                    continue

                doc_id = f"jf__{orig_bucket}__{safe_id(slug)}"
                source_path = f"joint_fires_corpus/extracted/{orig_bucket}/{txt_path.name}"

                for ci, ch in enumerate(chunks):
                    n_tok = len(TOK.encode(ch, add_special_tokens=False))
                    rec = {
                        "doc_id": doc_id,
                        "bucket": bucket,
                        "source_path": source_path,
                        "source_url": url,
                        "title": title,
                        "org": org,
                        "year": year,
                        "section": meta.get("section", ""),
                        "subsection": meta.get("subsection", ""),
                        "license": meta.get("license", ""),
                        "chunk_idx": ci,
                        "n_chunks_in_doc": len(chunks),
                        "n_tokens": n_tok,
                        "is_bibliography": is_bib_chunk(ch),
                        "text": ch,
                    }
                    fout.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    n_chunks += 1
                    n_tokens += n_tok
                    bucket_chunks[bucket] += 1
                    bucket_tokens[bucket] += n_tok
                n_docs += 1

    stats = {
        "n_docs": n_docs,
        "n_chunks": n_chunks,
        "n_skipped_docs": n_skipped,
        "total_tokens": n_tokens,
        "avg_tokens_per_chunk": round(n_tokens / max(n_chunks, 1), 1),
        "by_bucket": {
            b: {"chunks": bucket_chunks[b], "tokens": bucket_tokens[b]}
            for b in sorted(bucket_chunks)
        },
    }
    STATS.write_text(json.dumps(stats, indent=2))

    print(f"\n=== JOINT FIRES CORPUS ===")
    print(f"{n_docs:,} docs, {n_chunks:,} chunks, {n_tokens:,} tokens "
          f"(avg {stats['avg_tokens_per_chunk']} tok/chunk), "
          f"{n_skipped} docs skipped (too short)")
    for b in sorted(bucket_chunks):
        print(f"  {b:40} {bucket_chunks[b]:>5} chunks / {bucket_tokens[b]:>9,} tokens")


if __name__ == "__main__":
    main()
