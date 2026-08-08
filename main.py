from app.graph.builder import graph


response = graph.invoke({
    "query": "How were the himalayas made",
    "revision_count": 0
})


# print(response)
print("------------ PAPER RESULTS ---------------")
# print(response["paper_results"])

print("------------ WEB RESULTS ---------------")
print(response["final_result"])
# print("balabaljajjsjjs",response["revision_count"])
print("MEMORY_____________1111111_______________", response["memory_hit"])

print("---------------- EVALUATION OF SYSTEM ----------------",response["evaluation"])