from langchain_text_splitters import split_text_on_tokens
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.core.config import settings


def chunk_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size = settings.CHUNK_SIZE,
        chunk_overlap = settings.CHUNK_OVERLAP,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    chunks = splitter.split_documents(documents)

    for index, chunk in chunks:
        chunk.metadata['chunk_id'] = str(index)

    return chunks
    