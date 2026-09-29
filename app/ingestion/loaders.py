from pathlib import Path
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader
)

def load_documets(file_path: str):
    path = Path(file_path)

    extention = path.suffix.lower()

    if extention == ".pdf":
        loader = PyPDFLoader(file_path)
    elif extention == ".txt":
        loader = TextLoader(file_path)
    elif extention == ".docx":
        loader = Docx2txtLoader(file_path)
    else:
        raise ValueError(f"Unsupported file type: {extention}")


    documents = loader.load()

    for document in documents:
        document.metadata['source'] = path.name
        document.metadata['file_path'] = str(path)

    return documents