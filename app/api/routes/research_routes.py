from fastapi import APIRouter
from typing import List
from app.schemas.research_schema import ResearchRequest
from app.services.research_service import run_research, get_research_history
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