from app.graph.builder import graph

def run_graph(query: str):
    return graph.invoke({
        "query": query,
        "revision_count": 0,
    })

