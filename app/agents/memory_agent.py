
from app.memory.retrieve import retrieve_memory

from app.state.research_state import ResearchState


def memory_agent(state: ResearchState):
    report = retrieve_memory(state['query'])
    print("MEMORY____________________________ False")
    if not report:
        return{
            "memory_context": "",
            "memory_hit": False
        }
    
    print("MEMORY____________________________ True")
    return {
        "memory_context": report,
        "memory_hit": True
    }