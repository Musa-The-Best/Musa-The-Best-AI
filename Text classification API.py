import requests

# Hugging Face API endpoint for DistilBERT (sentiment analysis)
api_url = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"

# Your Hugging Face API token (replace with your actual token)
headers = {
    "Authorization": "Bearer YOUR_API_KEY_HERE"
}

# Text to classify (example sentence)
text = "I love learning about AI! It's so fascinating."

# Make a POST request to the Hugging Face API
response = requests.post(api_url, headers=headers, json={'inputs': text})

if response.status_code == 200:
    # Parse and print the results
    classification = response.json()
    print("Predicted label:", classification[0]['label'])
else:
    print(f"Error: {response.status_code}")