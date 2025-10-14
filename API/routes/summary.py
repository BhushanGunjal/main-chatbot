# API/routes/history.py

from fastapi import APIRouter, UploadFile, File
from UPLOAD.processor import extract_text, save_file
from AGENTS.summarizer import summary_agent

router = APIRouter()


@router.post("/")
async def summarize_file(file: UploadFile = File(...)):
    """
    Summarizes the content of the uploaded file.
    """
    file_path = save_file(file)
    content = extract_text(file_path)
    summary = summary_agent(content)
    return {
        "filename": file.filename,
        "summary": summary
        }

# AGENTS/summarizer.py
# cleared and end