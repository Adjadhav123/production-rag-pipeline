from langchain_chroma import Chroma
from app.core.config import settings
from app.services.embedding import get_embedding

def get_vector_store():
    embeddings = get_embedding()
    vector_store = Chroma(
        collection_name=settings.VECTOR_COLLECTION,
        embedding_function=embeddings,
        persist_directory=settings.CHROMA_PERSIST_DIRECTORY
    )
    return vector_store
    