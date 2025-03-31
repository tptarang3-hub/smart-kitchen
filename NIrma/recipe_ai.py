import groq
from groq import Client
import db_handler
import os

def get_recipe():
    os.environ["GROQ_API_KEY"] = "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"  
    client = Client(api_key=os.getenv("GROQ_API_KEY"))
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
            "role": "user",
            "content": "Generate a recipe using the following ingredients: " + ", ".join([item[0] for item in db_handler.get_inventory()]),
            },
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    response_text = ""
    for chunk in completion:
        response_text += chunk.choices[0].delta.content or ""

    if response_text:
        print(response_text)
        return response_text
    else:
        print("I received no meaningful response. Please try again.")