from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
from ai_agent import get_response_from_agent
import uvicorn

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    messages: List[str]
    allow_search: bool

app = FastAPI(title="LangGraph Fashion Agent API")

ALLOWED_MODEL_NAMES = ["llama3-70b-8192", "llama-3.3-70b-versatile", "gpt-4o-mini", "mixtral-8x7b-32768"]

@app.post("/chat")
def endpoint(request: RequestState):
    """
    Endpoint to handle chat requests using Langgraph and search tools.
    It dynamically selects model and provider based on the request.
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Model not supported"}
    
    response = get_response_from_agent(
        llm_id=request.model_name,
        query=request.messages,
        allow_search=request.allow_search,
        provider=request.model_provider
    )
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9999)

    