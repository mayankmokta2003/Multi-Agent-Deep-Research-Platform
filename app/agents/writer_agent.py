from langchain_core.prompts import ChatPromptTemplate
from app.llms.mistral import get_llm
from app.state.research_state import ResearchState


writer_prompt = ChatPromptTemplate.from_messages(
[
(
"system",
"""
You are an expert AI Research Writer.
Answer the user's query.
Use all evidence.
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


def writer_agent(state: ResearchState):
    llm = get_llm()
    chain = writer_prompt | llm
    response = chain.invoke({
        "query": state["query"],
        "context": state["merged_context"],
        "feedback": state["feedback"]
    })
    return{"final_result": response.content}
