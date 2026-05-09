#!/usr/bin/env python3
"""Dedupe inquisitor chunks against existing mentor-corpus subtrees.

Process:
1. Build a set of normalized-text SHA-256 hashes from:
   - mentor-corpus-repo/corpus/chunks.jsonl (subtree 1: 17,241)
   - mentor-corpus-repo/joint_fires_corpus/chunks/chunks.jsonl (subtree 2: 6,955)
2. Stream inquisitor chunks; drop any whose hash matches OR whose hash matches
   another inquisitor chunk seen earlier in this pass (intra-corpus dedup).
3. Write deduped chunks to chunks_dedup.jsonl + dedupe_report.json.

Normalization: lowercase + collapse whitespace + strip provenance header
(first chunk of every doc has a "# Title\nPublisher: ...\nSource: ..." block
that would create false misses if compared against parent chunks). Strip
leading lines that match those patterns.
"""
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path("/home/user/workspace/inquisitor_corpus")
PARENT_CORPUS = Path("/home/user/workspace/mentor-corpus-repo/corpus/chunks.jsonl")
JF_CORPUS = Path("/home/user/workspace/mentor-corpus-repo/joint_fires_corpus/chunks/chunks.jsonl")
INQ_IN = ROOT / "chunks" / "chunks.jsonl"
INQ_OUT = ROOT / "chunks" / "chunks_dedup.jsonl"
REPORT = ROOT / "chunks" / "dedupe_report.json"

WS_RE = re.compile(r"\s+")
HEADER_LINE_RE = re.compile(r"^(#\s|Publisher:\s|Source:\s)", re.M)


def normalize_for_hash(text: str) -> str:
    # Strip leading provenance header lines
    lines = text.split("\n")
    body_start = 0
    for i, ln in enumerate(lines):
        if HEADER_LINE_RE.match(ln) or not ln.strip():
            body_start = i + 1
            continue
        break
    body = "\n".join(lines[body_start:])
    body = body.lower().strip()
    body = WS_RE.sub(" ", body)
    return body


def hash_text(text: str) -> str:
    return hashlib.sha256(normalize_for_hash(text).encode("utf-8")).hexdigest()


def load_parent_hashes() -> dict[str, str]:
    """Return hash -> source_label so we know which parent corpus had the dupe."""
    parent: dict[str, str] = {}
    for path, label in [(PARENT_CORPUS, "mentor"), (JF_CORPUS, "jf")]:
        if not path.exists():
            print(f"WARN: {path} missing")
            continue
        n = 0
        with open(path) as f:
            for line in f:
                rec = json.loads(line)
                h = hash_text(rec["text"])
                # First write wins (preserves source priority)
                parent.setdefault(h, label)
                n += 1
        print(f"  {label}: {n:,} chunks loaded")
    return parent


def main():
    print("Loading parent corpus hashes...")
    parent_hashes = load_parent_hashes()
    print(f"  Total unique parent hashes: {len(parent_hashes):,}")

    print("\nDedup pass on inquisitor chunks...")
    seen_inq: set[str] = set()
    n_in = 0
    n_kept = 0
    n_dup_parent_mentor = 0
    n_dup_parent_jf = 0
    n_dup_intra = 0
    by_bucket_kept: Counter = Counter()
    by_bucket_dropped: Counter = Counter()

    with open(INQ_IN) as fin, open(INQ_OUT, "w") as fout:
        for line in fin:
            n_in += 1
            rec = json.loads(line)
            h = hash_text(rec["text"])

            if h in parent_hashes:
                src = parent_hashes[h]
                if src == "mentor":
                    n_dup_parent_mentor += 1
                else:
                    n_dup_parent_jf += 1
                by_bucket_dropped[rec["bucket"]] += 1
                continue

            if h in seen_inq:
                n_dup_intra += 1
                by_bucket_dropped[rec["bucket"]] += 1
                continue
            seen_inq.add(h)

            fout.write(line)
            n_kept += 1
            by_bucket_kept[rec["bucket"]] += 1

    report = {
        "n_in": n_in,
        "n_kept": n_kept,
        "n_dropped_total": n_in - n_kept,
        "dropped_breakdown": {
            "dup_with_mentor_corpus": n_dup_parent_mentor,
            "dup_with_joint_fires_corpus": n_dup_parent_jf,
            "intra_corpus_duplicate": n_dup_intra,
        },
        "by_bucket_kept": dict(sorted(by_bucket_kept.items())),
        "by_bucket_dropped": dict(sorted(by_bucket_dropped.items())),
    }
    REPORT.write_text(json.dumps(report, indent=2))

    print(f"\n=== DEDUP REPORT ===")
    print(f"Input chunks:               {n_in:,}")
    print(f"Kept:                       {n_kept:,}")
    print(f"Dropped — mentor corpus:    {n_dup_parent_mentor:,}")
    print(f"Dropped — joint_fires:      {n_dup_parent_jf:,}")
    print(f"Dropped — intra-inquisitor: {n_dup_intra:,}")
    print(f"Total dropped:              {n_in - n_kept:,}")
    print(f"\nDeduped output: {INQ_OUT}")


if __name__ == "__main__":
    main()
