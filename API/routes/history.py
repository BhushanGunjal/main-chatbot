# API/routes/history.py

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

# In-memory storage (resets when server restarts)
chat_history: List[dict] = []

class Message(BaseModel):
    sender: str   # e.g., "user" or "bot"
    text: str

@router.post("/add")
def add_message(message: Message):
    """
    Add a chat message to history.
    """
    chat_history.append(message.dict())
    return {"status": "message added", "message": message}

@router.get("/all")
def get_history():
    """
    Get the entire chat history.
    """
    return {"history": chat_history}

@router.delete("/clear")
def clear_history():
    """
    Clear the chat history.
    """
    chat_history.clear()
    return {"status": "history cleared"}
