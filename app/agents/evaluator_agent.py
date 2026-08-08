
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from app.state.research_state import ResearchState
from app.llms.mistral import get_llm
from langchain_litellm import ChatLiteLLM
from app.utils.retry import with_retry


class Evaluation(BaseModel):
    groundedness: float = Field(description="Score from 1 to 10")
    relevance: float = Field(description="Score from 1 to 10")
    completeness: float = Field(description="Score from 1 to 10")
    hallucination_risk: str = Field(description="Low, Medium or High")
    feedback: str


evaluator_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an LLM response evaluator.

Evaluate the generated answer against the user's query and
the evidence used to generate it.

Evaluate:

1. Groundedness: Is the answer supported by the evidence?
2. Relevance: Does the answer directly answer the query?
3. Completeness: Does it sufficiently cover the query?
4. Hallucination Risk: Low, Medium, or High.

Give scores from 1 to 10.
Keep feedback short and specific.
Return the answer in json
"""
    ),
    (
        "human",
        """
User Query:
{query}

Evidence:
{context}

Generated Answer:
{answer}
"""
    )
])




primary_llm = ChatLiteLLM(model="mistral/mistral-small-latest")
fallback_llm = ChatLiteLLM(model="gemini/gemini-2.5-flash")

llm = primary_llm.with_fallbacks([fallback_llm])




# def evaluate_response(state: ResearchState):
#     structured_llm = llm.with_structured_output(Evaluation)
#     chain = evaluator_prompt | structured_llm

#     evaluation = chain.invoke({
#         "query": state["query"],
#         "context": state.get("merged_context", ""),
#         "answer": state["final_result"]
#     })
#     return {"evaluation": evaluation}
    

def evaluate_response(state: ResearchState):
    structured_llm = llm.with_structured_output(Evaluation)
    chain = evaluator_prompt | structured_llm

    evaluation = with_retry(chain.invoke, {
        "query": state["query"],
        "context": state.get("merged_context", ""),
        "answer": state["final_result"]
    })
    return {"evaluation": evaluation}