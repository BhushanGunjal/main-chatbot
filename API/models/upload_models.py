from pydantic import BaseModel

class UploadResponse(BaseModel):
    filename: str
    content_type: str
    size_kb: float
    status: str
    chunks: list[str]
