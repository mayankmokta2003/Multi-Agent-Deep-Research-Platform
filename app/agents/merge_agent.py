from app.state.research_state import ResearchState


def merge_agent(state: ResearchState):
    final = []
    final.extend(state['docs_results'])
    final.extend(state['web_results'])
    final.extend(state['paper_results'])
    return {"final_result": "\n".join(final)}