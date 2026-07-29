from langchain_chroma import Chroma
from langchain_mistralai import MistralAIEmbeddings
from app.config.settings import get_settings

settings = get_settings()


embeddings = MistralAIEmbeddings(
    api_key=settings.MISTRAL_API_KEY
)

vectorstore = Chroma(
    collection_name="research_memory",
    embedding_function=embeddings,
    persist_directory="memory_db"
)

THRESHOLD = 0.85


def retrieve_memory(query: str):
    results = vectorstore._similarity_search_with_relevance_scores(query=query, k=1)
    if not results:
        return None
    doc, score = results[0]
    if score < THRESHOLD:
        return None
    return doc


