from langgraph.graph import StateGraph, START, END
from app.agents.planner import planner_node
from app.state.research_state import ResearchState
from app.agents.paper_agent import paper_agent
from app.agents.web_agent import web_agent
from app.agents.docs_agent import docs_agent
from app.agents.context_builder import context_builder
from app.agents.writer_agent import writer_agent
from app.agents.critic_agent import critic_agent
from app.agents.memory_agent import retrieve_memory
from app.agents.citation_agent import citation_agent



MAX_REVISIONS = 2

def should_continue(state: ResearchState):
    if state["approved"] == True:
        return END
    if state["revision_count"] > MAX_REVISIONS:
        return END
    return "writer_agent"




builder = StateGraph(ResearchState)

builder.add_node("planner", planner_node)
builder.add_node("paper_agent", paper_agent)
builder.add_node("web_agent", web_agent)
builder.add_node("docs_agent", docs_agent)
builder.add_node("context_builder", context_builder)
builder.add_node("writer_agent", writer_agent)
builder.add_node("critic_agent", critic_agent)
builder.add_node("retrieve_memory", retrieve_memory)
builder.add_node("citation_agent", citation_agent)


builder.add_edge(START, "retrieve_memory")
builder.add_edge("retrieve_memory", "planner")
builder.add_edge("planner", "paper_agent")
builder.add_edge("planner", "web_agent")
builder.add_edge("planner", "docs_agent")
builder.add_edge("docs_agent", "context_builder")
builder.add_edge("paper_agent", "context_builder")
builder.add_edge("web_agent", "context_builder")
builder.add_edge("context_builder", "writer_agent")
builder.add_edge("writer_agent", "critic_agent")
builder.add_conditional_edges("critic_agent", should_continue)


graph = builder.compile()
