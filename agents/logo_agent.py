from tools.groq_client import ask_groq

def logo_agent(
        branding
):

    prompt = f"""
    Based on:

    {branding}

    Create a professional logo design prompt
    for an AI image generator.
    """

    return ask_groq(prompt)