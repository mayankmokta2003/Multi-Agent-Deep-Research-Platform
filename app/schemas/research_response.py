from pydantic import BaseModel
from datetime import datetime

class ResearchResponse(BaseModel):
    report: str


class ResearchHistoryResponse(BaseModel):
    id: int
    query: str
    report: str
    evaluation: dict
    created_at: datetime

    model_config = {
        "from_attributes": True
    }