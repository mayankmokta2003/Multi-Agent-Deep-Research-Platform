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


# def save_memory(query: str, report: str):
#     vectorstore.add_texts(
#         texts = [report],
#         metadata={
#             "query": query
#         }
#     )


def save_memory(query: str, report: str):
    vectorstore.add_texts(
        texts=[query],
        metadatas=[{
            "report": report
        }]
    )