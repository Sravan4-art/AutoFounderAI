from tools.groq_client import ask_groq

def startup_score_agent(
        market,
        finance,
        marketing
):

    prompt = f"""
    Evaluate this startup.

    Market:
    {market}

    Finance:
    {finance}

    Marketing:
    {marketing}

    Return ONLY one number between 0 and 100.

    Example:

    78

    Do not explain.
    Do not add text.
    Only return the number.
    """

    return ask_groq(prompt)