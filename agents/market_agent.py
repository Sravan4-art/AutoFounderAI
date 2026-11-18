from tools.search_tool import search_web
from tools.groq_client import ask_groq

def market_agent(business):

    competitors = search_web(
        f"{business} competitors"
    )

    prompt = f"""
    Business:

    {business}

    Competitors:

    {competitors}

    Analyze market.
    """

    return ask_groq(prompt)