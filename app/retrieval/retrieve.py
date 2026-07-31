from langchain_chroma import Chroma
from langchain_mistralai import MistralAIEmbeddings
from app.config.settings import get_settings

settings = get_settings()

embeddings = MistralAIEmbeddings(api_key=settings.MISTRAL_API_KEY)


def retrieve(query: str):
    vectorstore = Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )
    docs = vectorstore.similarity_search(query=query, k=5)
    print("Found:", len(docs))
    return docs
