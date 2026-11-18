
import os
import time
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing. Check your .env file.")

client = Groq(api_key=api_key)


def ask_groq(prompt, max_tokens=1000):

    for attempt in range(4):
        try:
            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=max_tokens
            )

            return response.choices[0].message.content

        except Exception as e:

            status_code = getattr(e, "status_code", None)

            if status_code == 429 and attempt < 3:
                wait_time = 2 ** (attempt + 1)

                print(
                    f"Groq rate limit reached. "
                    f"Retrying in {wait_time} seconds..."
                )

                time.sleep(wait_time)

            else:
                print("Groq Error:", e)
                raise
