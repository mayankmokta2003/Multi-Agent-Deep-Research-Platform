from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from app.llms.mistral import get_llm
from app.state.research_state import ResearchState
from langchain_core.output_parsers import PydanticOutputParser


class Evaluation(BaseModel):
    groundedness: float = Field(description="Score from 1-10")
    relevance: float = Field(description="Score from 1-10")
    completeness: float = Field(description="Score from 1-10")
    hallucination_risk: str = Field(description="Low, Medium or High")
    feedback: str = Field(description="Short feedback")


parser = PydanticOutputParser(pydantic_object=Evaluation)

prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are an expert LLM evaluator.
Evaluate the answer on:
1. Groundedness (1-10)
2. Relevance (1-10)
3. Completeness (1-10)
4. Hallucination Risk (Low/Medium/High)
{format_instructions}
"""),
    ("human", """
Question:{query}
Answer:{answer}
""")
])


llm = get_llm()



chain = (
    prompt.partial(
        format_instructions=parser.get_format_instructions()
    )
    | llm
    | parser
)


def evaluator_agent(state: ResearchState):
    evaluation = chain.invoke({
        "query": state["query"],
        "answer": state["final_result"]
    })
    return {
        "evaluation": evaluation.model_dump()
    }

