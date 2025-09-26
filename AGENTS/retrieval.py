from UPLOAD.embeddings import query_vector_db

def retrieval_agent(user_message: str) -> str:
    """
    Retrieval agent
    """
    results = query_vector_db(user_message, n_results=2)
    if results and results.get("documents"):
        docs = results["documents"][0]
        return f"[Retrieval Agent] Found documents: {docs}"
    else:
        return f"[Retrieval Agent] No relevant info found."
    