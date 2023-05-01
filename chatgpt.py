import requests
import json
import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Given a prompt, getGptText returns ChatGPT response
def getGptText(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        temperature=0.7
    )

    # Print the generated text from the response
    generated_text = response['choices'][0]['text']
    return(generated_text)

prompt = "explain how the gensim library for python works"
print(getGptText(prompt))