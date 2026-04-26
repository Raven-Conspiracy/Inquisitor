#!/usr/bin/env python3
"""
Incrementally chunk the equipment DB text files (ODIN + CSIS + Wikipedia)
and append them to chunks.jsonl.

Each entry is a small standalone text file already (not a PDF), so we skip the
PDF extraction step but reuse the same paragraph-aware chunker and tokenizer.
"""
import json, sys, re
from pathlib import Path

sys.path.insert(0, "/home/user/workspace/dataset")
from extract_and_chunk import chunk_text, TOK, TEXT_DIR, normalize_text

ROOT = Path("/home/user/workspace")
CHUNKS = ROOT / "dataset" / "chunks.jsonl"
SRC_ROOT = ROOT / "sources" / "equipment_db"

SOURCES = [
    # (dir,                      bucket,                doc_id_prefix)
    (SRC_ROOT / "odin" / "api_text",       "threat_equipment_odin",     "odin"),
    (SRC_ROOT / "csis" / "text",           "threat_equipment_csis",     "csis"),
    (SRC_ROOT / "wikipedia" / "text",      "threat_equipment_wikipedia","wp"),
]

# Doc-id collisions: each entry file becomes its own "doc" with stable id
existing_doc_ids = set()
if CHUNKS.exists():
    with open(CHUNKS) as f:
        for line in f:
            existing_doc_ids.add(json.loads(line)["doc_id"])
print(f'Existing doc_ids: {len(existing_doc_ids)}')

added_chunks = 0
added_tokens = 0
added_docs = 0
skipped_too_small = 0
skipped_existing = 0

with open(CHUNKS, "a", encoding="utf-8") as fout:
    for src_dir, bucket, prefix in SOURCES:
        if not src_dir.exists():
            print(f"SKIP missing dir: {src_dir}")
            continue
        files = sorted(src_dir.glob("*.txt"))
        print(f"\n=== {bucket} ({prefix}): {len(files)} files in {src_dir} ===")
        per_bucket_chunks = 0
        per_bucket_tokens = 0
        per_bucket_docs = 0
        for f in files:
            doc_id = f"{prefix}__{f.stem}"[:160]
            if doc_id in existing_doc_ids:
                skipped_existing += 1
                continue
            text = f.read_text(errors='replace')
            text = normalize_text(text)
            if len(text) < 800:
                skipped_too_small += 1
                continue
            # Save cleaned text mirror
            (TEXT_DIR / f"{bucket}__{doc_id}.txt").write_text(text, encoding="utf-8")
            chunks = chunk_text(text)
            doc_tokens = 0
            for ci, ch in enumerate(chunks):
                n_tok = len(TOK.encode(ch, add_special_tokens=False))
                doc_tokens += n_tok
                rec = {
                    "doc_id": doc_id,
                    "bucket": bucket,
                    "source_path": str(f.relative_to(ROOT)),
                    "chunk_idx": ci,
                    "n_chunks_in_doc": len(chunks),
                    "n_tokens": n_tok,
                    "is_bibliography": False,
                    "text": ch,
                }
                fout.write(json.dumps(rec, ensure_ascii=False) + "\n")
            per_bucket_chunks += len(chunks)
            per_bucket_tokens += doc_tokens
            per_bucket_docs += 1
        print(f"  added: {per_bucket_docs} docs / {per_bucket_chunks} chunks / {per_bucket_tokens:,} tokens")
        added_docs += per_bucket_docs
        added_chunks += per_bucket_chunks
        added_tokens += per_bucket_tokens

print(f'\n=== TOTAL ADDED: {added_docs} docs / {added_chunks} chunks / {added_tokens:,} tokens ===')
print(f'Skipped (existing): {skipped_existing}')
print(f'Skipped (too small <800 chars): {skipped_too_small}')

# Refresh stats
from collections import Counter
bucket_chunks = Counter()
bucket_tokens = Counter()
total = 0; total_tokens = 0
docs = set()
with open(CHUNKS) as f:
    for line in f:
        rec = json.loads(line)
        bucket_chunks[rec["bucket"]] += 1
        bucket_tokens[rec["bucket"]] += rec["n_tokens"]
        total += 1
        total_tokens += rec["n_tokens"]
        docs.add(rec["doc_id"])

stats = {
    "n_docs": len(docs),
    "n_chunks": total,
    "total_tokens": total_tokens,
    "avg_tokens_per_chunk": round(total_tokens / total, 1),
    "by_bucket": {b: {"chunks": bucket_chunks[b], "tokens": bucket_tokens[b]}
                  for b in sorted(bucket_chunks)},
}
Path("/home/user/workspace/dataset/chunk_stats.json").write_text(json.dumps(stats, indent=2))
print(f'\nCorpus now: {len(docs)} docs, {total:,} chunks, {total_tokens:,} tokens')
print(json.dumps(stats['by_bucket'], indent=2))
