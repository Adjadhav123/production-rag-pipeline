from  app.core.config import settings
from app.retrieval.vector_store import get_vector_store


def get_retriever():

    vector_store = get_vector_store()

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": settings.RETRIEVAL_TOP_K
        }
    )

    return retriever
    