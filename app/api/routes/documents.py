from pathlib import Path 
from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
)

from app.ingestion.pipeline import ingest_documents


router = APIRouter(
    prefix="/api/v1/documents",
    tags=["documents"]
)

UPLOAD_DIR = Path(
    "/data/documents"
)


UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)

@router.post("/")
async def upload_document(
    file: UploadFile = File(...)
): 

    allowed_extentions = {
        ".pdf",
        ".txt",
        ".docx"
    }

    extension = Path(
        file.filename
    ).suffix.lower()

    if extension not in allowed_extentions:
        raise HTTPException(
            status_code=400,
            detail = "Unsupported file type"
        )

    destination = (
        UPLOAD_DIR / file.filename
    )

    contents = await file.read()

    with open(
        destination,
        "wb"
    ) as output:
        output.write(contents)

    result = ingest_documents(
        str(destination)
    )


    return result
