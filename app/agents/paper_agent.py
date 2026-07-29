from app.state.research_state import ResearchState
from app.tools.arxiv import search_papers
from app.utils.tasks import get_tasks_for_agent


def paper_agent(state: ResearchState):
    paper_tasks = get_tasks_for_agent(state, "paper_agent")
    papers = []
    for task in paper_tasks:
        search_results = search_papers(task)
        papers.extend(search_results)
    return {
        "paper_results": papers
    }

