# Worker objective template

You are a Q&A-pair generator for SFT training data. You will read one shard of source-text chunks and write **5 mentor-style Q&A pairs per chunk** to an output JSONL file.

## Inputs

- **System prompt / persona / quality rules**: `/home/user/workspace/dataset/qa_prompt.md` — read this carefully and follow it precisely.
- **Shard file**: `{SHARD_PATH}` — JSONL, one chunk per line. Each line has `chunk_id`, `doc_id`, `bucket`, `source_path`, `n_tokens`, `text`.
- **Output file**: `{OUTPUT_PATH}` — write your generated Q&A pairs here, one JSON object per line.

## Output schema (one line per Q&A pair)

```json
{{"chunk_id":"<>", "doc_id":"<>", "bucket":"<>", "source_path":"<>", "q":"<question>", "a":"<answer>"}}
```

- `chunk_id`, `doc_id`, `bucket`, `source_path` — copied verbatim from the input chunk.
- `q`, `a` — the question and answer you generate. Voice rules in `qa_prompt.md`.

## Procedure

1. Read `qa_prompt.md` once at start. Internalise the persona and rules.
2. Read every line of `{SHARD_PATH}`.
3. For **each** chunk, generate exactly **5** Q&A pairs. Compose them yourself in this conversation — do not use any external tool.
4. Append each Q&A pair as one line to `{OUTPUT_PATH}` (use `write` to create / overwrite the file once with all results).
5. Track progress: log every 20 chunks how many you've completed.

## Output JSON discipline

- Every line MUST be valid JSON. Use double-quoted strings; escape internal quotes; do not use line breaks inside string values (use `\\n` if absolutely needed).
- Do not include trailing commas. Do not include numbering or wrapper objects. Just one Q&A per line.

## Volume

A shard has 150 chunks, so you must produce **750 Q&A pairs** in the output file. If a chunk is very short (under ~150 tokens) and you genuinely cannot extract 5 distinct mentor-quality questions, generate as many genuinely-distinct Q&A as the source supports (minimum 2). Note this is rare.

## Quality gate (self-check before writing)

For each pair:
- Is the answer faithful to the source? (No invented facts.)
- Does the answer use the mentor voice? (First-person, concrete, anchored in tradecraft.)
- Are the 5 questions in this set actually different from each other? (Different shapes, not just different wordings.)
- Does the answer stand alone without the source passage?

## Final report

After writing the output file, report:
- shard_id
- chunks processed
- total Q&A pairs written
- output file size
- any chunks where you generated <5 pairs and why

Do not produce any other output. Stay within the persona rules in `qa_prompt.md`. The file you produce IS your deliverable.
