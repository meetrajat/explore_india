from fastapi import FastAPI, Query
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from india.monuments.monument_tool import get_monument_fact
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
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7, api_key=os.getenv("OPENAI_API_KEY"))
    tools = [get_monument_fact]
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    result = agent.run(request.query)
    return {"result": result}