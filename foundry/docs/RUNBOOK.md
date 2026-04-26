# Foundry Deployment Runbook

End-to-end recipe to deploy the Cogitator Bellum mentor model in Palantir Foundry and surface it as a tool inside an AIP Agent. Path 1 from the project plan: train inside Foundry, publish the model as a Foundry resource, expose it to AIP via a `ChatCompletion` function, wire it into AIP Agent Studio.

> Prereqs: a Foundry tenant with AIP enabled, a project that has a GPU resource queue assigned (for training), and your user added to that queue.

## 0. Repo layout you will recreate inside Foundry

```
foundry/
  transforms-model-training/        ← Foundry "Model Training" code repo
    src/
      _version.py                    (Foundry overwrites at build time)
      model_adapters/
        qwen_mentor_adapter.py       (the ModelAdapter Foundry calls)
      model_training/
        train_mentor.py              (LoRA SFT training transform)
        batch_inference.py           (batch ChatCompletion transform)
    conda_recipe/meta.yaml           (palantir_models + peft + trl + …)
    setup.py
  datasets/
    build_sft_dataset.py             (local helper → sft_chat.csv)
  docs/RUNBOOK.md                    (this file)
```

## 1. Build the SFT dataset CSV locally

```bash
python foundry/datasets/build_sft_dataset.py
# → foundry/datasets/sft_chat.csv  (490 rows, columns: messages, chunk_id, bucket, doc_id)
```

`messages` is JSON-encoded `[{role, content}, …]` so the row stays a single CSV cell. The training transform parses it back with `json.loads`.

## 2. Create the Foundry project layout

In Foundry, in your project (e.g. `Mentor Model`):

| Path | Type | Purpose |
| --- | --- | --- |
| `/Mentor Model/datasets/sft_chat` | Dataset | Upload `sft_chat.csv` here. |
| `/Mentor Model/datasets/eval_prompts` | Dataset | Optional. Columns: `user`, `system?`. Used by `batch_inference.py`. |
| `/Mentor Model/datasets/eval_completions` | Dataset | Output of `batch_inference.py`. |
| `/Mentor Model/models/cogitator_bellum_mentor` | Model | Foundry creates this on first training build. |

Upload paths:

```
Foundry → Files → New dataset → Upload sft_chat.csv → save at /Mentor Model/datasets/sft_chat
```

If your tenant allows pip/conda egress, skip the next paragraph. Otherwise (air-gapped tenant), mirror the base model files once:

1. Locally: `huggingface-cli download Qwen/Qwen3-0.6B-Base --local-dir ./qwen_base`
2. Upload `qwen_base/` as a Foundry dataset at `/Mentor Model/datasets/qwen3_0_6b_base`.
3. In `train_mentor.py`, change `BASE_MODEL_ID = "Qwen/Qwen3-0.6B-Base"` to a path the transform mounts from that dataset, and pass that same path through `QwenMentorAdapter(base_model_id=...)` so `load()` finds it at inference time too.

## 3. Create the Code Repository

1. Open **Code Repositories** → **New repository** → choose the **Model Training** template.
2. Name it `mentor-corpus-training`. Place it inside the same project that has the GPU resource queue.
3. Once initialized, replace the template's contents with the files from `foundry/transforms-model-training/`:
   - copy `src/model_adapters/qwen_mentor_adapter.py`
   - copy `src/model_training/train_mentor.py` and `src/model_training/batch_inference.py`
   - replace `conda_recipe/meta.yaml` with ours
   - delete the template's example sklearn adapter and example training transform

4. Toggle **Show hidden files** in the repo. In the most-nested `build.gradle`, add:
   ```groovy
   environment {
       'CONDA_OVERRIDE_CUDA': '12.1'   // match the CUDA version of your GPU SKU
   }
   ```
   Per [Foundry GPU docs](https://palantir.com/docs/foundry/model-integration/gpu-training/), this is required so conda installs the GPU build of `pytorch`.

## 4. First build → fill in the adapter RID

The **Model Adapter Library** auto-publishes itself as a conda package named `transforms-model-training-<repository-rid>`. The first build will fail to run inference because `qwen_mentor_adapter.py:dependencies()` has a placeholder. Fix:

1. Click **Build** on `train_mentor.py`. Wait for the conda environment to resolve (the repo will publish `transforms-model-training-<rid>` even if the training step itself fails on data path issues).
2. Open the published package on the model page or in the repo's **Releases** tab. Copy the full RID, e.g. `ri.stemma.main.repository.91e66421-…`.
3. In `qwen_mentor_adapter.py`, replace both `<REPLACE_WITH_RID>` strings with the value above. Commit.
4. Build again. This time the training transform should succeed and `mentor_model.publish(...)` will create `/Mentor Model/models/cogitator_bellum_mentor` with version `0.1.0` (MINOR bump from the published `ModelVersionChangeType.MINOR`).

## 5. Verify with batch inference

1. Make a tiny CSV `eval_prompts.csv`:
   ```csv
   user
   "What is the difference between collection management and analysis tasking?"
   "Walk me through the doctrinal use of the Iskander-M and what changes when it's deployed in Kaliningrad."
   ```
2. Upload as a dataset at `/Mentor Model/datasets/eval_prompts`.
3. Build `batch_inference.py`. The output dataset `/Mentor Model/datasets/eval_completions` should contain a `completion` column with mentor-style answers.

If the answers look templated or generic, the model is loading the base weights without the LoRA adapter — re-check that `qwen_mentor_adapter.QwenMentorAdapter.save` ran and the model resource shows non-empty artifacts.

## 6. Wire the model into AIP Logic via `ChatCompletion`

The cleanest way to make the Foundry-trained model callable from AIP Agent Studio is to wrap it in a `ChatCompletion` function. There are two flavors:

### 6a. Python `ChatCompletion` function (recommended for in-Foundry models)

In a TypeScript/Python Functions repo, create a function that loads the model with `palantir_models.transforms.ModelInput`, calls `predict`, and returns a `FunctionsGenericChatCompletionResponse`. Sketch:

```python
# functions/mentor_chat.py
from functions.api import function, ExternalSystems
from palantir_models import ModelAdapter
from palantir_models.transforms import ModelInput
from language_model_service.api import (
    GenericChatCompletionRequestMessages,
    GenericCompletionParams,
    GenericChatCompletionResponse,
    ChatCompletion,
)

@ChatCompletion
def mentor_chat(
    messages: GenericChatCompletionRequestMessages,
    params: GenericCompletionParams,
    model: ModelAdapter = ModelInput("/Mentor Model/models/cogitator_bellum_mentor"),
) -> GenericChatCompletionResponse:
    user_msg = next((m.content for m in reversed(messages) if m.role == "USER"), "")
    system_msg = next((m.content for m in messages if m.role == "SYSTEM"), None)

    import pandas as pd
    df = pd.DataFrame([{"user": user_msg, "system": system_msg}])
    out = model.predict(df).iloc[0]["completion"]

    return GenericChatCompletionResponse(completion=out)
```

> Confirm the exact import paths against your tenant's installed `palantir_models` and `language_model_service` versions — Palantir versions these in lockstep. The TypeScript variant for `ChatCompletion` is documented in [Register an LLM using function interfaces](https://palantir.com/docs/foundry/aip/chat-completion-function-interface-quickstart/) and is the same shape used here.

### 6b. (alternative) BYOM / Registered Model

If you would rather host the model outside Foundry but call it from AIP, use Foundry's [Bring Your Own Model](https://palantir.com/docs/foundry/aip/bring-your-own-model/) flow with a REST source pointing at an HF Inference Endpoint or Fireworks/SageMaker hosting your trained adapter. Path 2 from the project plan; not needed if you went Path 1.

Once the function builds, AIP Logic will see it under **Registered Models**.

## 7. Build the AIP Agent

1. Open **AIP Agent Studio** → **Create new agent** → name it `Cogitator Bellum Mentor`.
2. **Agent configuration**: paste the same system prompt that's in `MENTOR_SYSTEM_PROMPT` (the model was trained on this — keep it consistent).
3. **Model**: under model selection, choose your registered `mentor_chat` function (from step 6a).
4. **Retrieval context** (optional but high value): add an Ontology context object pointing at a `MentorCorpusChunk` object type built from `chunks.jsonl` so the agent can ground answers in the original 17,241-chunk corpus when the model is uncertain.
5. **Tools** (optional): add `query_objects` over the corpus object type, plus any Action your application needs.

Test the agent in Agent Studio with a few prompts from `qa/qa_combined.jsonl` to confirm it produces mentor-voice answers.

## 8. Embedding in apps

Three deployment surfaces, all listed in [Leveling up your AIP agents with the Palantir API](https://community.palantir.com/t/leveling-up-your-aip-agents-with-the-palantir-api/2956):

- **AIP Threads** for ad-hoc analyst chat.
- **Workshop AIP Interactive widget** for embedding the agent in an internal app.
- **Foundry public API** (`foundry.v2.aip_agents.Agent.Session.streaming_continue`) for any custom front-end.

## 9. Updating the model

Re-running the training transform produces a new model version (configurable via `ModelVersionChangeType.MAJOR/MINOR/PATCH` in `train_mentor.py`). AIP will pick up the new version automatically the next time the function reloads — pin a specific version via the model resource page if you want production stability.

## Common gotchas

- **GPU not detected at runtime.** Confirm `pytorch-gpu` is in `meta.yaml`, `CONDA_OVERRIDE_CUDA` is set in the nested `build.gradle`, and the project's resource queue actually includes the requested SKU. Preview builds run on CPU regardless — only full builds get GPU.
- **`AutoModelForCausalLM` 401/403.** The base model `Qwen/Qwen3-0.6B-Base` is open weights, but if your tenant blocks the HF CDN you must mirror the base into a Foundry dataset (see step 2, air-gapped path) and pass the local path through `BASE_MODEL_ID`.
- **Adapter RID placeholder still in code.** Inference will fail with a conda solve error. Re-read step 4.
- **`PeftModel.from_pretrained` on CPU.** It works but is very slow for first inference. The adapter's `load()` already routes to GPU when `torch.cuda.is_available()`. If your AIP function deployment is CPU-only, expect ~20-40s per response on a 0.6B model — fine for a chat tool, slow for batch.
- **Tokenizer pad token.** Already handled in both training and adapter — do not remove the `if tokenizer.pad_token is None` guards.
