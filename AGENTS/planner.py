def planner_logic(user_message: str) -> str:
    """
    Returns Query Classification based on the Query
    """

    if "doc" in user_message.lower():
        return "retrieval"
    
    elif "why" in user_message.lower():
        return "reasoning"
    
    else:
        return "summary"
    

