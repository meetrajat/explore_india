import requests
from india.common.utilityClass import UtilityClass

def get_wikipedia_fact(query):
    """
    Fetch a summary fact about the query from Wikipedia REST API.
    Args:
        query (str): The search term to look up on Wikipedia.
    Returns:
        str: A summary fact about the query, or an error message if not found.
    """
    url = UtilityClass.get_wikipedia_baseurl() + query
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Fact for {query}: {data}")
        return data.get('extract', 'No summary available.')
    else:
        return f"No information found for '{query}'."
