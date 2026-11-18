from tools.groq_client import ask_groq

def strategy_agent(
        market,
        finance,
        marketing
):

    prompt = f"""
        Market:

        {market}

        Finance:

        {finance}

        Marketing:

        {marketing}

        Create a 12 month growth strategy.

        Maximum 100 words.
        Be concise.
        """

    return ask_groq(prompt)