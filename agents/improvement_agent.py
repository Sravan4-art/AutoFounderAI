from tools.groq_client import ask_groq

def improvement_agent(
        ceo_review,
        investor_review
):

    prompt = f"""
CEO Review:

{ceo_review}

Investor Review:

{investor_review}

Suggest improvements.

Maximum 100 words.
"""

    return ask_groq(prompt)