from fastapi import APIRouter
from typing import List
from app.schemas.research_schema import ResearchRequest
from app.services.research_service import run_research
from app.schemas.research_response import ResearchResponse

router = APIRouter(prefix="/research", tags=["Research"])


@router.post("", response_model=ResearchResponse)

def research(request: ResearchRequest):
    return run_research(request.query)


