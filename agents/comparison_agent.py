from tools.groq_client import ask_groq

def comparison_agent(
        startup1,
        startup2
):

    prompt = f"""
    Compare:

    Startup 1:
    {startup1}

    Startup 2:
    {startup2}

    Give:

    Better Market
    Better Revenue Potential
    Better Investment Opportunity
    Winner
    """

    return ask_groq(prompt)