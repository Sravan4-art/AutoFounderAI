from tools.groq_client import ask_groq

def business_plan_agent(
        market,
        finance,
        strategy
):

    prompt = f"""
    Create a professional startup business plan.

    Market:
    {market}

    Finance:
    {finance}

    Strategy:
    {strategy}

    Include:

    1. Executive Summary
    2. Business Description
    3. Market Analysis
    4. Revenue Model
    5. Marketing Plan
    6. Financial Plan
    7. Growth Strategy

    Maximum 500 words.
    """

    return ask_groq(prompt)