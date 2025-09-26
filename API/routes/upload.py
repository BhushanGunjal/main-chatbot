from fastapi import APIRouter, File, UploadFile
from API.models.upload_models import UploadResponse
from UPLOAD.processor import save_file, extract_text
from UPLOAD.embeddings import add_to_vector_db

router = APIRouter()

@router.post("/", response_model=UploadResponse)
async def upload_file(file: UploadFile = File(...)):
    """
    Save uploaded file, extract text, and add to vector DB.
    Returns metadata + indexing status.
    """
    # Read file to get size
    contents = await file.read()
    size_kb = round(len(contents) / 1024, 2)

    # Reset file pointer for saving
    file.file.seek(0)

    # 1. Save file locally
    file_path = save_file(file)

    # 2. Extract text (for now: txt only)
    content = extract_text(file_path)

    # 3. Store in vector DB
    add_to_vector_db(doc_id=file.filename, content=content, metadata={"path": file_path})

    return UploadResponse(
        filename=file.filename,
        content_type=file.content_type,
        size_kb=size_kb,
        status="uploaded & indexed"
    )
