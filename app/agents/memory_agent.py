
from app.memory.retrieve import retrieve_memory

from app.state.research_state import ResearchState


def memory_agent(state: ResearchState):
    docs = retrieve_memory(state['query'])

    if not docs:
        return{
            "memory_context": "",
            "memory_hit": False
        }

    return {
        "memory_context": docs.page_content,
        "memory_hit": True
    }