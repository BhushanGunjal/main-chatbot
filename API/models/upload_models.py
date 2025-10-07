from pydantic import BaseModel

class Chunk(BaseModel):
    id: str
    text: str
    metadata: dict

class UploadResponse(BaseModel):
    filename: str
    content_type: str
    size_kb: float
    status: str
    chunks: list[Chunk]
    index_status: str
    index_counts: int


