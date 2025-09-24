from AGENTS.graph import run_graph

def orchestrator(user_message: str) -> str:
    """
    Dummy as of now to connect the message to the LangGraph
    """

    try:
        response = run_graph(user_message)
        return response
    
    except Exception as e:
        return f"[Orchestration Error] error is as follows: {e}"

