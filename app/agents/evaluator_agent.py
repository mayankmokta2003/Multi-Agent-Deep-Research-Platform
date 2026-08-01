# from pydantic import BaseModel, Field
# from langchain_core.prompts import ChatPromptTemplate

# from app.llms.mistral import get_llm
# from app.state.research_state import ResearchState


# class Evaluation(BaseModel):
#     groundedness: float = Field(description="Score from 1-10")
#     relevance: float = Field(description="Score from 1-10")
#     completeness: float = Field(description="Score from 1-10")
#     hallucination_risk: str = Field(description="Low | Medium | High")
#     feedback: str


# prompt = ChatPromptTemplate.from_messages([
#     (
#         "system",
#         """
# You are an expert evaluator.

# Evaluate the answer based on:

# 1. Groundedness
# 2. Relevance
# 3. Completeness
# 4. Hallucination Risk

# Return scores from 1-10.
# """
#     ),
#     (
#         "human",
#         """
# Question:
# {query}

# Answer:
# {answer}
# """
#     )
# ])


# def evaluator_agent(state: ResearchState):

#     llm = get_llm().with_structured_output(Evaluation)

#     chain = prompt | llm

#     evaluation = chain.invoke({
#         "query": state["query"],
#         "answer": state["final_result"]
#     })

#     return evaluation.model_dump()












from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate

from app.llms.mistral import get_llm


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


def evaluate_response(query: str, context: str, answer: str):

    llm = get_llm().with_structured_output(Evaluation)

    chain = evaluator_prompt | llm

    evaluation = chain.invoke({
        "query": query,
        "context": context,
        "answer": answer
    })

    return evaluation.model_dump()