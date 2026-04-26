"""
One-time helper to convert sft/sft_chat.jsonl into the row format Foundry's
training transform expects: one row per SFT example with a 'messages' column
containing the JSON-encoded list of {role, content}.

Run locally before uploading to Foundry:
    python foundry/datasets/build_sft_dataset.py

Output: foundry/datasets/sft_chat.csv
Then in Foundry: New Dataset → Upload → import as Pandas DataFrame, place at
/Mentor Model/datasets/sft_chat (matches the path in train_mentor.py).
"""

import csv
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "sft" / "sft_chat.jsonl"
DST = Path(__file__).resolve().parent / "sft_chat.csv"


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"Missing {SRC}. Run from the repo root.")

    with SRC.open() as fin, DST.open("w", newline="") as fout:
        writer = csv.writer(fout, quoting=csv.QUOTE_ALL)
        writer.writerow(["messages", "chunk_id", "bucket", "doc_id"])
        n = 0
        for line in fin:
            obj = json.loads(line)
            meta = obj.get("meta", {})
            writer.writerow([
                json.dumps(obj["messages"], ensure_ascii=False),
                meta.get("chunk_id", ""),
                meta.get("bucket", ""),
                meta.get("doc_id", ""),
            ])
            n += 1
    print(f"Wrote {n} rows to {DST}")


if __name__ == "__main__":
    main()
