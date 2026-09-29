from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient


from app.core.config import settings
from app.services.embedding import get_embedding

def get_qdrant_client():
    return QdrantClient(
        url=settings.QDRANT_URL
    )

def get_vector_store():
    client = get_qdrant_client()

    embeddings = get_embedding()

    vector_store = QdrantVectorStore(
        client=client,
        collection_name=settings.QDRANT_COLLECTION,
        embedding=embeddings
    )


    return vector_store
    