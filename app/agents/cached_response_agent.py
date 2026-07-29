from app.state.research_state import ResearchState


def cached_response_agent(state: ResearchState):

    return {
        "final_result": state["memory_context"]
    }