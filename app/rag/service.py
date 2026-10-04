from typing import List

from langchain_core.documents import Document 


from app.core.config import settings
from app.rag.prompt import RAG_PROMPT
from app.retrieval.hybrid import get_retriever
from app.retrieval.reranker import SimpleReranker
from app.services.llm import get_llm


class RAGService:

    def __init__(self):

        self.retriever = get_retriever()

        self.reranker = SimpleReranker()

        self.llm = get_llm()


    def retrieve(
        self,
        query
    )->List[Document]:

        documents = self.retriever.invoke(
            query
        )


        documents = self.reranker.rerank(
            query=query,
            documents=documents,
            top_k=settings.FINAL_TOP_K
        )


        return documents

    def build_context(
        self,
        documents: List[Document]
    ):
        context_parts = []
        for document in documents:
            source = document.metadata.get("source", "unknown")
            page = document.metadata.get("page")
            chunk_id = document.metadata.get("chunk_id")
            context_parts.append(
                f"SOURCE : {source}\nPAGE: {page}\nCHUNK_ID : {chunk_id}\n\nCONTENT:\n{document.page_content}"
            )
        return "\n\n".join(context_parts)

    def build_sources(
        self,
        documents: List[Document]
    ):
        sources = []
        for document in documents:
            sources.append(
                {
                    "document": document.metadata.get("source"),
                    "page": document.metadata.get("page"),
                    "chunk_id": document.metadata.get("chunk_id")
                }
            )
        return sources

    async def ask(
        self,
        question: str
    ):
        documents = self.retrieve(question)

        if not documents:
            return {
                "answer": "I could not find this information in the documents",
                "sources": []
            }

        context = self.build_context(documents)
        messages = RAG_PROMPT.format_messages(
            context=context,
            question=question
        )
        response = self.llm.invoke(messages)

        return {
            "answer": response.content,
            "sources": self.build_sources(documents)
        }