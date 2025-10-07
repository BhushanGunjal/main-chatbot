from fastapi import APIRouter
from API.models.index_models import IndexRequest, IndexResponse
from UPLOAD.indexer import index_chunks_list

router = APIRouter()


@router.post("/", response_model=IndexResponse)
async def index_chunks(request: IndexRequest):
    """
    Index provided text chunks into the vector database.
    """
    return index_chunks_list(request.chunks)
