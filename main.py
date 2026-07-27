from app.graph.builder import graph
from app.state.research_state import ResearchState

response = graph.invoke({
    "query": "Latest AI Agent Memory Techniques"
})

print(response)

