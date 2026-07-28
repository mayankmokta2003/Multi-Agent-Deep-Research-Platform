from app.graph.builder import graph


response = graph.invoke({
    "query": "Latest AI Agent Memory Techniques"
})


# print(response)
print("------------ PAPER RESULTS ---------------")
# print(response["paper_results"])

print("------------ WEB RESULTS ---------------")
print(response["final_result"])
