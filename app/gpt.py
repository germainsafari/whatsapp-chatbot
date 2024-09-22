import openai
import os


openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(question):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message["content"].strip()
