# UPLOAD/indexer.py
from UPLOAD.embeddings import add_to_vector_db
from API.models.index_models import IndexResponse
from API.models.upload_models import Chunk
from typing import List

def index_chunks_list(chunks: List[Chunk]) -> IndexResponse:
    """
    Index a list of chunks into the vector DB.
    Returns IndexResponse.
    """
    indexed_count = 0
    print("#############################################Chunks retrieved: ", len(chunks))
    for chunk in chunks:
        print("Indexing chunk:", chunk["id"])
        add_to_vector_db(
            doc_id=chunk["id"],
            content=chunk["text"],
            metadata=chunk["metadata"]
        )
        print("#############################################Debug: Metadata for", chunk["id"], "is", chunk["metadata"])
        indexed_count += 1
        print(f"#############################################Indexed {indexed_count} chunks so far.")
    
    return IndexResponse(status="indexed", indexed_chunks=indexed_count)
