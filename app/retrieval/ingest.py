from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_mistralai import MistralAIEmbeddings
from langchain_chroma import Chroma
from app.config.settings import get_settings


settings = get_settings()

embeddings = MistralAIEmbeddings(api_key=settings.MISTRAL_API_KEY)


def ingest_pdf(path: str):
    loader = PyPDFLoader(path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200
    )
    chunks = splitter.split_documents(docs)
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="db"
    )
    return vectorstore
