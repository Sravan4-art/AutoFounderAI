from tools.groq_client import ask_groq

def investor_agent(
        market,
        finance,
        strategy
):

    prompt = f"""
        You are a venture capitalist.

        Review:

        {market}

        {finance}

        {strategy}

        Should you invest?

        Give:

        Investment Amount
        Risk Level
        Return Potential
        Decision

        Maximum 100 words.
        Be concise.
        """

    return ask_groq(prompt)