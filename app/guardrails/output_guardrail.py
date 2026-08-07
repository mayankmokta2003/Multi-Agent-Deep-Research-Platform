from app.state.research_state import ResearchState
from fastapi import HTTPException


def output_guardrail(report: str):
    if len(report.strip()) > 200:
        raise HTTPException(
            status_code=500,
            detail="Generated report is too short."
        )
    return {}




# def output_guardrail(report: str):

#     if len(report.split()) < 300:
#         raise HTTPException(
#             status_code=500,
#             detail="Generated report is too short."
#         )

#     if "#" not in report:
#         raise HTTPException(
#             status_code=500,
#             detail="Report is not properly formatted."
#         )

#     if "Reference" not in report and "References" not in report:
#         raise HTTPException(
#             status_code=500,
#             detail="References section missing."
#         )