from tools.groq_client import ask_groq

def ceo_agent(
        market,
        branding,
        finance,
        marketing,
        strategy
):

    prompt = f"""
        You are the CEO.

        Review:

        {market}

        {branding}

        {finance}

        {marketing}

        Decide:

        Should we launch?

        Why?

        Maximum 100 words.
        Be concise.
        """

    return ask_groq(prompt)