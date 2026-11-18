from tools.groq_client import ask_groq

def finance_agent(
        business,
        budget
):

    prompt = f"""
    Business:

    {business}

    Budget:

    {budget}

    Create:

    Startup Cost
    Revenue Forecast
    Break Even Analysis
    """

    return ask_groq(prompt)