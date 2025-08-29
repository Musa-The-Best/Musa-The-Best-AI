
import requests
from config import HF_APIKEY

MODEL_ID = "nlpconnect/vit-gpt2-image-captioning"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"
headers = {
    "Authorization": f"Bearer {HF_APIKEY}"
}

def caption_single_image(image_source="3x3 logo.png"):
    """Generate a caption for a single image using the Hugging Face API."""
    try:
        with open(image_source, "rb") as f:
            image_bytes = f.read()
    except FileNotFoundError:
        print(f"[Error] Image file '{image_source}' not found.")
        return
    except Exception as e:
        print(f"[Error] Unable to open image file. Details: {e}")
        return

    response = requests.post(API_URL, headers=headers, data=image_bytes)

    if response.status_code != 200:
        print(f"[Error] API request failed with status code {response.status_code}: {response.text}")
        return

    try:
        result = response.json()
    except requests.exceptions.JSONDecodeError:
        print("[Error] Failed to parse the response as JSON.")
        return

    if isinstance(result, dict) and "error" in result:
        print(f"[Error] {result['error']}")
        return

    caption = result[0].get("generated_text", "No caption found")
    print(f"Image: {image_source}\nCaption: {caption}")

def main():
    caption_single_image()

if __name__ == "__main__":
    main()
