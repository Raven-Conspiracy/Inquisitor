"""
SFT trainer for Qwen3-0.6B-Base + LoRA on the mentor Q&A dataset.

Targets: HF Jobs, Colab T4, Kaggle, or any CUDA box with >= 12 GB VRAM.
For CPU-only it works but is 8-24 hr; prefer GPU.

Run:
    pip install -r training/requirements.txt
    python training/train_sft.py
"""

import json
import os
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import LoraConfig
from trl import SFTTrainer, SFTConfig

BASE_MODEL = "Qwen/Qwen3-0.6B-Base"
DATA_PATH = "sft/sft_chat.jsonl"
OUTPUT_DIR = "training/output"
HF_HUB_REPO = "OmnissiahsCypher/cogitator-bellum-mentor"  # set to None to skip push

# ---------- Load data ----------

ds = load_dataset("json", data_files=DATA_PATH, split="train")
print(f"Loaded {len(ds)} SFT examples")
ds = ds.train_test_split(test_size=0.05, seed=42)
print(f"  train: {len(ds['train'])}  eval: {len(ds['test'])}")

# ---------- Tokenizer + model ----------

tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, trust_remote_code=True)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL,
    torch_dtype="bfloat16",
    device_map="auto",
    trust_remote_code=True,
)

# ---------- LoRA config (r=16, 3 epochs) ----------

peft_config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
    target_modules=[
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj",
    ],
)

# ---------- Training config ----------

sft_config = SFTConfig(
    output_dir=OUTPUT_DIR,
    num_train_epochs=3,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    gradient_accumulation_steps=4,        # effective batch = 8
    gradient_checkpointing=True,
    learning_rate=2e-4,
    lr_scheduler_type="cosine",
    warmup_ratio=0.05,
    logging_steps=10,
    eval_strategy="steps",
    eval_steps=50,
    save_strategy="steps",
    save_steps=100,
    save_total_limit=3,
    bf16=True,
    max_length=1536,
    packing=False,
    report_to="none",
    push_to_hub=bool(HF_HUB_REPO),
    hub_model_id=HF_HUB_REPO,
    hub_private_repo=False,
)

# ---------- Train ----------

trainer = SFTTrainer(
    model=model,
    args=sft_config,
    train_dataset=ds["train"],
    eval_dataset=ds["test"],
    peft_config=peft_config,
    processing_class=tokenizer,
)

trainer.train()

# ---------- Save adapter + merged model ----------

trainer.save_model(OUTPUT_DIR)
print(f"\nLoRA adapter saved to {OUTPUT_DIR}")

# Optional: merge LoRA into base for a self-contained model
try:
    print("\nMerging LoRA into base model...")
    merged = trainer.model.merge_and_unload()
    merged.save_pretrained(os.path.join(OUTPUT_DIR, "merged"))
    tokenizer.save_pretrained(os.path.join(OUTPUT_DIR, "merged"))
    print(f"Merged model saved to {OUTPUT_DIR}/merged")
except Exception as e:
    print(f"Merge skipped: {e}")

if HF_HUB_REPO:
    print(f"\nPushing to {HF_HUB_REPO}...")
    trainer.push_to_hub()
    print("Done.")
