from langchain_core.prompts import ChatPromptTemplate
from app.llms.mistral import get_llm
from app.llms.gateway import call_llm
from app.state.research_state import ResearchState
from app.utils.retry import with_retry


writer_prompt = ChatPromptTemplate.from_messages(
[
(
"system",
"""
You are an expert AI Research Writer.
Use the evidence in the following priority order:
1. Uploaded Documents (Highest Priority)
2. Research Papers
3. Web Results
If the uploaded documents contain information relevant to the user's query,
base the answer primarily on them.
Only use web results to supplement missing information.
Write a professional markdown report.
"""
),
(
"human",
"""
User Query: {query}
Evidence: {context}
Critic Feedback: {feedback}
"""
)
])




# def writer_agent(state: ResearchState):
#     prompt = writer_prompt.format(
#         query = state["query"],
#         context=state["merged_context"],
#         feedback=state.get("feedback", "")
#     )
#     response = call_llm(prompt)
#     return{"final_result": response, "revision_count": state["revision_count"]+1}



def writer_agent(state: ResearchState):
    prompt = writer_prompt.format(
        query = state["query"],
        context=state["merged_context"],
        feedback=state.get("feedback", "")
    )
    response = with_retry(call_llm, prompt)
    return{"final_result": response, "revision_count": state["revision_count"]+1}