"""
Foundry batch inference transform — load the trained mentor model and run
chat completion over a Foundry dataset of prompts.

Use this for offline evaluation, mass Q&A regression, or pipeline-style
generation. For interactive AIP Agent Studio use, see foundry/docs/RUNBOOK.md
section "Wiring the model into AIP Logic".
"""

from transforms.api import transform, Input, Output, lightweight
from palantir_models.transforms import ModelInput
from palantir_models.models import ModelAdapter


@lightweight(gpu_type="NVIDIA_T4")
@transform(
    prompts_input=Input("/Mentor Model/datasets/eval_prompts"),
    mentor_model=ModelInput("/Mentor Model/models/cogitator_bellum_mentor"),
    completions_output=Output("/Mentor Model/datasets/eval_completions"),
)
def compute(prompts_input, mentor_model: ModelAdapter, completions_output):
    """Reads a 'user' (and optional 'system') column, writes mentor completions."""
    df_in = prompts_input.pandas()

    # The adapter's api() declared a single tabular input named 'prompts'
    # with optional 'system' column. ModelAdapter.transform routes that
    # through predict() and returns the named-tuple of outputs.
    result = mentor_model.transform(prompts=df_in)
    df_out = result.responses

    completions_output.write_pandas(df_out)
