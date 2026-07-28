from langchain_mistralai import ChatMistralAI
from functools import lru_cache
from app.config.settings import get_settings


@lru_cache
def get_llm():
    setting = get_settings()
    return ChatMistralAI(
        model = setting.model_name,
        temperature=setting.temperature,
        api_key = setting.MISTRAL_API_KEY
    )



