from app.state.research_state import ResearchState


def citation_agent(state: ResearchState):
    report = state['final_result']
    sources = state["sources"]
    if not sources:
        return {}
    citation_text = "\n\n---\n## SOURCES\n"
    seen = set()

    for i, source in enumerate(sources, start=1):
        key = (source["title"], source["url"])
        if key in seen:
            continue
        seen.add(key)
        title = source["title"] or "Untitled"
#         if source["title"]:
#           title = source["title"]
#         else:
#           title = "Untitled"
        url = source["url"]
        source_type = source["type"]
        if url:
            citation_text += (f"{i}. [{source_type.upper()}]" f"{title}\n   {url}\n")
        else:
            citation_text += (f"{i}. [{source_type.upper()}] " f"{title}\n")
        
    return {"final_result": report + citation_text}