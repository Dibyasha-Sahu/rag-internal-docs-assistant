import os

from dotenv import load_dotenv
from groq import Groq

from app.rag.prompts import build_prompt


load_dotenv()


def generate_answer(query, context):
    prompt = build_prompt(query, context)

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0,
    )

    answer = response.choices[0].message.content

    return {
        "answer": answer,
        "prompt": prompt,
    }