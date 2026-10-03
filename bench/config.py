"""Arms (model configurations) and environment."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

DATA_DIR = ROOT / "data"
RESULTS_DIR = ROOT / "results"


@dataclass(frozen=True)
class Arm:
    key: str
    provider: str  # "jev" | "openrouter"
    model: str
    kind: str  # "decision" | "chat_json" | "guard_llama" | "guard_nemotron" | "guard_policy"
    note: str = ""
    reasoning_effort: str | None = None
    max_tokens: int = 800
    temperature: float | None = 0.0
    default: bool = True  # False: runnable with --arms, not part of the comparison


ARMS: dict[str, Arm] = {
    "jev": Arm(
        key="jev",
        provider="jev",
        model="jev-1.13.0",
        kind="decision",
        note="TypeSafe System One model, pinned version. Typed answers with probabilities.",
    ),
    "gpt5mini": Arm(
        key="gpt5mini",
        provider="openrouter",
        model="openai/gpt-5-mini",
        kind="chat_json",
        note="Chat model + strict JSON schema. Same model family as a production Magento "
        "validator.",
        reasoning_effort="low",
        max_tokens=1000,
        temperature=None,
    ),
    "flashlite": Arm(
        key="flashlite",
        provider="openrouter",
        model="google/gemini-2.5-flash-lite",
        kind="chat_json",
        note="Cheapest Google chat model with structured output.",
        max_tokens=600,
    ),
    "gemma4": Arm(
        key="gemma4",
        provider="openrouter",
        model="google/gemma-4-26b-a4b-it",
        kind="chat_json",
        note="Open-weight Google model with structured output.",
        max_tokens=600,
    ),
    "llamaguard": Arm(
        key="llamaguard",
        provider="openrouter",
        model="meta-llama/llama-guard-4-12b",
        kind="guard_llama",
        note="Fixed MLCommons hazard taxonomy (S1-S14). Plain profanity is not a hazard there.",
        max_tokens=30,
    ),
    "safeguard": Arm(
        key="safeguard",
        provider="openrouter",
        model="openai/gpt-oss-safeguard-20b",
        kind="guard_policy",
        note="Policy-conditioned safety reasoner: the policy text goes in the system prompt. "
        "Reasoning can run past 900 tokens even at low effort; upstream rate-limits at 3 workers.",
        reasoning_effort="low",
        max_tokens=2000,
        temperature=None,
    ),
    "nemotron": Arm(
        key="nemotron",
        provider="openrouter",
        model="nvidia/nemotron-3.5-content-safety:free",
        kind="guard_nemotron",
        note="4B guard fine-tuned from Gemma-3-4B, Aegis taxonomy (includes Profanity). Free "
        "route. "
        "Emits 110-180 reasoning tokens before the verdict, so the cap must leave room. "
        "Dropped from the comparison on 2026-10-02: no probability, slower and less accurate "
        "than the other guards, and the free route is capped per day.",
        max_tokens=512,
        default=False,
    ),
}


DEFAULT_ARMS = [key for key, arm in ARMS.items() if arm.default]


def require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"{name} is not set (put it in .env or export it)")
    return value
