import hashlib
from pathlib import Path 

from app.ingestion.chunker import chunk_documents
from app.ingestion.loaders import load_documets
from app.core.config import settings
from app.retrieval.vector_store import get_vector_store

def calculate_file_hash(file_path: str):

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        while chunk:= f.read(1024 * 1024):
            sha256.update(chunk)

    return sha256.hexdigest()

def ingest_documents(file_path: str):

    path = Path(file_path)

    print(f'Loading documents {path.name}')

    documents = load_documets(
        str(path)
    )

    print(f"Loaded {len(documents)} documents pages")

    file_hash = calculate_file_hash(
        str(path)
    )

    for document in documents:
        document.metadata['document_id'] = file_hash
        document.metadata['version'] = "1"
        document.metadata['is_active'] = True


    chunks = chunk_documents(documents)

    print(f"Chunked into {len(chunks)} chunks")

    vector_store = get_vector_store()

    vector_store.add_documents(chunks)

    print(f"Sucessfully indexed: {path.name}")


    return {
        "document_id": file_hash,
        "file_name": path.name,
        "chunks": len(chunks)
    }