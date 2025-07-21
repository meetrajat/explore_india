from langchain.tools import tool
from india.food.food_api import get_nutrition_info

@tool("get_nutrition_info", description="Get nutritional information for a food item using the Spoonacular API.")
def get_nutrition_tool(food_name: str) -> dict:
    """
    Get nutritional information for a food item using the Spoonacular API.
    Args:
        food_name (str): The name of the food item to look up.
    Returns:
        dict: Nutritional information or an error message.
    """
    return get_nutrition_info(food_name)