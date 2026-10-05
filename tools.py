import os
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()

def get_market_research_tools():
    """Initializes and returns the search tool using Tavily for market intelligence."""
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    if not tavily_api_key:
        raise ValueError("TAVILY_API_KEY not found in environment variables.")
    
    # Tavily search tool configured to retrieve top relevant web snippets & news
    search_tool = TavilySearchResults(
        max_results=5,
        search_depth="advanced",
        include_answer=True
    )
    search_tool.name = "market_search"
    search_tool.description = "Searches the web for startups, market trends, funding rounds, and industry reports."
    
    return [search_tool]