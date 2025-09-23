# API/routes/chat.py

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Request body model
class ChatRequest(BaseModel):
    message: str

# Response model (optional, helps with docs)
class ChatResponse(BaseModel):
    reply: str

@router.post("/send", response_model=ChatResponse)
def send_message(request: ChatRequest):
    """
    Endpoint to handle chat messages.
    Right now it just echoes back the user's message.
    Later you can connect this to LangGraph or an LLM.
    """
    user_message = request.message
    return {"reply": f"You said: {user_message}"}
