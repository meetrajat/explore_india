from fastapi import FastAPI, Query
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from india.monuments.monument_tool import get_monument_fact
from india.food.food_tool import get_nutrition_tool
from dotenv import load_dotenv
import os

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/ask")
def ask_fact(request: QueryRequest):
    """
    API endpoint that takes a string input, initializes LLM, and uses LangChain agent to call the appropriate tool.
    """
    load_dotenv()  # Load environment variables from .env file
    # By default ChatOpenAI() uses GPT-3.5-turbo model
    # You can change the model by specifying the model parameter
    #llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7, api_key=os.getenv("OPENAI_API_KEY"))
    llm = getLLM()
    tools = select_tools(request.query)
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    result = agent.run(request.query)
    return {"result": result}

def select_tools(query: str):
    """
    Selects tools based on the query type.
    Args:
        query (str): The user query to classify.
    Returns:
        list: List of tools to be used.
    """
    input_query = query.lower()
    tools = []
    if any(word in input_query for word in ["nutrition", "calorie", "protein", "fat", "carb", "food"]):
        tools.append(get_nutrition_tool)
    if any(word in input_query for word in ["monument", "statue", "building", "heritage", "site"]):
        tools.append[get_nutrition_tool]
    if any(word in query for word in ["history", "event", "year"]):
        tools.append[get_monument_fact]
    else:
        tools = [get_monument_fact,get_nutrition_tool]  # No tools available for this query type
    return tools    

def llm_intent_detection(query: str):
    prompt = ("Classify the following query as one of: food, monument, history, or unknown.\n"
        "Query: \"" + query + "\"\n"
        "Intent:")
    llm = getLLM();
    response = llm([{"role": "user", "content": prompt}])
    intent = response.content.strip().lower()
    return intent

def getLLM():
    """
    Initializes and returns the LLM instance.
    Returns:
        ChatOpenAI: The initialized LLM instance.
    """
    return ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7, api_key=os.getenv("OPENAI_API_KEY"))