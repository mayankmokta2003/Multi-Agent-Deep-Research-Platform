from fastapi import APIRouter
from typing import List
from app.schemas.research_schema import ResearchRequest
from app.services.research_service import run_research, get_research_history, get_research_by_id,delete_research
from app.schemas.research_response import ResearchResponse, ResearchHistoryResponse

router = APIRouter(prefix="/research", tags=["Research"])


@router.post("", response_model=ResearchResponse)
def research(request: ResearchRequest):
    return run_research(request.query)


@router.get(
    "/history",
    response_model=List[ResearchHistoryResponse],
)
def history():
    return get_research_history()



@router.get(
    "/{research_id}",
    response_model=ResearchHistoryResponse,
)
def research_by_id(research_id: int):
    return get_research_by_id(research_id)



@router.delete("/{research_id}")
def delete(research_id: int):
    return delete_research(research_id)



@router.post("/upload")
