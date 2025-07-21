import requests
from india.common.utilityClass import UtilityClass
import os
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class FoodRequest(BaseModel):
    food_name: str

def get_nutrition_info(food_name):
    """
    Fetch nutritional information for a given food using the Spoonacular API.
    Args:
        food_name (str): The name of the food item to look up.
    Returns:
        dict: Nutritional information or an error message.
    """
    api_key = os.getenv("SPOONACULAR_KEY")
    if not api_key:
        return {"error": "Spoonacular API key not set in environment."}
    url = f"https://api.spoonacular.com/recipes/guessNutrition?title={food_name}&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"No information found for '{food_name}'.", "status_code": response.status_code}

@app.post("/nutrition")
def nutrition_info(request: FoodRequest):
    """
    API endpoint to get nutritional information for a food item using the Spoonacular API.
    """
    result = get_nutrition_info(request.food_name)
    return result