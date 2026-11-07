
import os
import requests
from dotenv import load_dotenv
from tavily import TavilyClient
from langchain.tools import tool
from bs4 import BeautifulSoup

load_dotenv()

tavily = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


@tool
def web_search(query: str) -> str:
    """Search the web for recent information."""
    result = tavily.search(query=query, max_results=5)
    search_results = []

    for i in result["results"]:
        data = (
            f"Title: {i['title']}\n"
            f"URL: {i['url']}\n"
            f"Snippet: {i['content'][:100]}"
        )
        search_results.append(data)

    return "\n\n".join(search_results)


@tool
def scrap_url(url: str) -> str:
    """Scrape a webpage and return clean text for deep reading."""
    try:
        response = requests.get(
            url,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()

        title = soup.title.get_text(strip=True) if soup.title else "No title"
        content = soup.get_text(separator=" ", strip=True)

        return f"Title: {title}\n\nContent:\n{content[:1000]}"

    except Exception as e:
        return f"Error: {e}"
