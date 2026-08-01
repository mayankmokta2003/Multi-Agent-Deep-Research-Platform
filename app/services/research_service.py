from app.graph.builder import graph
from app.schemas.research_response import ResearchResponse
from app.graph.graph_runner import run_graph
from app.database.connection import SessionLocal
from app.models.research_model import Research
from fastapi import HTTPException, UploadFile
from app.agents.evaluator_agent import evaluate_response
from app.retrieval.ingest import ingest_pdf
import json
import time
import os


def run_research(query: str):
    db = SessionLocal()
    try:
        result = run_graph(query)
        evaluation = evaluate_response(
            query = query,
            context = result.get("merged_context", ""),
            answer = result["final_result"]
        )
        research = Research(query=query, report=result["final_result"])
        db.add(research)
        db.commit()
        return ResearchResponse(report=result["final_result"], evaluation=evaluation)

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
        return {"message": "Research deleted successfully"}
    finally:
        db.close()




UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
def upload_pdf(file: UploadFile):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as pdf:
        pdf.write(file.file.read())
    ingest_pdf(file_path)
    return {
        "message": "PDF uploaded successfully.",
        "filename": file.filename,
    }


