#!/usr/bin/env python3
"""
Chunk the user-authored Cogitator Bellum wiki.

Strategy: split on ### headers so each weapon system entry becomes its own doc.
Then apply paragraph-aware chunking from the existing pipeline.
Skip generic structural headings (Part X / Volume X / Table of Contents / etc).
"""
import json, re, sys
from pathlib import Path
from collections import Counter

sys.path.insert(0, '/home/user/workspace/dataset')
from extract_and_chunk import chunk_text, TOK, TEXT_DIR, normalize_text

WIKI = Path('/home/user/workspace/sources/munitions_uav_wiki/cogitator_bellum.md')
CHUNKS_PATH = Path('/home/user/workspace/dataset/chunks.jsonl')

raw = WIKI.read_text()
# Strip HTML comment header for the body parse (keep provenance separately)
provenance_match = re.match(r'<!--(.*?)-->\s*', raw, re.S)
provenance = provenance_match.group(1).strip() if provenance_match else ''
body = raw[provenance_match.end():] if provenance_match else raw

# Find all ### entries with their position spans
# Match lines that start exactly with "### " (not #### or higher)
header_re = re.compile(r'^### (?!#)(.+?)$', re.M)
entries = []
matches = list(header_re.finditer(body))
print(f'Found {len(matches)} ### headers')

# Build entries: title + body until next ### header (or end of file)
for i, m in enumerate(matches):
    title = m.group(1).strip()
    start = m.start()
    end = matches[i+1].start() if i+1 < len(matches) else len(body)
    entry_text = body[start:end].strip()
    # Find which Part/Volume/section this entry belongs to (most recent ## or # above it)
    # to add as context
    parent_re = re.compile(r'^(#{1,2}) (.+?)$', re.M)
    parents = []
    for pm in parent_re.finditer(body[:start]):
        parents.append((pm.group(1), pm.group(2).strip()))
    # Take last # (volume) and last ## (section)
    volume = ''
    section = ''
    for level, name in reversed(parents):
        if not section and level == '##':
            section = name
        if not volume and level == '#':
            volume = name
        if volume and section:
            break
    entries.append({
        'title': title,
        'volume': volume,
        'section': section,
        'text': entry_text,
        'idx': i,
    })

# Filter out non-substantive entries (TOC stubs, summary lines, etc.)
def is_substantive(e):
    if len(e['text']) < 400:
        return False
    # Skip toc-like entries
    title_low = e['title'].lower()
    skip_titles = ['table of contents', 'summary', 'final notes', 'methodology',
                   'how to use', 'classification']
    if any(s in title_low for s in skip_titles):
        return False
    return True

substantive = [e for e in entries if is_substantive(e)]
skipped = len(entries) - len(substantive)
print(f'Substantive entries: {len(substantive)}  (skipped {skipped})')

# Remove already-existing wiki chunks (in case of re-run)
if CHUNKS_PATH.exists():
    keep_lines = []
    removed = 0
    with open(CHUNKS_PATH) as f:
        for line in f:
            r = json.loads(line)
            if r.get('bucket') == 'cogitator_bellum':
                removed += 1
                continue
            keep_lines.append(line)
    if removed:
        with open(CHUNKS_PATH, 'w') as f:
            f.writelines(keep_lines)
        print(f'Removed {removed} existing wiki chunks before re-chunking')

# Helper: derive a stable doc_id from title
def safe_id(s, n=80):
    s = re.sub(r'[^A-Za-z0-9]+', '_', s).strip('_')
    return s[:n] or 'untitled'

added_chunks = 0
added_tokens = 0
with open(CHUNKS_PATH, 'a', encoding='utf-8') as fout:
    for e in substantive:
        doc_id = f'cogbel__{e["idx"]:04d}__{safe_id(e["title"])}'[:160]
        # Provide bucket-context on each chunk (volume + section + title)
        context_header = ''
        if e['volume']:
            context_header += f'[{e["volume"]}]\n'
        if e['section']:
            context_header += f'[{e["section"]}]\n'
        # Combine for chunking; the title is already in the text as a `### ` line
        full_text = (context_header + e['text']) if context_header else e['text']
        full_text = normalize_text(full_text)
        chunks = chunk_text(full_text)
        # Save text mirror
        (TEXT_DIR / f'cogitator_bellum__{doc_id}.txt').write_text(full_text, encoding='utf-8')
        for ci, ch in enumerate(chunks):
            n_tok = len(TOK.encode(ch, add_special_tokens=False))
            rec = {
                'doc_id': doc_id,
                'bucket': 'cogitator_bellum',
                'source_path': 'munitions_uav_wiki/cogitator_bellum.md',
                'chunk_idx': ci,
                'n_chunks_in_doc': len(chunks),
                'n_tokens': n_tok,
                'is_bibliography': False,
                'text': ch,
            }
            fout.write(json.dumps(rec, ensure_ascii=False) + '\n')
            added_chunks += 1
            added_tokens += n_tok

print(f'Added: {len(substantive)} docs / {added_chunks} chunks / {added_tokens:,} tokens')

# Refresh global stats
buckets_chunks = Counter(); buckets_tokens = Counter()
total = 0; total_tokens = 0; docs = set()
with open(CHUNKS_PATH) as f:
    for line in f:
        r = json.loads(line)
        buckets_chunks[r['bucket']] += 1
        buckets_tokens[r['bucket']] += r['n_tokens']
        total += 1
        total_tokens += r['n_tokens']
        docs.add(r['doc_id'])

print(f'\n=== CORPUS NOW ===')
print(f'{len(docs):,} docs, {total:,} chunks, {total_tokens:,} tokens')
for b in sorted(buckets_chunks):
    print(f'  {b}: {buckets_chunks[b]:,} chunks / {buckets_tokens[b]:,} tokens')

stats = {
    'n_docs': len(docs),
    'n_chunks': total,
    'total_tokens': total_tokens,
    'avg_tokens_per_chunk': round(total_tokens / total, 1),
    'by_bucket': {b: {'chunks': buckets_chunks[b], 'tokens': buckets_tokens[b]} for b in sorted(buckets_chunks)},
}
Path('/home/user/workspace/dataset/chunk_stats.json').write_text(json.dumps(stats, indent=2))
