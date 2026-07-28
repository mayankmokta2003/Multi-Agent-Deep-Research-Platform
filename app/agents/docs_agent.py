from app.state.research_state import ResearchState

def docs_agent(state: ResearchState):
    tasks = state["plan"].research_steps
    docs_tasks = []
    for step in tasks:
        if step.agent == "docs_agent":
            docs_tasks.append(step.task)
    results = []
    for task in docs_tasks:
        results.append(f"DOCS EXECUTED -> {task}")
    return {
        "docs_results": results
    }