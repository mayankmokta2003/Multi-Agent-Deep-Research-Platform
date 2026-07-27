from typing import TypedDict
from app.agents.planner import PlannerOutput


class ResearchState(TypedDict):
    query: str
    plan: PlannerOutput
    web_results: list
    paper_results: list
    docs_results: list
    final_result: str