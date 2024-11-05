import faiss
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document
import os

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

class VectorStoreManager:
    def __init__(self, index_file_path="faiss_index"):
        self.index_file_path = index_file_path
        if os.path.exists(index_file_path):
            self.vector_store = FAISS.load_local(index_file_path, embeddings)
        else:
            self.vector_store = FAISS(embeddings)

    def add_documents(self, documents):
        doc_objs = [Document(content=doc) for doc in documents]
        self.vector_store.add_documents(doc_objs)
        self.vector_store.save_local(self.index_file_path)

    def search(self, query, top_k=3):
        return self.vector_store.similarity_search(query, k=top_k)
