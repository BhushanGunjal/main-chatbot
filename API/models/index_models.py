
from pydantic import BaseModel
from API.models.upload_models import Chunk   # reuse existing Chunk model

class IndexRequest(BaseModel):
    filename: str          # identify file
    chunks: list[Chunk]    # list of chunks from upload step

class IndexResponse(BaseModel):
    status: str
    indexed_chunks: int