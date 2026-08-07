from fastapi import HTTPException
from app.llms.mistral import get_llm
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate


class TopicResponse(BaseModel):
    allowed: bool


prompt = ChatPromptTemplate.from_messages([
    ("system", """
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

"""),
        ("human", "query: {query}")
    ])


def topic_guardrail(query: str):
    llm = get_llm().with_structured_output(TopicResponse)
    chain = prompt | llm
    response = chain.invoke({
        "query": query
    })

    if not response.allowed:
        raise HTTPException(
            status_code=400,
            detail="This query is outside the scope of this Research Assistant."
        )