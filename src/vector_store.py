from sentence_transformers import SentenceTransformer, util

class VectorStoreManager:
    def __init__(self):
        # Initialize the sentence-transformers model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.document_embeddings = []
        self.documents = []

    def add_documents(self, documents):
        """
        Adds documents to the vector store by encoding them with SentenceTransformers.
        """
        self.documents.extend(documents)
        doc_embeddings = self.model.encode(documents, convert_to_tensor=True)
        self.document_embeddings.extend(doc_embeddings)

    def search(self, query, top_k=3):
        """
        Searches for the most relevant documents in the vector store based on the query.
        """
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        similarities = util.pytorch_cos_sim(query_embedding, self.document_embeddings)
        
        # Sort and retrieve the most similar documents
        top_results = similarities.topk(top_k)
        top_docs = [self.documents[i] for i in top_results.indices]
        return top_docs
