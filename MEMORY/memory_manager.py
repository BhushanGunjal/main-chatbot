import chromadb
from datetime import datetime
from UPLOAD.embeddings import embed_text

chroma_client = chromadb.PersistentClient(path="./DB/chroma")
memory_collection = chroma_client.get_or_create_collection(name="chat_memory")

def store_memory(role: str, content: str):
    """
    Stores a user or assistant message in vector memory.
    """
    try:
        message_id = f"{role}_{datetime.now().timestamp()}"
        embedding = embed_text(content)
        metadata = {
            "role": role,
            "timestamp": datetime.now().isoformat()
        }

        memory_collection.add(
            ids=[message_id],
            documents=[content],
            embeddings=[embedding],
            metadatas=[metadata]
        )
        print(f"Stored message from {role}: {content[:60]}...")
        print(memory_collection)
    
    except Exception as e:
        print(f"[Memory Error] Failed to store message: {e}")


def retrieve_relevant_memories(query: str, n_results: int = 3) -> list[str]:
    """
    Retrieves relevant memories based on a query.
    """
    try:
        query_embedding = embed_text(query)
        results = memory_collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )

        if not results or "documents" not in results or not results["documents"]:
            return []
        
        retrieved_texts = results["documents"][0]
        return retrieved_texts
    
    except Exception as e:
        print(f"[Memory Error] Failed to retrieve memories: {e}")
        return []
    

def clear_memory():
    """
    Clears all stored memories.
    """
    try:
        print("Before Clearing: ",memory_collection.count())
        memory_collection.clear()
        print("Cleared all memories.")
        return "MEMORY CLEARED"
    
    except Exception as e:
        print(f"[Memory Error] Failed to clear memories: {e}")