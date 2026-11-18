from tools.groq_client import ask_groq

def marketing_agent(business):

    prompt = f"""
    Create marketing plan for:

    {business}

    Generate:

    Instagram Posts
    Facebook Ads
    Launch Campaign
    """

    return ask_groq(prompt)