from app.state.research_state import ResearchState


def paper_agent(state: ResearchState):
    tasks = state["plan"].research_steps
    paper_tasks = []
    for step in tasks:
        if step.agent == "paper_agent":
            paper_tasks.append(step.task)
    papers = []
    for task in paper_tasks:
        papers.append(f"PAPER EXECUTED -> {task}")
    return {
        "paper_results": papers
    }
