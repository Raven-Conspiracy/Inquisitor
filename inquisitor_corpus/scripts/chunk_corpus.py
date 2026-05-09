#!/usr/bin/env python3
"""Chunk inquisitor_corpus extracted text files using the same tokenizer +
chunk_text() helpers as mentor-corpus and joint_fires_corpus.

Input:  inquisitor_corpus/extracted/<bucket>/<slug>.txt
Output: inquisitor_corpus/chunks/chunks.jsonl
        inquisitor_corpus/chunks/chunk_stats.json

Schema matches existing corpus (doc_id, bucket, source_path, chunk_idx,
n_chunks_in_doc, n_tokens, text, is_bibliography).

All buckets prefixed with "inq_" to avoid collisions with mentor-corpus
("threat_doctrine") and joint_fires ("jf_*").

Special handling: oob_*_structured / oob_red_ledger buckets are pre-chunked
(one self-contained record per file). They are emitted as a single chunk
each with structured=True flag, regardless of length.
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

ROOT = Path("/home/user/workspace/inquisitor_corpus")
EXTRACTED = ROOT / "extracted"
CHUNKS_DIR = ROOT / "chunks"
CHUNKS_DIR.mkdir(parents=True, exist_ok=True)
OUT = CHUNKS_DIR / "chunks.jsonl"
STATS = CHUNKS_DIR / "chunk_stats.json"

LOG_PASS1 = ROOT / "manifest" / "download_log.csv"
LOG_PASS2 = ROOT / "manifest" / "retry_pass_log.csv"
LOG_PASS3 = ROOT / "manifest" / "fetch_url_recovery_log.csv"

MIN_CHARS_PROSE = 600     # standard threshold for harvested prose
MIN_CHARS_STRUCT = 200    # structured OOB chunks can be shorter

STRUCTURED_BUCKETS = {
    "oob_china_structured",
    "oob_iran_structured",
    "oob_dprk_structured",
    "oob_red_ledger",
}


def safe_id(s: str, n: int = 100) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")
    return s[:n] or "untitled"


def is_bib_chunk(text: str) -> bool:
    lines = [ln.strip() for ln in text.split("\n") if ln.strip()]
    if not lines:
        return False
    cite_re = re.compile(r"^(\d+\.\s|\[\d+\]|[A-Z][a-z]+,\s+[A-Z]\.)")
    cite_count = sum(1 for ln in lines if cite_re.match(ln))
    return cite_count / max(len(lines), 1) > 0.45 and len(lines) > 6


# Build slug -> metadata lookup. Master sheet (pass 1 log) has full metadata
# for ALL 514 sources regardless of status. Use it as primary.
slug_meta: dict[tuple[str, str], dict] = {}

if LOG_PASS1.exists():
    with open(LOG_PASS1) as f:
        for r in csv.DictReader(f):
            extracted = r.get("extracted_path") or ""
            url = (r.get("url") or "").strip()
            bucket = r.get("bucket") or "unknown"
            # Derive slug from extracted path if present, else skip (status=fail
            # without extracted_path means we never got the doc — we'll match
            # later passes by URL).
            if extracted:
                slug = Path(extracted).stem
                slug_meta[(bucket, slug)] = {
                    "title": (r.get("title") or "").strip() or slug,
                    "url": url,
                    "org": (r.get("org") or "").strip(),
                    "authors": (r.get("authors") or "").strip(),
                    "year": (r.get("year") or "").strip(),
                    "section": (r.get("section") or "").strip(),
                    "subsection": (r.get("subsection") or "").strip(),
                    "license": (r.get("license") or "").strip(),
                    "priority": (r.get("priority") or "").strip(),
                    "relevance": (r.get("relevance") or "").strip(),
                    "corpus_section": (r.get("corpus") or "").strip(),
                }

# URL -> master metadata (for matching pass 2/3 entries that don't have
# title/org/year columns)
url_to_master: dict[str, dict] = {}
if LOG_PASS1.exists():
    with open(LOG_PASS1) as f:
        for r in csv.DictReader(f):
            url = (r.get("url") or "").strip()
            if not url:
                continue
            url_to_master[url] = {
                "title": (r.get("title") or "").strip(),
                "url": url,
                "org": (r.get("org") or "").strip(),
                "authors": (r.get("authors") or "").strip(),
                "year": (r.get("year") or "").strip(),
                "section": (r.get("section") or "").strip(),
                "subsection": (r.get("subsection") or "").strip(),
                "license": (r.get("license") or "").strip(),
                "priority": (r.get("priority") or "").strip(),
                "relevance": (r.get("relevance") or "").strip(),
                "corpus_section": (r.get("corpus") or "").strip(),
            }

# Augment from pass 2 + pass 3 (these only have minimal cols but extracted_path
# is what we need; URL lets us look up master metadata)
for log_path in (LOG_PASS2, LOG_PASS3):
    if not log_path.exists():
        continue
    with open(log_path) as f:
        for r in csv.DictReader(f):
            if r.get("status") != "ok":
                continue
            extracted = (r.get("extracted_path") or "").strip()
            if not extracted:
                continue
            slug = Path(extracted).stem
            bucket = r.get("bucket") or "unknown"
            url = (r.get("url") or "").strip()
            # Look up master metadata via URL match
            master = url_to_master.get(url, {})
            if (bucket, slug) not in slug_meta:
                slug_meta[(bucket, slug)] = {
                    "title": master.get("title") or r.get("title") or slug,
                    "url": url,
                    "org": master.get("org", ""),
                    "authors": master.get("authors", ""),
                    "year": master.get("year", ""),
                    "section": master.get("section", ""),
                    "subsection": master.get("subsection", ""),
                    "license": master.get("license", ""),
                    "priority": master.get("priority") or r.get("priority", ""),
                    "relevance": master.get("relevance", ""),
                    "corpus_section": master.get("corpus_section", ""),
                }


def emit_record(fout, *, doc_id, bucket, source_path, meta, chunk_idx,
                n_chunks_in_doc, n_tokens, text, is_bib, is_structured):
    rec = {
        "doc_id": doc_id,
        "bucket": bucket,
        "source_path": source_path,
        "source_url": meta.get("url", ""),
        "title": meta.get("title", ""),
        "org": meta.get("org", ""),
        "authors": meta.get("authors", ""),
        "year": meta.get("year", ""),
        "section": meta.get("section", ""),
        "subsection": meta.get("subsection", ""),
        "license": meta.get("license", ""),
        "priority": meta.get("priority", ""),
        "corpus_section": meta.get("corpus_section", ""),
        "is_structured": is_structured,
        "chunk_idx": chunk_idx,
        "n_chunks_in_doc": n_chunks_in_doc,
        "n_tokens": n_tokens,
        "is_bibliography": is_bib,
        "text": text,
    }
    fout.write(json.dumps(rec, ensure_ascii=False) + "\n")


def main():
    n_docs = 0
    n_chunks = 0
    n_skipped = 0
    n_tokens = 0
    bucket_chunks: Counter = Counter()
    bucket_tokens: Counter = Counter()

    OUT.write_text("")

    with open(OUT, "a", encoding="utf-8") as fout:
        for bucket_dir in sorted(EXTRACTED.iterdir()):
            if not bucket_dir.is_dir():
                continue
            orig_bucket = bucket_dir.name
            bucket = f"inq_{orig_bucket}"
            is_structured_bucket = orig_bucket in STRUCTURED_BUCKETS

            for txt_path in sorted(bucket_dir.glob("*.txt")):
                slug = txt_path.stem
                meta = slug_meta.get((orig_bucket, slug), {})

                raw = txt_path.read_text(encoding="utf-8", errors="ignore")
                min_chars = MIN_CHARS_STRUCT if is_structured_bucket else MIN_CHARS_PROSE

                if len(raw) < min_chars:
                    n_skipped += 1
                    continue

                doc_id = f"inq__{orig_bucket}__{safe_id(slug)}"
                source_path = f"inquisitor_corpus/extracted/{orig_bucket}/{txt_path.name}"

                if is_structured_bucket:
                    # Pre-chunked structured OOB: emit as single chunk, no
                    # title header injection (the file already has one), no
                    # re-tokenizing into smaller pieces.
                    text = raw.strip()
                    n_tok = len(TOK.encode(text, add_special_tokens=False))
                    # Attempt to extract title from "# ..." first line
                    first_line = text.split("\n", 1)[0]
                    derived_title = first_line.lstrip("# ").strip() if first_line.startswith("#") else slug
                    if not meta.get("title"):
                        meta = dict(meta)
                        meta["title"] = derived_title
                    if not meta.get("org"):
                        meta = dict(meta)
                        meta["org"] = "Inquisitor curated OOB"
                    emit_record(
                        fout,
                        doc_id=doc_id,
                        bucket=bucket,
                        source_path=source_path,
                        meta=meta,
                        chunk_idx=0,
                        n_chunks_in_doc=1,
                        n_tokens=n_tok,
                        text=text,
                        is_bib=False,
                        is_structured=True,
                    )
                    n_chunks += 1
                    n_tokens += n_tok
                    bucket_chunks[bucket] += 1
                    bucket_tokens[bucket] += n_tok
                    n_docs += 1
                    continue

                # Standard prose chunking path
                title = meta.get("title") or slug
                url = meta.get("url") or ""
                org = meta.get("org") or ""
                year = meta.get("year") or ""

                text = normalize_text(raw)
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

                for ci, ch in enumerate(chunks):
                    n_tok = len(TOK.encode(ch, add_special_tokens=False))
                    emit_record(
                        fout,
                        doc_id=doc_id,
                        bucket=bucket,
                        source_path=source_path,
                        meta={**meta, "title": title, "url": url, "org": org, "year": year},
                        chunk_idx=ci,
                        n_chunks_in_doc=len(chunks),
                        n_tokens=n_tok,
                        text=ch,
                        is_bib=is_bib_chunk(ch),
                        is_structured=False,
                    )
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

    print(f"\n=== INQUISITOR CORPUS ===")
    print(f"{n_docs:,} docs, {n_chunks:,} chunks, {n_tokens:,} tokens "
          f"(avg {stats['avg_tokens_per_chunk']} tok/chunk), "
          f"{n_skipped} docs skipped (too short)")
    for b in sorted(bucket_chunks):
        print(f"  {b:42} {bucket_chunks[b]:>5} chunks / {bucket_tokens[b]:>9,} tokens")


if __name__ == "__main__":
    main()
