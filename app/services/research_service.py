from app.graph.builder import graph
from app.schemas.research_response import ResearchResponse
from app.database.connection import SessionLocal
from app.models.research_model import Research


def run_research(query: str):
    db = SessionLocal()
    try:
        result = graph.invoke({
            "query": query
        })
        research = Research(query=query, report=result["final_result"])
        db.add(research)
        db.commit()
        return ResearchResponse(report=result["final_result"])

    except Exception as e:
        db.rollback()
        raise RuntimeError(f"Research generation failed: {str(e)}")
    finally:
        db.close()
