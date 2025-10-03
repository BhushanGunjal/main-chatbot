from fastapi import APIRouter
from API.models.index_models import IndexRequest, IndexResponse
from UPLOAD.embeddings import add_to_vector_db

router = APIRouter()


@router.post("/", response_model=IndexResponse)
async def index_chunks(request: IndexRequest):
    """
    Index provided text chunks into the vector database.
    """
    indexed_count = 0
    for chunk in request.chunks:

        add_to_vector_db(
            doc_id = chunk.id,
            content = chunk.text,
            metadata = chunk.metadata
        )
        indexed_count += 1

    return IndexResponse(
        status = "indexed",
        indexed_chunks = indexed_count
    )