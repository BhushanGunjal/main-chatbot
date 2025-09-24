
from AGENTS.planner import planner_logic
from AGENTS.reasoning import reasoning_agent
from AGENTS.retrieval import retrieval_agent
from AGENTS.summarizer import summary_agent


def run_graph(user_message:str) -> str:
    """
    Orchestrates flow of the chatbot:
    1. Planner decides which path to take.
    2. Calls the corresponding agent.
    3. Returns the agent's response.
    """
    decision = planner_logic(user_message)

    if decision == "retrieval":
        response = retrieval_agent(user_message)
    elif decision == "reasoning":
        response = reasoning_agent(user_message)
    else:
        response = summary_agent(user_message)
    return response
