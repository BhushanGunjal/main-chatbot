# API/routes/history.py

from fastapi import APIRouter
from API.models.chat_models import ChatResponse

router = APIRouter()

dummy_history = [
    {"reply": "Test Message 1"},
    {"reply": "Test Message 2"},
    {"reply": "Test Message 3"},
]


@router.get("/", response_model=list[ChatResponse])
async def get_history():
    """
    Returns dummy chat history.
    """
    # added temp for debugging
    print("Chat history fetched")
    # done 
    return [ChatResponse(**msg) for msg in dummy_history]
