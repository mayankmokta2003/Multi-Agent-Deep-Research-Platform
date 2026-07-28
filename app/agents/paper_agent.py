from app.state.research_state import ResearchState
from app.tools.arxiv import search_papers


def paper_agent(state: ResearchState):
    tasks = state["plan"].research_steps
    paper_tasks = []
    for step in tasks:
        if step.agent == "paper_agent":
            paper_tasks.append(step.task)
    papers = []
    for task in paper_tasks:
        search_results = search_papers(task)
        papers.extend(search_results)
    return {
        "paper_results": papers
    }
