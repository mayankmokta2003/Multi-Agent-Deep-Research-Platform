from langgraph.graph import StateGraph, START, END
from app.agents.planner import planner_node
from app.state.research_state import ResearchState
from app.agents.paper_agent import paper_agent


builder = StateGraph(ResearchState)

builder.add_node("planner", planner_node)
builder.add_node("paper_agent", paper_agent)

builder.add_edge(START, "planner")
builder.add_edge("planner", "paper_agent")
builder.add_edge("paper_agent", END)

graph = builder.compile()

