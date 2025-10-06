import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer


# Initialize Chroma client
chroma_client = chromadb.PersistentClient(path="./DB/chroma")
collection = chroma_client.get_or_create_collection("chatbot_docs")

# Initialize the HuggingFace embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def sanitize_metadata(metadata: dict) -> dict:
    """
    Ensure metadata values are ChromaDB-compatible.
    Prints a warning if a non-primitive value is found.
    """
    if not metadata:
        return {}

    import json

    clean_metadata = {}
    for k, v in metadata.items():
        if isinstance(v, (str, int, float, bool)) or v is None:
            clean_metadata[k] = v
        else:
            print(f"[WARN] Non-primitive metadata value for key '{k}': {type(v).__name__} -> serializing to string")
            try:
                clean_metadata[k] = json.dumps(v)
            except Exception as e:
                print(f"[ERROR] Failed to serialize metadata key '{k}': {e}")
                clean_metadata[k] = str(v)  # fallback as string

    return clean_metadata




def embed_text(text: str) -> list[float]:
    """
    Convert text into embedding vector
    """
    return embedding_model.encode(text).tolist()  # convert to list for JSON compatibility

def add_to_vector_db(doc_id: str, content: str, metadata: dict = None):
    """
    Add a chunk with embedding to Chroma
    """
    # Optional: delete previous entries (you may want to remove this in production)
    existing = collection.get(ids=[doc_id])
    if existing and existing["ids"]:
        collection.delete(ids=[doc_id])

    embedding = embed_text(content)
    clean_metadata = sanitize_metadata(metadata)
    collection.add(
        ids=[doc_id],
        documents=[content],
        metadatas=[clean_metadata],
        embeddings=[embedding]  # store embedding for semantic search
    )

def query_vector_db(query: str, n_results: int = 2):
    """
    Perform semantic search using query embeddings
    """
    query_embedding = embed_text(query)
    return collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
