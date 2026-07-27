from langchain_core.prompts import ChatPromptTemplate
from app.llms.mistral import get_llm
from pydantic import BaseModel




class ResearchStep(BaseModel):
    agent: str
    task: str


class PlannerOutput(BaseModel):
    research_steps: list[ResearchStep]


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert research planner. "
            "Create a short research plan for the given topic.",
        ),
        ("human", "{query}"),
    ]
)


def planner_node(state):
    llm = get_llm()
    structured_llm = llm.with_structured_output(PlannerOutput)
    chain = prompt | structured_llm
    response = chain.invoke({
        "query": state["query"]
    })
    return {"plan": response.content}




