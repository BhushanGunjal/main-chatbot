from UPLOAD.embeddings import query_vector_db

def retrieval_agent(user_message: str) -> str:
    """
    Retrieval agent
    """
    results = query_vector_db(user_message, n_results=1)
    
    if (
        not results
        or "documents" not in results
        or not results["documents"]
        or not results["documents"][0]
    ):
            return f"[Retrieval Agent] No relevant info found."
    
    docs = results["documents"][0]
    metadatas = results["metadatas"][0]
    response_lines = []
    for i, (doc, meta) in enumerate(zip(docs,metadatas)):
        line = f"Chunk {i} | Filename: {meta.get('filename', 'unknown')} | Tokens: {meta.get('token_count', 'N/A')}\n{doc}\n"
        response_lines.append(line)
    
    return "[Retrieval Agent] Found documents:\n\n" + "\n\n---\n\n".join(response_lines)
