from typing import List 

from langchain_core.documents import Document

class SimpleReranker:

    def rerank(
        self,
        query: str,
        documents: List[Document],
        top_k: int = 5,
    ):

        query_words = set(query.lower().split())

        scored_docs = []
        
        for document in documents:

            text_words = set(
                document.page_content.lower().split()
            )

            overlap = query_words.intersection(
                text_words
            )

            scored_docs.append(
                (overlap, document)
            )

        scored_docs.sort(
            key=lambda x: x[0],
            reverse=True
        )

        return [
            doc for score, doc in scored_docs[:top_k]
        ]