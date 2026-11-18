from tools.groq_client import ask_groq

def competitor_agent(business):

    prompt = f"""
    Business:

    {business}

    Analyze competitors.

    Give:

    1. Top Competitors
    2. Their Strengths
    3. Their Weaknesses
    4. Market Gaps
    5. How to Beat Them

    Maximum 150 words.
    """

    return ask_groq(prompt)