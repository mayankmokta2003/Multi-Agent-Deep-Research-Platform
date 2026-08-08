from typing import TypedDict
from app.agents.planner import PlannerOutput


class ResearchState(TypedDict):
    query: str
    plan: PlannerOutput
    web_results: list
    paper_results: list
    docs_results: list
    merged_context: str
    final_result: str
    approved: bool
    feedback: str
    score: int
    strengths: list[str]
    weaknesses: list[str]
    missing_topics: list[str]
    revision_count: int
    
    memory_context: str
    memory_hit: bool

    sources: list
    
    evaluation: dict
    usage: list

    