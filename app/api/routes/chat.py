from fastapi import APIRouter
from app.models.schemas import (
    ChatRequest,
    ChatResponse
)

from app.rag.service import RAGService

router = APIRouter(
    prefix="/api/v1",
    tags=["chat"]
)

rag_service = RAGService()

@router.post(
    "/chat",
    response_model=ChatResponse
)

async def chat(
    request: ChatRequest
):

    result = await rag_service.ask(
        request.question
    )

    return result