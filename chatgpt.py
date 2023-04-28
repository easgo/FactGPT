import requests
import json
import os
import openai

def getGptText(prompt):
    # Setting up the API endpoint and API key
    url = 'https://api.openai.com/v1/engines/davinci-codex/completions'
    
    openai.organization = "YOUR_ORG_ID"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.Model.list()

    # Set up the request headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    # Set up the request data
    data = {
        'prompt': prompt,
        'max_tokens': 50,
        'temperature': 0.7
    }

    # Send the request to the API
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Get the response data as a JSON object
    response_data = json.loads(response.content)

    # Print the generated text from the response
    generated_text = response_data['choices'][0]['text']
    return(generated_text)