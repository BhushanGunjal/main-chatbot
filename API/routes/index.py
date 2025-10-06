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
    print("Chunks retrieved: ", len(request.chunks))  # Debugging log
    for chunk in request.chunks:
        print("Indexing chunk:", chunk.id)  # Debugging log
        add_to_vector_db(
            doc_id = chunk.id,
            content = chunk.text,
            metadata = chunk.metadata
        )
        print("Debug: Metadata for", chunk.id, "is", chunk.metadata)  # Debugging log
        indexed_count += 1
        print(f"Indexed {indexed_count} chunks so far.")  # Progress log
    return IndexResponse(
        status = "indexed",
        indexed_chunks = indexed_count
    )