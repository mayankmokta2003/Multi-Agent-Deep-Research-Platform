from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate

from app.llms.mistral import get_llm
from app.state.research_state import ResearchState


class Evaluation(BaseModel):
    groundedness: float = Field(description="Score from 1-10")
    relevance: float = Field(description="Score from 1-10")
    completeness: float = Field(description="Score from 1-10")
    hallucination_risk: str = Field(description="Low | Medium | High")
    feedback: str


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert evaluator.

Evaluate the answer based on:

1. Groundedness
2. Relevance
3. Completeness
4. Hallucination Risk

Return scores from 1-10.
"""
    ),
    (
        "human",
        """
Question:
{query}

Answer:
{answer}
"""
    )
])


def evaluator_agent(state: ResearchState):

    llm = get_llm().with_structured_output(Evaluation)

    chain = prompt | llm

    evaluation = chain.invoke({
        "query": state["query"],
        "answer": state["final_result"]
    })

    return evaluation.model_dump()