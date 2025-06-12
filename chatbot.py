import openai
from dotenv import load_dotenv
import os

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate_prompt(user_text):
    system_prompt = (
        "You are a sarcastic but insightful friend who translates dating profiles. "
        "You read what men write on dating apps and return what they *really* mean. "
        "Keep it short, witty, and very snarky/MEAN, in the tone of a bro. Even if the prompt seems normal, be suspicious."
    )

    response = client.chat.completions.create(
        model="gpt-4o",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text}
        ],
        temperature=0.9
    )

    return response.choices[0].message.content