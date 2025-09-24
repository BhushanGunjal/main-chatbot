# API/routes/upload.py

from fastapi import APIRouter, File, UploadFile
from API.models.upload_models import UploadResponse
import os

router = APIRouter()

@router.post("/", response_model=UploadResponse)
async def upload_file(file: UploadFile = File(...)):
    """
    Accepts a file upload and returns basic info.
    Later we'll process it into embeddings for ChromaDB.
    """
    contents = await file.read()
    size_kb = round(len(contents) / 1024,2)

    return UploadResponse(
        filename=file.filename,
        content_type=file.content_type,
        size_kb=size_kb
    )