from langchain_community.tools.tavily_search import TavilySearchResults

web_search_tool = TavilySearchResults(k=3)

def perform_web_search(query):
    results = web_search_tool.invoke({"query": query})
    return results
