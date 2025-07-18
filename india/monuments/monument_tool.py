from langchain.tools import tool
from india.monuments.monument_api import get_wikipedia_fact

@tool("get_monument_fact", description="Get a fact about a monument from Wikipedia using the REST API.")
def get_monument_fact(query: str) -> str:
    """
    Get a fact about a monument using Wikipedia REST API.
    Args:
        query (str): The search term to look up on Wikipedia.
    Returns:
        str: A summary fact about the monument, or an error message if not found.
    """
    return get_wikipedia_fact(query)