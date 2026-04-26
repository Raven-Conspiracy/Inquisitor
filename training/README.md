# Training

Supervised fine-tuning of [`Qwen/Qwen3-0.6B-Base`](https://huggingface.co/Qwen/Qwen3-0.6B-Base) with LoRA on the 490-pair mentor Q&A dataset.

## Config

- LoRA: r=16, alpha=32, dropout=0.05, on q/k/v/o/gate/up/down proj
- Effective batch size: 8 (2 × 4 grad accumulation)
- Learning rate: 2e-4 cosine, 5% warmup
- Epochs: 3 (~185 optimizer steps total)
- Precision: bf16
- Max sequence length: 1,536 tokens

## Run on GPU

```bash
git clone https://github.com/omnissiahcypher/mentor-corpus
cd mentor-corpus
pip install -r training/requirements.txt
python training/train_sft.py
```

Expected wall-clock:

| Hardware | Estimate |
|---|---|
| T4 16 GB (Colab/Kaggle) | ~25-40 min |
| A10G / L4 24 GB | ~10-15 min |
| H100 80 GB | ~3-5 min |
| 2-vCPU CPU only | 8-24 hr (not recommended) |

## HF Jobs (recommended)

```bash
hf auth login   # paste a write token
hf jobs run \
  --hardware nvidia-l4 \
  --image huggingface/transformers-pytorch-gpu \
  --secrets HF_TOKEN \
  -- \
  bash -c "git clone https://github.com/omnissiahcypher/mentor-corpus && \
           cd mentor-corpus && \
           pip install -r training/requirements.txt && \
           python training/train_sft.py"
```

## Push to Hub

The script auto-pushes to `OmnissiahsCypher/cogitator-bellum-mentor`. Set `HF_HUB_REPO = None` in `train_sft.py` to disable, or change the repo name.

## Inference after training

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "OmnissiahsCypher/cogitator-bellum-mentor"  # or local path
tok = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16, device_map="auto")

SYSTEM = "You are a senior US/NATO intelligence and military mentor..."  # see sft_chat.jsonl
messages = [
    {"role": "system", "content": SYSTEM},
    {"role": "user", "content": "What's the difference between collection management and analysis tasking?"},
]
inputs = tok.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True).to(model.device)
out = model.generate(inputs, max_new_tokens=400, temperature=0.7, top_p=0.9)
print(tok.decode(out[0][inputs.shape[-1]:], skip_special_tokens=True))
```

## Data format

`sft/sft_chat.jsonl` — chat-format with system prompt:

```json
{"messages": [
  {"role": "system", "content": "You are a senior US/NATO intelligence..."},
  {"role": "user", "content": "..."},
  {"role": "assistant", "content": "..."}
],
 "meta": {"chunk_id": "...", "bucket": "...", "doc_id": "..."}}
```

`sft/sft_text.jsonl` — plain-text fallback for non-chat-template tokenizers.

## Notes on dataset size

490 Q&A is small. Expected outcomes:

- Strong mentor-voice imitation (the persona is consistent and rare)
- Solid faithfulness on the 105 chunks covered
- Limited factual coverage of the 17,241-chunk corpus (only ~0.6% of chunks are represented)

For a stronger model, regenerate Q&A across more shards (the pipeline + prompt are in `scripts/`) and re-run training. The full corpus supports up to ~86,000 Q&A at 5 per chunk.
