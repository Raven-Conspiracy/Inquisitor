"""
Foundry training transform: SFT a Qwen3-0.6B-Base model with LoRA on the
mentor Q&A dataset and publish the result as a Foundry model.

Inputs:
    sft_dataset: a Foundry dataset built from sft/sft_chat.jsonl (or rebuilt
        from the corpus); the dataset must have a 'messages' column whose
        cells are JSON arrays of {role, content} (system/user/assistant).

Outputs:
    mentor_model: Foundry model resource. The trained QwenMentorAdapter is
        published here with version auto-derived from the git commit.

Run config:
    @lightweight() with gpu_type='NVIDIA_T4' (or stronger). Confirm your
    project's GPU resource queue allows the requested type — see
    https://palantir.com/docs/foundry/model-integration/gpu-training/.

Wall-clock estimates (from training/README.md):
    T4 16GB    ~25-40 min       L4 24GB    ~10-15 min       H100 80GB ~3-5 min
"""

from __future__ import annotations

import json
import os
import tempfile

from transforms.api import transform, Input, Output, lightweight
from palantir_models.transforms import ModelOutput
from palantir_models.models import ModelVersionChangeType

# Local module — the model adapter we publish at the end
from model_adapters.qwen_mentor_adapter import (  # noqa: E402
    QwenMentorAdapter,
    MENTOR_SYSTEM_PROMPT,
)


# ---------- Tunables --------------------------------------------------------

BASE_MODEL_ID = "Qwen/Qwen3-0.6B-Base"

LORA_R = 16
LORA_ALPHA = 32
LORA_DROPOUT = 0.05
LORA_TARGET_MODULES = [
    "q_proj", "k_proj", "v_proj", "o_proj",
    "gate_proj", "up_proj", "down_proj",
]

NUM_EPOCHS = 3
PER_DEVICE_BATCH = 2
GRAD_ACCUM = 4
LR = 2e-4
WARMUP_RATIO = 0.05
MAX_SEQ_LEN = 1536


# ---------- Transform -------------------------------------------------------

@lightweight(gpu_type="NVIDIA_T4")  # bump to NVIDIA_L4 / NVIDIA_A10G if available
@transform(
    sft_dataset=Input("/Mentor Model/datasets/sft_chat"),  # update to your dataset path
    mentor_model=ModelOutput("/Mentor Model/models/cogitator_bellum_mentor"),
)
def compute(sft_dataset, mentor_model):
    import torch
    from datasets import Dataset
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from peft import LoraConfig
    from trl import SFTTrainer, SFTConfig

    # ---- 1. Load SFT data from Foundry dataset ----
    # The Foundry dataset is expected to have one row per SFT example and a
    # column 'messages' whose value is a JSON-encoded list of {role, content}.
    df = sft_dataset.pandas()
    if "messages" not in df.columns:
        raise ValueError(
            "Expected column 'messages' in the SFT dataset. Build the dataset "
            "from sft/sft_chat.jsonl with one row per JSONL record."
        )

    def _parse(row):
        m = row["messages"]
        if isinstance(m, str):
            return {"messages": json.loads(m)}
        return {"messages": m}

    hf_ds = Dataset.from_pandas(df[["messages"]].reset_index(drop=True))
    hf_ds = hf_ds.map(_parse)
    split = hf_ds.train_test_split(test_size=0.05, seed=42)

    # ---- 2. Tokenizer + base model ----
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL_ID, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    base = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL_ID,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )

    peft_config = LoraConfig(
        r=LORA_R,
        lora_alpha=LORA_ALPHA,
        lora_dropout=LORA_DROPOUT,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=LORA_TARGET_MODULES,
    )

    # ---- 3. Train ----
    with tempfile.TemporaryDirectory() as out_dir:
        sft_config = SFTConfig(
            output_dir=out_dir,
            num_train_epochs=NUM_EPOCHS,
            per_device_train_batch_size=PER_DEVICE_BATCH,
            per_device_eval_batch_size=PER_DEVICE_BATCH,
            gradient_accumulation_steps=GRAD_ACCUM,
            gradient_checkpointing=True,
            learning_rate=LR,
            lr_scheduler_type="cosine",
            warmup_ratio=WARMUP_RATIO,
            logging_steps=10,
            eval_strategy="steps",
            eval_steps=50,
            save_strategy="no",
            bf16=True,
            max_length=MAX_SEQ_LEN,
            packing=False,
            report_to="none",
            push_to_hub=False,
        )

        trainer = SFTTrainer(
            model=base,
            args=sft_config,
            train_dataset=split["train"],
            eval_dataset=split["test"],
            peft_config=peft_config,
            processing_class=tokenizer,
        )
        trainer.train()

        # ---- 4. Wrap and publish ----
        peft_model = trainer.model           # base + LoRA adapter (PEFT-wrapped)
        peft_model.eval()

        adapter = QwenMentorAdapter(
            model=peft_model,
            tokenizer=tokenizer,
            base_model_id=BASE_MODEL_ID,
            system_prompt=MENTOR_SYSTEM_PROMPT,
            max_new_tokens=400,
            temperature=0.7,
            top_p=0.9,
        )

        mentor_model.publish(
            model_adapter=adapter,
            change_type=ModelVersionChangeType.MINOR,
        )
