from fastapi import APIRouter
from MEMORY.memory_manager import clear_memory

router = APIRouter()


@router.post("/")
async def clear():
    """
    Index provided text chunks into the vector database.
    """
    return clear_memory()
