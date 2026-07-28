from app.state.research_state import ResearchState
from app.utils.tasks import get_tasks_for_agent
from app.tools.tavily import search_web

def web_agent(state: ResearchState):
    web_tasks = get_tasks_for_agent(state, "web_agent")
    results = []
    for task in web_tasks:
        out = search_web(task)
        results.extend(out)
    return {"web_results": results}
