from langchain_groq import ChatGroq

from app.core.config import settings

def get_llm():
    return ChatGroq(
        model = settings.LLM_MODEL,
        temperature = settings.TEMPERATURE,
        groq_api_key = settings.GROQ_API_KEY
    )