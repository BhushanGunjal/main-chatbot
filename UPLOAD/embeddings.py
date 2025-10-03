import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer


# Initialize Chroma client
chroma_client = chromadb.PersistentClient(path="./DB/chroma")
collection = chroma_client.get_or_create_collection("chatbot_docs")

# Initialize the HuggingFace embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

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

    collection.add(
        ids=[doc_id],
        documents=[content],
        metadatas=[metadata or {}],
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
