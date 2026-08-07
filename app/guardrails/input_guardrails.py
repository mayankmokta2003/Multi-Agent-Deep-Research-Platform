from app.state.research_state import ResearchState


# BLOCKED_WORDS = [
#     "ignore previous",
#     "ignore all previous",
#     "system prompt",
#     "developer message",
#     "reveal prompt",
#     "bomb",
#     "hack"
# ]

# def input_gaurdrail(state: ResearchState):
#     for word in BLOCKED_WORDS:
#         if word in state["query"]:
#             raise ValueError("Prompt Injection Detected.")
#     return {}




from app.guardrails.prompt_injection import prompt_injection_guardrail
from app.guardrails.topic_gaurdrail import topic_guardrail

def input_guardrail(state: ResearchState):

    query = state["query"]

    prompt_injection_guardrail(query)
    topic_guardrail(query)

    return state