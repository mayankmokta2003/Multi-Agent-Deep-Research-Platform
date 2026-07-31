from app.graph.builder import graph

def run_graph(query: str):
    result = graph.invoke({
        "query": query,
        "revision_count": 0,
    })
    return result

