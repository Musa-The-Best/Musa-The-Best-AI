import requests
from PIL import Image
from io import BytesIO
from config import HF_API_KEY

# Define the API endpoint as a constant
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"

def generate_image_from_text(prompt: str) -> Image.Image:
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": prompt}

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()  # Raise an error for bad status codes

        # Check if the response content is an image
        if 'image' in response.headers.get('Content-Type', ''):
            image = Image.open(BytesIO(response.content))
            return image
        else:
            raise Exception("The response is not an image. It might be an error message.")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")
def main():
    """
    Main loop for user interaction. Continuously prompts the user for a description,
    generates an image via the API, displays it, an offers an option yo save the image.
    """
    print("Welcome to the Text-to-Image Generator!")
    print