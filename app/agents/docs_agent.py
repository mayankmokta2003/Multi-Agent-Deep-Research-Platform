# from app.state.research_state import ResearchState
# from app.utils.tasks import get_tasks_for_agent
# from app.retrieval.retrieve import retrieve

# def docs_agent(state: ResearchState):
#     docs_tasks = get_tasks_for_agent(state, "docs_agent")
#     docs = []
#     for task in docs_tasks:
#         result = retrieve(task)
#         print("=" * 50)
#         print(result)
#         print("--------------------------" * 50)
#         docs.append(result)
#     return {
#         "docs_results": docs
#     }






# from app.state.research_state import ResearchState
# from app.utils.tasks import get_tasks_for_agent
# from app.retrieval.retrieve import retrieve


# def docs_agent(state: ResearchState):

#     print("DOCS AGENT EXECUTED")

#     docs_tasks = get_tasks_for_agent(state, "docs_agent")

#     print("Tasks:", docs_tasks)

#     docs = []

#     for task in docs_tasks:
#         result = retrieve(task)

#         print("Retrieved Docs:", len(result))

#         docs.append(result)

#     return {
#         "docs_results": docs
#     }






from app.state.research_state import ResearchState
from app.retrieval.retrieve import retrieve
from app.utils.tasks import get_tasks_for_agent


def docs_agent(state: ResearchState):

    docs_tasks = get_tasks_for_agent(state, "docs_agent")

    # Fallback
    if not docs_tasks:
        docs_tasks = [state["query"]]

    docs = []

    for task in docs_tasks:
        docs.extend(retrieve(task))

    return {
        "docs_results": docs
    }