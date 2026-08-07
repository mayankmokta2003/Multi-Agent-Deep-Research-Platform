from fastapi import HTTPException
from app.llms.gateway import call_llm
from pydantic import BaseModel


class TopicResponse(BaseModel):
    allowed: bool


def topic_guardrail(query: str):

    prompt = f"""
Your job is to classify whether the query is suitable for a research assistant.

Allow:
- research
- science
- technology
- programming
- education
- business
- medicine
- history
- finance
- reports
- analysis

Reject:
- casual chat
- jokes
- roleplay
- romance
- hacking requests
- illegal activities

Query:
{query}
"""
    response = call_llm(
        prompt=prompt,
        response_format=TopicResponse
    )

    if not response.allowed:
        raise HTTPException(
            status_code=400,
            detail="This query is outside the scope of this Research Assistant."
        )