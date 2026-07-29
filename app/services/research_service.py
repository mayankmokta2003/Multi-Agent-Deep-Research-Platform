from app.graph.builder import graph
from app.schemas.research_response import ResearchResponse


def run_research(query: str):
    try:
        result = graph.invoke({
            "query": query
        })
        return ResearchResponse(report=result["final_result"])

    except Exception as e:
        raise RuntimeError(f"Research generation failed: {str(e)}")

