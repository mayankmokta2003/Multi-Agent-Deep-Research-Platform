from fastapi import APIRouter, UploadFile, File, Request
from typing import List
from app.schemas.research_schema import ResearchRequest
from app.services.research_service import (run_research, get_research_history,
get_research_by_id,delete_research, upload_pdf)
from app.schemas.research_response import ResearchResponse, ResearchHistoryResponse
from slowapi import Limiter
from slowapi.util import get_remote_address



router = APIRouter(prefix="/research", tags=["Research"])
limiter = Limiter(key_func=get_remote_address)

@router.post("", response_model=ResearchResponse)
# @limiter.limit("5/minute")
@limiter.limit("2/minute")
def research(request: Request, body: ResearchRequest):
    return run_research(body.query)


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
def upload(file: UploadFile = File(...)):
    return upload_pdf(file)




