from app.graph.builder import graph


response = graph.invoke({
    "query": "Latest AI Agent Memory Techniques"
})


print(response)
# print(response["paper_results"])

