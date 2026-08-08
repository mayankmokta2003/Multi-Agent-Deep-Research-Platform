from langchain_core.prompts import ChatPromptTemplate
# from app.state.research_state import ResearchState
from app.llms.mistral import get_llm
from app.llms.gateway import call_llm
from langchain_litellm import ChatLiteLLM
from pydantic import BaseModel, Field
from app.utils.retry import with_retry



class ResearchStep(BaseModel):
    agent: str = Field(description="Agent responsible for this task")
    task: str = Field(description="Task to perform")


class PlannerOutput(BaseModel):
    research_steps: list[ResearchStep]



planner_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are the Planner Agent.
Break the user's research query into small executable tasks.
Available agents:
1. web_agent (Latest news, blogs, documentation, websites)
2. paper_agent (Research papers)
3. docs_agent (Uploaded PDFs)
Return ONLY valid JSON.
""",
        ),
        ("human", "{query}"),
    ]
)



primary_llm = ChatLiteLLM(model="mistral/mistral-small-latest")
fallback_llm = ChatLiteLLM(model="gemini/gemini-2.5-flash")
llm = primary_llm.with_fallbacks([fallback_llm])


def planner_node(state):
    structured_llm = llm.with_structured_output(PlannerOutput)
    chain = planner_prompt | structured_llm
    response = with_retry(
        chain.invoke,{
            "query": state["query"]
        }
    )
    # print(response)
    return {"plan": response}





