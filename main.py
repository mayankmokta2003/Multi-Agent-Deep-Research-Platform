from app.graph.builder import graph


response = graph.invoke({
    "query": "Latest AI Agent Memory Techniques in 2026",
    "revision_count": 0
})


# print(response)
print("------------ PAPER RESULTS ---------------")
# print(response["paper_results"])

print("------------ WEB RESULTS ---------------")
print(response["final_result"])
print("balabaljajjsjjs",response["revision_count"])
print("MEMORY____________________________", response["memory_hit"])