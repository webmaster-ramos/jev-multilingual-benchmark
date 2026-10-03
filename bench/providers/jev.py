"""TypeSafe System One endpoint, called directly (one POST, no SDK)."""

from __future__ import annotations

import time

import httpx

from bench.config import require_env

API = "https://api.typesafe.ai/v1/systemone"
RETRY_STATUS = {408, 429, 500, 502, 503, 524}
PRICE_PER_MTOK_INPUT = 0.042  # USD, list price on 2026-10-02; output is free


class JevError(RuntimeError):
    pass


def evaluate(
    state: dict | str,
    questions: dict[str, dict],
    *,
    model: str = "jev-1.13.0",
    timeout: float = 60.0,
    retries: int = 4,
) -> dict:
    headers = {
        "Authorization": f"Bearer {require_env('TYPESAFE_API_KEY')}",
        "Content-Type": "application/json",
    }
    body = {"state": state, "model": model, "questions": questions}
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
            raise JevError(f"http {response.status_code}: {response.text[:300]}")
        data = response.json()
        usage = data.get("usage") or {}
        input_tokens = usage.get("input_tokens") or 0
        return {
            "answers": data.get("answers", {}),
            "usage": {
                "input_tokens": input_tokens,
                "output_tokens": usage.get("output_tokens"),
                "reasoning_tokens": None,
            },
            "cost_usd": round(input_tokens / 1_000_000 * PRICE_PER_MTOK_INPUT, 8),
            "latency_ms": latency_ms,
            "model": data.get("model"),
            "provider": "typesafe",
            "finish_reason": None,
        }
    raise JevError(f"gave up after {retries} attempts: {last}")
