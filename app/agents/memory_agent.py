
from app.memory.retrieve import retrieve_memory

from app.state.research_state import ResearchState


def memory_agent(state: ResearchState):
    docs = retrieve_memory(state['query'])
    context = ""
    for doc in docs:
        context += doc.page_content
        context += "\n\n"
    return context