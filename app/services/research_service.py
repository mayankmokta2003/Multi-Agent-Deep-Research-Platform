from app.graph.builder import graph
from app.schemas.research_response import ResearchResponse
from app.graph.graph_runner import run_graph
from app.database.connection import SessionLocal
from app.models.research_model import Research
from fastapi import HTTPException



def run_research(query: str):
    db = SessionLocal()
    try:
        result = run_graph(query)
        research = Research(query=query, report=result["final_result"])
        db.add(research)
        db.commit()
        return ResearchResponse(report=result["final_result"])

    except Exception as e:
        db.rollback()
        raise RuntimeError(f"Research generation failed: {str(e)}")
    finally:
        db.close()



def get_research_history():
    db = SessionLocal()
    try:
        return db.query(Research).order_by(Research.created_at.desc()).all()
    finally:
        db.close()



def get_research_by_id(research_id: int):
    db = SessionLocal()
    try:
        research = (
            db.query(Research)
            .filter(Research.id == research_id)
            .first()
        )
        if research is None:
            raise HTTPException(status_code=404, detail="Research not found")
        return research
    finally:
        db.close()



def delete_research(research_id: int):
    db = SessionLocal()
    try:
        research = (
            db.query(Research)
            .filter(Research.id == research_id)
            .first()
        )
        if research is None:
            raise HTTPException(status_code=404, detail="Research not found")
        db.delete(research)
        db.commit()
        return {
            "message": "Research deleted successfully"
        }

    finally:
        db.close()




def upload_pdf(file: UploadFile):
    