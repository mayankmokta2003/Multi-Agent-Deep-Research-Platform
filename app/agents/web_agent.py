from app.state.research_state import ResearchState


def web_agent(state: ResearchState):
    tasks = state['plan'].research_steps
    web_tasks = []
    for step in tasks:
        if step.agent == "web_agent":
            web_tasks.append(step.task)
    results = []
    for task in web_tasks:
        results.append(f"WEB EXECUTED -> {task}")
    return {"web_results": results}


