from app.config.settings import get_settings
from tavily import TavilyClient

settings = get_settings()

client = TavilyClient(api_key=settings.TAVILY_API_KEY)

def search_web(query: str, max_results: int = 5):
    response = client.search(query=query, max_results=max_results)
    return response["results"]
