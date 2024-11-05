import httpx
from src.config import Config

def perform_web_search(query):
    """
    Perform a web search using a custom search API (like Bing or Google Custom Search).
    Note: This function requires an API key from the chosen provider.
    """
    url = "https://api.bing.microsoft.com/v7.0/search"
    headers = {"Ocp-Apim-Subscription-Key": Config.WEB_SEARCH_API_KEY}
    params = {"q": query, "textDecorations": True, "textFormat": "HTML"}

    try:
        response = httpx.get(url, headers=headers, params=params)
        response.raise_for_status()
        results = response.json()["webPages"]["value"]
        return [result["snippet"] for result in results]
    except Exception as e:
        print(f"Web search failed: {e}")
        return []
