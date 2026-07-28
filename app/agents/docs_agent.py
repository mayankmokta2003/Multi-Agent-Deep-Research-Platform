from app.state.research_state import ResearchState
from app.utils.tasks import get_tasks_for_agent
from app.retrieval.retrieve import retrieve

def docs_agent(state: ResearchState):
    docs_tasks = get_tasks_for_agent(state, "docs_agent")
    docs = []
    for task in docs_tasks:
        docs.append(retrieve())
    return {
        "docs_results": docs
    }