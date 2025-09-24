# API/routes/chat.py

from fastapi import APIRouter
from API.models.chat_models import ChatRequest, ChatResponse
from AGENTS.orchestrator import orchestrator

router = APIRouter()


@router.post("/send", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Endpoint to handle chat messages.
    Right now it just echoes back the user's message.
    Later you can connect this to LangGraph or an LLM.
    """
    user_message = request.message
    reply = orchestrator(user_message)
    return ChatResponse(reply=reply)
