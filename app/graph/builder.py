from langgraph.graph import StateGraph, START, END
from app.agents.planner import planner_node
from app.state.research_state import ResearchState


builder = StateGraph(ResearchState)

builder.add_node("planner", planner_node)

builder.add_edge(START, "planner")
builder.add_edge("planner", END)

graph = builder.compile()



