from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from app.llms.mistral import get_llm
from app.state.research_state import ResearchState



class CriticOutput(BaseModel):
    approved: bool = Field(description="Whether report should be accepted.")
    score: int = Field(description="Score between 1 and 10.")
    strengths: list[str]
    weaknesses: list[str]
    missing_topics: list[str]
    feedback: str


critic_prompt = ChatPromptTemplate.from_messages(
[
(
"system",
"""
You are a senior research reviewer.
Original Query:
{query}
Review the report.
Evaluate:
1. Does it answer the query
2. Missing topics
3. Weak arguments
4. Factual consistency
5. Structure
6. Clarity
Return structured output.
"""
),
(
"human",
"{report}"
)
]
)



def critic_agent(state: ResearchState):
    llm = get_llm()
    structured_llm = llm.with_structured_output(CriticOutput)
    chain = critic_prompt | structured_llm
    response = chain.ivoke({
        "query": state["query"],
        "report": state["final_result"]
    })
    return {
    "approved": response.approved,
    "score": response.score,
    "strengths": response.strengths,
    "weaknesses": response.weaknesses,
    "missing_topics": response.missing_topics,
    "feedback": response.feedback,
}

