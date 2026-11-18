from tools.groq_client import ask_groq

def branding_agent(business):

    prompt = f"""
    Create branding for:

    {business}

    Generate:

    Startup Name
    Tagline
    Mission
    Logo Description
    """

    return ask_groq(prompt)