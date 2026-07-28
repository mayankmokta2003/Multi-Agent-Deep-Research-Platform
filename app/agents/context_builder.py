from app.state.research_state import ResearchState

def context_builder(state: ResearchState):
    context = []
    context.append(f"ESER QUERY: \n{state["query"]}\n")
    context.append("# Research Papers\n")
    for paper in state["paper_results"]:
        context.append(
            f"""
            TITLE: {paper["title"]}
            Authors: {", ".join(paper["authors"])}
            Summary: {paper["summary"]}
            URL: {paper["url"]}
            """
        )
    context.append("\n Web Results\n")
    for result in state["web_results"]:
        context.append(
            f"""
            Title: {result["title"]}
            Content:{result["content"]}
            URL:{result["url"]}
            """
        )

    return {
        "merged_context": "\n".join(context)
    }