"""Turn each arm's raw output into one comparable verdict record."""

from __future__ import annotations

import json
import re

LLAMA_GUARD_CODES = {
    "S1": "violence", "S2": "illegal", "S3": "sexual", "S4": "sexual", "S5": "harassment",
    "S6": "illegal", "S7": "illegal", "S8": "illegal", "S9": "violence", "S10": "hate",
    "S11": "self_harm", "S12": "sexual", "S13": "illegal", "S14": "illegal",
}

EMPTY = {"flag": None, "p_flag": None, "category": None, "language": None,
         "confidence": None, "severity": None}


def from_jev(answers: dict) -> dict:
    verdict = dict(EMPTY)
    flag = answers.get("flag") or {}
    if "noul" in flag:
        verdict["p_flag"] = float(flag["noul"])
        verdict["flag"] = verdict["p_flag"] >= 0.5
    category = answers.get("category") or {}
    if "choice" in category:
        verdict["category"] = category["choice"]
        verdict["confidence"] = category.get("confidence")
    language = answers.get("language") or {}
    if "choice" in language:
        verdict["language"] = language["choice"]
    severity = answers.get("severity") or {}
    if "score" in severity:
        verdict["severity"] = severity["score"]
    return verdict


def from_chat_json(text: str) -> dict:
    verdict = dict(EMPTY)
    data = _parse_json(text)
    if not isinstance(data, dict):
        return verdict
    verdict["flag"] = bool(data.get("flag")) if "flag" in data else None
    verdict["category"] = data.get("category")
    verdict["language"] = data.get("language")
    try:
        verdict["confidence"] = float(data.get("confidence"))
    except (TypeError, ValueError):
        verdict["confidence"] = None
    return verdict


def from_llama_guard(text: str) -> dict:
    """Llama Guard answers `safe` or `unsafe` plus a newline and hazard codes."""
    verdict = dict(EMPTY)
    body = text.strip().lower()
    if body.startswith("unsafe"):
        verdict["flag"] = True
        codes = re.findall(r"s\d{1,2}", body)
        verdict["category"] = LLAMA_GUARD_CODES.get(codes[0].upper(), "other") if codes else "other"
    elif body.startswith("safe"):
        verdict["flag"] = False
        verdict["category"] = "none"
    return verdict


def from_nemotron(text: str) -> dict:
    """Nemotron Content Safety answers `User Safety: safe|unsafe` and `Safety Categories: ...`."""
    verdict = dict(EMPTY)
    body = text.strip()
    data = _parse_json(body)
    if isinstance(data, dict):
        user_safety = str(data.get("User Safety") or data.get("user safety") or "").lower()
        if user_safety:
            verdict["flag"] = user_safety.startswith("unsafe")
            verdict["category"] = str(data.get("Safety Categories") or "none").lower()
            return verdict
    lowered = body.lower()
    safety = re.search(r"user safety:\s*(unsafe|safe)", lowered)
    token = safety.group(1) if safety else ("unsafe" if "unsafe" in lowered else
                                            "safe" if "safe" in lowered else None)
    if token == "unsafe":
        verdict["flag"] = True
        categories = re.search(r"safety categories:\s*(.+)", lowered)
        verdict["category"] = categories.group(1).strip() if categories else "other"
    elif token == "safe":
        verdict["flag"] = False
        verdict["category"] = "none"
    return verdict


def _parse_json(text: str) -> dict | list | None:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\n|\n```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, re.S)
        if not match:
            return None
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            return None
