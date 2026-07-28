from app.memory.save import save_memory
from app.state.research_state import ResearchState


def memory_save_agent(state: ResearchState):
    save_memory(state["query"], state["final_result"])
    return {}

