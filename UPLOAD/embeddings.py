import chromadb
from chromadb.config import Settings

# Initialize Chroma client
chroma_client = chromadb.PersistentClient(path="./DB/chroma")

collection = chroma_client.get_or_create_collection("chatbot_docs")

def add_to_vector_db(doc_id: str, content: str, metadata: dict = None):

    existing = collection.get()
    if existing and "ids" in existing:
        collection.delete(ids=existing["ids"])

    collection.add(
        ids=[doc_id],
        documents=[content],
        metadatas=[metadata or {}]
    )

def query_vector_db(query: str, n_results: int = 2):
    return collection.query(query_texts=[query], n_results=n_results)
