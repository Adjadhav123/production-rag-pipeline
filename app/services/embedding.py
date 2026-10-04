from langchain_community.embeddings import HuggingFaceEmbeddings
from app.core.config import settings

def get_embedding(model_name: str = None):
    model_name = model_name or settings.EMBEDDING_MODEL
    return HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={"trust_remote_code": True}
    )

