import requests

def chatGPT(text):
    url = "https://api.openai.com/v1/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR-API", #replace with your own API
    }
    data = {
        "model": "text-davinci-003",
        "prompt": text,
        "max_tokens": 4000,
        "temperature": 1.0,
    }
    response = requests.post(url, headers=headers, json=data)
    output = response.json()['choices'][0]['text']

    return print(output)


