"""Thin OpenRouter chat-completions client with usage accounting."""

from __future__ import annotations

import time

import httpx

from bench.config import require_env

API = "https://openrouter.ai/api/v1/chat/completions"
RETRY_STATUS = {408, 429, 500, 502, 503, 524}


class OpenRouterError(RuntimeError):
    pass


def _headers() -> dict[str, str]:
    return {
        "Authorization": f"Bearer {require_env('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/webmaster-ramos/jev-multilingual-benchmark",
        "X-Title": "jev-multilingual-benchmark",
    }


def chat(
    model: str,
    messages: list[dict[str, str]],
    *,
    schema: dict | None = None,
    schema_name: str = "verdict",
    temperature: float | None = 0.0,
    max_tokens: int = 800,
    reasoning_effort: str | None = None,
    timeout: float = 120.0,
    retries: int = 4,
) -> dict:
    body: dict = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "usage": {"include": True},
    }
    if temperature is not None:
        body["temperature"] = temperature
    if schema is not None:
        body["response_format"] = {
            "type": "json_schema",
            "json_schema": {"name": schema_name, "strict": True, "schema": schema},
        }
    if reasoning_effort:
        body["reasoning"] = {"effort": reasoning_effort}

    last = ""
    for attempt in range(1, retries + 1):
        started = time.perf_counter()
        try:
            response = httpx.post(API, headers=_headers(), json=body, timeout=timeout)
        except httpx.HTTPError as exc:
            last = f"transport: {exc}"
            time.sleep(2 * attempt)
            continue
        latency_ms = round((time.perf_counter() - started) * 1000, 1)
        if response.status_code in RETRY_STATUS:
            last = f"http {response.status_code}: {response.text[:200]}"
            time.sleep(3 * attempt)
            continue
        if response.status_code != 200:
            raise OpenRouterError(f"http {response.status_code}: {response.text[:300]}")
        data = response.json()
        if "error" in data:
            last = f"api error: {str(data['error'])[:200]}"
            time.sleep(3 * attempt)
            continue
        choice = data["choices"][0]
        usage = data.get("usage") or {}
        details = usage.get("completion_tokens_details") or {}
        return {
            "text": choice["message"].get("content") or "",
            "usage": {
                "input_tokens": usage.get("prompt_tokens"),
                "output_tokens": usage.get("completion_tokens"),
                "reasoning_tokens": details.get("reasoning_tokens"),
            },
            "cost_usd": usage.get("cost"),
            "latency_ms": latency_ms,
            "model": data.get("model"),
            "provider": data.get("provider"),
            "finish_reason": choice.get("finish_reason"),
        }
    raise OpenRouterError(f"gave up after {retries} attempts: {last}")
