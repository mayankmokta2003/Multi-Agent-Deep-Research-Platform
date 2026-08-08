from langchain_chroma import Chroma
from langchain_mistralai import MistralAIEmbeddings
from app.config.settings import get_settings

settings = get_settings()

embeddings = MistralAIEmbeddings(api_key=settings.MISTRAL_API_KEY)
vectorstore = Chroma(
    persist_directory="db",
    embedding_function=embeddings
)


def retrieve(query: str):
    docs = vectorstore.similarity_search_with_relevance_scores(query=query, k=5)
    filtered_docs = []
    for doc, score in docs:
        # print(f"Score: {score:.3f}")
        if score > 0.5:
            filtered_docs.append(doc)
    # print(f"Retrieved: {len(docs)} | Filtered: {len(filtered_docs)}")        
    return filtered_docs
