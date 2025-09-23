# API/routes/upload.py

from fastapi import APIRouter, File, UploadFile
import shutil
import os

router = APIRouter()

# Directory where files will be saved
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload a file and save it to the server.
    """
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save file to disk
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "status": "uploaded successfully"}
