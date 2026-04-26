"""
QwenMentorAdapter — Foundry ModelAdapter for the Qwen3-0.6B + LoRA mentor model.

This adapter is the bridge between Foundry and the trained model artifact:
  - save()   : called by ModelOutput.publish(...) in the training transform
  - load()   : called by ModelInput(...) at inference time
  - api()    : declares the tabular IO contract enforced by Foundry
  - predict(): batch chat completion that returns one row per input prompt

Design notes:
  - We persist the LoRA adapter weights + tokenizer + the system prompt + base
    model id. The base weights are pulled from the cached HF cache (or, if
    your tenant disallows internet egress, from a Foundry dataset uploaded
    once and copied into the env at build time — see docs/foundry/RUNBOOK.md
    for the air-gapped path).
  - Inference auto-routes to GPU if available (lightweight transform GPU
    profile or AIP Modeling Objective deployment with a GPU SKU).
  - The api() declares a single tabular input "prompts" with columns
    (system, user) and a single tabular output "responses" with columns
    (system, user, completion). This is the schema AIP Logic & Pipeline
    Builder will see when wiring the model into a flow.

Author: omnissiahcypher
"""

from __future__ import annotations

import json
import os
import shutil
from typing import List, Optional

import pandas as pd

from palantir_models.models import (
    ModelAdapter,
    ModelStateReader,
    ModelStateWriter,
    PythonEnvironment,
    CondaDependency,
)
from palantir_models.models.api import (
    DFType,
    ModelApi,
    ModelApiColumn,
    ModelInput,
    ModelOutput,
)
from palantir_models.models._types import CondaVersionExact


# ---------- Mentor system prompt (the persona this model was trained for) ----

MENTOR_SYSTEM_PROMPT = (
    "You are a senior US/NATO intelligence and military mentor. You speak from "
    "experience to a junior analyst — warm, patient, and precise. Anchor every "
    "answer in concrete tradecraft and specifics: doctrinal sources (ICD 203, "
    "JP 2-0, ATP 7-100.1, AFDP-1, etc.), exact specs (range, payload, CEP, "
    "guidance), and named threat systems. Use first person ('I', 'in my "
    "experience'). Voice markers, used sparingly: \"Here's the way to think "
    "about it…\", \"Don't conflate X with Y…\", \"The doctrinal answer is X. The "
    "practical answer is messier.\" Never write 'according to the passage' — "
    "you speak from knowledge. Expand acronyms on first use. No markdown. "
    "Faithfulness is sacred: zero invented facts, exact numbers."
)


# ---------- Adapter --------------------------------------------------------

class QwenMentorAdapter(ModelAdapter):
    """Foundry adapter for Qwen3-0.6B-Base + LoRA fine-tune on mentor Q&A."""

    ADAPTER_DIR = "lora_adapter"          # PEFT adapter weights + config
    TOKENIZER_DIR = "tokenizer"           # tokenizer files
    METADATA_FILE = "metadata.json"       # base_model_id, system prompt, gen params

    def __init__(
        self,
        model,
        tokenizer,
        base_model_id: str,
        system_prompt: str = MENTOR_SYSTEM_PROMPT,
        max_new_tokens: int = 400,
        temperature: float = 0.7,
        top_p: float = 0.9,
    ):
        self.model = model
        self.tokenizer = tokenizer
        self.base_model_id = base_model_id
        self.system_prompt = system_prompt
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature
        self.top_p = top_p

    # ---------- Foundry serialization --------------------------------------

    def save(self, state_writer: ModelStateWriter) -> None:
        """Persist LoRA adapter, tokenizer, and metadata into Foundry's model store."""
        with state_writer.extract_to_temp_dir() as tmp_dir:
            adapter_path = os.path.join(tmp_dir, self.ADAPTER_DIR)
            tok_path = os.path.join(tmp_dir, self.TOKENIZER_DIR)
            os.makedirs(adapter_path, exist_ok=True)
            os.makedirs(tok_path, exist_ok=True)

            # PEFT writes adapter_config.json + adapter_model.safetensors
            self.model.save_pretrained(adapter_path)
            self.tokenizer.save_pretrained(tok_path)

            metadata = {
                "base_model_id": self.base_model_id,
                "system_prompt": self.system_prompt,
                "max_new_tokens": self.max_new_tokens,
                "temperature": self.temperature,
                "top_p": self.top_p,
            }
            with open(os.path.join(tmp_dir, self.METADATA_FILE), "w") as f:
                json.dump(metadata, f, indent=2)

            # Walk tmp_dir and stream every file into the state_writer
            for root, _, files in os.walk(tmp_dir):
                for fn in files:
                    abs_path = os.path.join(root, fn)
                    rel_path = os.path.relpath(abs_path, tmp_dir)
                    with open(abs_path, "rb") as src, state_writer.open(rel_path, "wb") as dst:
                        shutil.copyfileobj(src, dst)

    @classmethod
    def load(cls, state_reader: ModelStateReader, container_context=None,
             external_model_context=None) -> "QwenMentorAdapter":
        """Reconstruct base + LoRA + tokenizer from Foundry's model store."""
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
        from peft import PeftModel

        with state_reader.extract_to_temp_dir() as tmp_dir:
            with open(os.path.join(tmp_dir, cls.METADATA_FILE)) as f:
                metadata = json.load(f)

            base_model_id = metadata["base_model_id"]
            adapter_path = os.path.join(tmp_dir, cls.ADAPTER_DIR)
            tok_path = os.path.join(tmp_dir, cls.TOKENIZER_DIR)

            tokenizer = AutoTokenizer.from_pretrained(tok_path, trust_remote_code=True)
            if tokenizer.pad_token is None:
                tokenizer.pad_token = tokenizer.eos_token

            # Pull base weights. On tenants with no internet egress, mirror
            # the base model into a Foundry dataset and replace base_model_id
            # with that local path before training (see RUNBOOK.md).
            base = AutoModelForCausalLM.from_pretrained(
                base_model_id,
                torch_dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32,
                device_map="auto" if torch.cuda.is_available() else None,
                trust_remote_code=True,
            )
            model = PeftModel.from_pretrained(base, adapter_path)
            model.eval()

            return cls(
                model=model,
                tokenizer=tokenizer,
                base_model_id=base_model_id,
                system_prompt=metadata["system_prompt"],
                max_new_tokens=metadata["max_new_tokens"],
                temperature=metadata["temperature"],
                top_p=metadata["top_p"],
            )

    # ---------- Foundry API contract --------------------------------------

    @classmethod
    def api(cls) -> ModelApi:
        """Declare the tabular IO contract Foundry will enforce.

        Inputs:
            prompts: pandas DataFrame with optional 'system' and required 'user' columns.
                     If 'system' is missing or null, the trained mentor system prompt is used.
        Outputs:
            responses: pandas DataFrame with columns (system, user, completion).
        """
        inputs = [
            ModelInput.Tabular(
                name="prompts",
                df_type=DFType.PANDAS,
                columns=[
                    ModelApiColumn(name="user", type=str),
                    ModelApiColumn(name="system", type=str, required=False),
                ],
            )
        ]
        outputs = [
            ModelOutput.Tabular(
                name="responses",
                columns=[
                    ModelApiColumn(name="system", type=str),
                    ModelApiColumn(name="user", type=str),
                    ModelApiColumn(name="completion", type=str),
                ],
            )
        ]
        return ModelApi(inputs, outputs)

    # ---------- Inference --------------------------------------------------

    def predict(self, prompts: pd.DataFrame) -> pd.DataFrame:
        """Generate one mentor response per prompt row."""
        import torch

        results: List[dict] = []
        device = next(self.model.parameters()).device

        for _, row in prompts.iterrows():
            user_msg = str(row["user"])
            system_msg = str(row.get("system") or self.system_prompt)

            messages = [
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg},
            ]
            input_ids = self.tokenizer.apply_chat_template(
                messages,
                return_tensors="pt",
                add_generation_prompt=True,
            ).to(device)

            with torch.no_grad():
                output_ids = self.model.generate(
                    input_ids,
                    max_new_tokens=self.max_new_tokens,
                    temperature=self.temperature,
                    top_p=self.top_p,
                    do_sample=self.temperature > 0,
                    pad_token_id=self.tokenizer.pad_token_id,
                )
            completion = self.tokenizer.decode(
                output_ids[0][input_ids.shape[-1]:],
                skip_special_tokens=True,
            ).strip()

            results.append(
                {"system": system_msg, "user": user_msg, "completion": completion}
            )

        return pd.DataFrame(results, columns=["system", "user", "completion"])

    # ---------- Conda dependencies ----------------------------------------

    @classmethod
    def dependencies(cls) -> PythonEnvironment:
        """The auto-published transforms-model-training-<rid> library handle
        is filled in by Foundry's build system. Replace the placeholder
        below with the value shown on your model page after the first build.
        See foundry/docs/RUNBOOK.md step 4."""
        from main._version import __version__ as generated_version_tag  # type: ignore
        return PythonEnvironment(
            conda_dependencies=[
                CondaDependency(
                    "transforms-model-training-<REPLACE_WITH_RID>",
                    CondaVersionExact(version=f"{generated_version_tag}"),
                    "<REPLACE_WITH_RID>",
                )
            ]
        )
