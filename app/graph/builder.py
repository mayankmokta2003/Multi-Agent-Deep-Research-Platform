from langgraph.graph import StateGraph, START, END
from app.agents.planner import planner_node
from app.state.research_state import ResearchState
from app.agents.paper_agent import paper_agent
from app.agents.web_agent import web_agent
from app.agents.docs_agent import docs_agent
from app.agents.context_builder import context_builder
from app.agents.writer_agent import writer_agent
from app.agents.critic_agent import critic_agent
from app.agents.memory_agent import memory_agent
from app.agents.memory_save_agent import memory_save_agent
from app.agents.cached_response_agent import cached_response_agent
from app.guardrails.input_guardrails import input_gaurdrail
from app.guardrails.output_guardrail import output_guardrail


MAX_REVISIONS = 2
def should_continue(state: ResearchState):
    if state["approved"] == True:
        return "memory_save_agent"
    if state["revision_count"] > MAX_REVISIONS:
        return "memory_save_agent"
    return "writer_agent"


def should_research(state: ResearchState):

    if state["memory_hit"] == True:
        return "cached_response_agent"
    return "planner"


builder = StateGraph(ResearchState)

builder.add_node("planner", planner_node)
builder.add_node("paper_agent", paper_agent)
builder.add_node("web_agent", web_agent)
builder.add_node("docs_agent", docs_agent)
builder.add_node("context_builder", context_builder)
builder.add_node("writer_agent", writer_agent)
builder.add_node("critic_agent", critic_agent)
builder.add_node("memory_agent", memory_agent)
builder.add_node("memory_save_agent", memory_save_agent)
builder.add_node("cached_response_agent", cached_response_agent)
builder.add_node("input_gaurdrail", input_gaurdrail)
builder.add_node("output_guardrail", output_guardrail)


builder.add_edge(START, "input_gaurdrail")
builder.add_edge("input_gaurdrail", "memory_agent")
builder.add_conditional_edges("memory_agent", should_research, {
    "cached_response_agent": "cached_response_agent", "planner": "planner"
})
builder.add_edge("cached_response_agent", END)
builder.add_edge("planner", "paper_agent")
builder.add_edge("planner", "web_agent")
builder.add_edge("planner", "docs_agent")
builder.add_edge("docs_agent", "context_builder")
builder.add_edge("paper_agent", "context_builder")
builder.add_edge("web_agent", "context_builder")
builder.add_edge("context_builder", "writer_agent")
builder.add_edge("writer_agent", "critic_agent")
builder.add_conditional_edges("critic_agent", should_continue, {
    "memory_save_agent": "memory_save_agent", "writer_agent": "writer_agent"
})
builder.add_edge("memory_save_agent", END)

graph = builder.compile()
