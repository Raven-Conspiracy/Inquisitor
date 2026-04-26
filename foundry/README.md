# Foundry deployment (Path 1 — native training)

This subtree contains everything needed to train the Cogitator Bellum mentor model **inside Palantir Foundry** and surface it as a tool in AIP Agent Studio.

| File | Purpose |
| --- | --- |
| `transforms-model-training/src/model_adapters/qwen_mentor_adapter.py` | `palantir_models.ModelAdapter` for Qwen3-0.6B + LoRA — implements `load`, `save`, `api`, `predict` |
| `transforms-model-training/src/model_training/train_mentor.py` | `@lightweight(gpu_type=...)` SFT training transform that publishes a Foundry model |
| `transforms-model-training/src/model_training/batch_inference.py` | Batch chat-completion transform for evaluation |
| `transforms-model-training/conda_recipe/meta.yaml` | Runtime deps (`palantir_models`, `pytorch-gpu`, `transformers`, `peft`, `trl`, …) |
| `datasets/build_sft_dataset.py` | Local helper: `sft/sft_chat.jsonl` → CSV ready for upload as a Foundry dataset |
| `docs/RUNBOOK.md` | End-to-end deployment runbook (project setup → training → AIP Logic → Agent Studio) |

Start with [`docs/RUNBOOK.md`](docs/RUNBOOK.md). The runbook references Foundry docs for every step:

- [Creating model adapters](https://palantir.com/docs/foundry/integrate-models/model-adapter-creation/)
- [Train models with GPUs](https://palantir.com/docs/foundry/model-integration/gpu-training/)
- [Models trained in Foundry — Train in Code Repositories](https://palantir.com/docs/foundry/integrate-models/model-asset-code-repositories/)
- [Register an LLM using function interfaces (`ChatCompletion`)](https://palantir.com/docs/foundry/aip/chat-completion-function-interface-quickstart/)
- [Bring Your Own Model (alt path)](https://palantir.com/docs/foundry/aip/bring-your-own-model/)

## TL;DR

```
1. python foundry/datasets/build_sft_dataset.py        # → sft_chat.csv
2. Foundry → upload sft_chat.csv as /Mentor Model/datasets/sft_chat
3. Foundry → New Code Repository (Model Training template), copy in foundry/transforms-model-training/
4. Build train_mentor.py once → copy the published RID into qwen_mentor_adapter.dependencies()
5. Build train_mentor.py again → produces /Mentor Model/models/cogitator_bellum_mentor
6. Wrap the model in a ChatCompletion function (sample in RUNBOOK §6a)
7. AIP Agent Studio → new agent → choose your ChatCompletion function as the model
```

Total time once you have a GPU resource queue: ~1 hour, most of it waiting for the conda env to resolve and the SFT job to run.
