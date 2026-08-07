from fastapi import HTTPException

BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "ignore all previous instructions",
    "forget previous instructions",
    "forget your instructions",
    "system prompt",
    "developer prompt",
    "developer message",
    "reveal your prompt",
    "show your prompt",
    "print your prompt",
    "repeat your instructions",
    "act as system",
    "bypass",
    "jailbreak",
]


def prompt_injection_guardrail(query: str):
    text = query.lower()
    for pattern in BLOCKED_PATTERNS:
        if pattern in text:
            raise HTTPException(
                status_code=400,
                detail="Prompt injection attempt detected."
            )