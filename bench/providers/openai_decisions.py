"""OpenAI Decisions API, called directly (one POST, no SDK).

Added 2026-10-07, after the article was published: OpenAI shipped a decision endpoint of the same
shape as Jev (typed answers with probabilities, input-only pricing) two weeks after Jev launched.
The endpoint is OpenAI-only; OpenRouter serves the same model (gpt-6-luna) as a chat model, which
is the separate `luna` arm.
"""

from __future__ import annotations

import time

import httpx

from bench.config import require_env

API = "https://api.openai.com/v1/decisions"
RETRY_STATUS = {408, 429, 500, 502, 503, 504, 524}
PRICE_PER_MTOK_INPUT = 0.10  # USD, gpt-6-luna on /v1/decisions, guide read 2026-10-07; no output charge


class DecisionsError(RuntimeError):
    pass


def evaluate(
    text: str,
    questions: list[dict],
    *,
    model: str = "gpt-6-luna",
    timeout: float = 60.0,
    retries: int = 4,
) -> dict:
    headers = {
        "Authorization": f"Bearer {require_env('OPENAI_API_KEY')}",
        "Content-Type": "application/json",
    }
    body = {"model": model, "input": text, "questions": questions}
    last = ""
    for attempt in range(1, retries + 1):
        started = time.perf_counter()
        try:
            response = httpx.post(API, headers=headers, json=body, timeout=timeout)
        except httpx.HTTPError as exc:
            last = f"transport: {exc}"
            time.sleep(2 * attempt)
            continue
        latency_ms = round((time.perf_counter() - started) * 1000, 1)
        if response.status_code in RETRY_STATUS:
            wait = response.headers.get("retry-after")
            last = f"http {response.status_code}: {response.text[:200]}"
            time.sleep(float(wait) if wait else 3 * attempt)
            continue
        if response.status_code != 200:
            raise DecisionsError(f"http {response.status_code}: {response.text[:300]}")
        data = response.json()
        usage = data.get("usage") or {}
        input_tokens = usage.get("input_tokens") or 0
        return {
            # keyed by question name, like Jev's answers, so verdict parsing stays parallel
            "answers": {a.get("name"): a for a in data.get("answers", [])},
            "usage": {
                "input_tokens": input_tokens,
                "output_tokens": usage.get("output_tokens"),
                "reasoning_tokens": None,
            },
            "cost_usd": round(input_tokens / 1_000_000 * PRICE_PER_MTOK_INPUT, 8),
            "latency_ms": latency_ms,
            "model": data.get("model", model),
            "provider": "openai",
            "finish_reason": None,
        }
    raise DecisionsError(f"gave up after {retries} attempts: {last}")
