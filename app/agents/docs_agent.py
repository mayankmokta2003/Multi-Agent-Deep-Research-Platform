from app.state.research_state import ResearchState
from app.retrieval.retrieve import retrieve
from app.utils.tasks import get_tasks_for_agent


def docs_agent(state: ResearchState):
    docs_tasks = get_tasks_for_agent(state, "docs_agent")
    if not docs_tasks:
        docs_tasks = [state["query"]]
    docs = []
    for task in docs_tasks:
        docs.extend(retrieve(task))
    return {
        "docs_results": docs
    }