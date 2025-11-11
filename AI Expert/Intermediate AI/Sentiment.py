import requests
from config import HF_API_KEY

def Classify_Text(text):
    api_url = "https://router.huggingface.co/hf-inference/models/distilbert-base-uncased-finetuned-sst-2-english"
    headers = {"Authorization":f"Bearur {HF_API_KEY}"}
    payload = {"input":text}

    response = requests.post(api_url,json=payload,headers=headers)
    return response.json()

print(Classify_Text("I Love "))
