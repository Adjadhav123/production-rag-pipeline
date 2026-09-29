from rank_bm25  import BM25Okapi

class BM25Retriever:

    def __init__(self, documents):

        self.documents = documents


        tokenized_documents = [
            doc.page_content().lower().split()
            for doc in documents
        ]


        self.bm25 = BM25Okapi(
            tokenized_documents
        )


    def search(
        self,
        query: str,
        k: int = 10,
    ):

        tokens = query.lower().split()

        results = self.bm25.get_top_n(
            tokens,
            self.documents,
            n=k
        )

        return results

