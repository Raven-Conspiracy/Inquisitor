"""Foundry transforms-model-training package setup.

Foundry rebuilds this package on every commit and publishes it to the
internal conda channel as `transforms-model-training-<repository-rid>`.
You do not need to bump the version manually — Foundry derives it from
the git commit hash.
"""

from setuptools import find_packages, setup

setup(
    name="mentor_corpus_training",
    version="0.0.0",  # Foundry rewrites this at build time
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    description="Qwen3-0.6B + LoRA mentor SFT training transforms and model adapter.",
)
