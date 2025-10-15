from AGENTS.graph import run_graph
from MEMORY.memory_manager import retrieve_relevant_memories, store_memory

def orchestrator(user_message: str) -> str:
    """
    Orchestrates chat workflow with memory integration.
    Steps:
    1. Retrieve relevant past messages from vector memory.
    2. Provide memory context to the graph for better reasoning.
    3. Store both user and assistant messages back into memory.
    """

    try:
        # 1️⃣ Retrieve memory context
        memory_contexts = retrieve_relevant_memories(user_message)
        context_text = "\n\n".join(memory_contexts)

        # 2️⃣ Run your normal workflow (pass context if needed)
        full_input = f"Previous context:\n{context_text}\n\nUser: {user_message}"
        response = run_graph(full_input)

        # 3️⃣ Store both sides of the conversation
        store_memory("user", user_message)
        store_memory("assistant", response)

        print({"user": user_message, "memory": memory_contexts, "response": response})
        
        return response

    
    except Exception as e:
        return f"[Orchestration Error] error is as follows: {e}"

