from app.state.research_state import ResearchState
# merged_context

def merge_agent(state: ResearchState):
    return{
        "merged_context": {
            "query": state["query"],
            "web_results": state["web_results"],
            "paper_results": state["paper_results"],
            "docs_results": state["docs_results"],
        }
    }
