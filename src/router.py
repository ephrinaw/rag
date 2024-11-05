from langchain_nomic import NomicVectorStore
from langchain_community.tools.tavily_search import TavilySearchResults

class DocumentRetriever:
    def __init__(self):
        self.vectorstore = NomicVectorStore("nomic")
        self.web_search_tool = TavilySearchResults(k=3)  # Tavily for web search

    def add_documents(self, documents):
        self.vectorstore.add_documents(documents)

    def retrieve_local(self, question, top_k=5):
        return self.vectorstore.query(question, k=top_k)

    def internet_search(self, question):
        return self.web_search_tool.search(query=question)
