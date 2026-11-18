

from tools.groq_client import ask_groq

def swot_agent(
        business,
        market,
        competitor
):

    prompt = f"""
    Business:
    {business}

    Market:
    {market}

    Competitor Analysis:
    {competitor}

    Generate a SWOT Analysis.

    Give:

    Strengths
    Weaknesses
    Opportunities
    Threats

    Maximum 150 words.
    """

    return ask_groq(prompt)