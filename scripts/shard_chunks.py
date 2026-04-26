#!/usr/bin/env python3
"""Split chunks.jsonl into shards for parallel Q&A generation."""
import json
from pathlib import Path

CHUNKS = Path('/home/user/workspace/dataset/chunks.jsonl')
SHARD_DIR = Path('/home/user/workspace/dataset/qa_shards')
SHARD_DIR.mkdir(exist_ok=True)
QA_DIR = Path('/home/user/workspace/dataset/qa_output')
QA_DIR.mkdir(exist_ok=True)

CHUNKS_PER_SHARD = 30  # ~559 shards — balance between context budget and orchestration overhead
DONE_FILE = Path('/home/user/workspace/dataset/qa_output/keep/done_chunk_ids.txt')

done_ids = set()
if DONE_FILE.exists():
    done_ids = set(DONE_FILE.read_text().split())
print(f'Already-done chunks (from smoke test): {len(done_ids)}')

chunks = []
skipped = 0
with open(CHUNKS) as f:
    for line in f:
        c = json.loads(line)
        cid = f"{c['doc_id']}__c{c['chunk_idx']:03d}"
        if cid in done_ids:
            skipped += 1
            continue
        chunks.append({
            'chunk_id': cid,
            'doc_id': c['doc_id'],
            'bucket': c['bucket'],
            'source_path': c['source_path'],
            'n_tokens': c['n_tokens'],
            'text': c['text'],
        })

print(f'Total chunks: {len(chunks)}')
print(f'Skipped (already done): {skipped}')

# Stratify: shuffle within each bucket so each shard sees variety, then interleave
import random
random.seed(7)
from collections import defaultdict
by_bucket = defaultdict(list)
for c in chunks:
    by_bucket[c['bucket']].append(c)
for b in by_bucket:
    random.shuffle(by_bucket[b])

# Interleave round-robin so each shard has a mix of buckets
ordered = []
buckets = list(by_bucket.keys())
indexes = {b: 0 for b in buckets}
while any(indexes[b] < len(by_bucket[b]) for b in buckets):
    for b in buckets:
        if indexes[b] < len(by_bucket[b]):
            ordered.append(by_bucket[b][indexes[b]])
            indexes[b] += 1

# Clear old shards
for old in SHARD_DIR.glob('shard_*.jsonl'):
    old.unlink()

# Write shards
n_shards = (len(ordered) + CHUNKS_PER_SHARD - 1) // CHUNKS_PER_SHARD
for i in range(n_shards):
    shard = ordered[i * CHUNKS_PER_SHARD : (i + 1) * CHUNKS_PER_SHARD]
    shard_path = SHARD_DIR / f'shard_{i:04d}.jsonl'
    with open(shard_path, 'w') as f:
        for c in shard:
            f.write(json.dumps(c, ensure_ascii=False) + '\n')

print(f'Created {n_shards} shards in {SHARD_DIR}')
print(f'Output dir for Q&A: {QA_DIR}')

# Print bucket distribution per shard (first 3)
for i in range(min(3, n_shards)):
    p = SHARD_DIR / f'shard_{i:04d}.jsonl'
    bks = defaultdict(int)
    n = 0
    with open(p) as f:
        for line in f:
            bks[json.loads(line)['bucket']] += 1
            n += 1
    print(f'  shard_{i:04d}: {n} chunks; buckets: {dict(bks)}')
