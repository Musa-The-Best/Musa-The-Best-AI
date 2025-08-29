import requests
from PIL import Image
import io
import os

# Hugging Face API URL
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"

def generate_image(prompt, neg_prompt="", api_token=None, save_path="output.png"):
    """
    Sends a text prompt (and optional negative prompt) to the Stable Diffusion API
    and saves the generated image as a PNG file.
    """
    headers = {"Authorization": f"Bearer {api_token}"}

    # Build payload with optional parameters
    payload = {
        "inputs": prompt,
        "parameters": {
            "negative_prompt": neg_prompt
        }
    }

    # API request
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
    except Exception as e:
        print(f"Error: {e}")
        return None

    # Check if response has image bytes
    if "image" in response.headers.get("Content-Type", ""):
        image = Image.open(io.BytesIO(response.content))
        image.save(save_path)
        print(f"Image saved as {save_path}")
        return save_path
    else:
        print("Error: Response did not return an image. Possibly an error message.")
        print(response.json())
        return None

def main():
    print("Stable Diffusion Text-to-Image Generator API")
    api_token = input("Enter your Hugging Face API token: ").strip()

    while True:
        prompt = input("\nEnter your text prompt (or 'q' to quit): ").strip()
        if prompt.lower() == "q":
            break

        # Ask for user-specified negative prompt
        neg_prompt = input("Enter a negative prompt (press Enter to skip): ").strip()

        save_path = input("Enter file name to save image (press Enter for default 'output.png'): ").strip()
        if not save_path:
            save_path = "output.png"

        print("\nGenerating image with the following parameters:")
        print(f"Prompt: {prompt}")
        print(f"Negative Prompt: {neg_prompt}")

        # Generate image
        result = generate_image(prompt, neg_prompt, api_token=api_token, save_path=save_path)
        if result:
            try:
                img = Image.open(result)
                img.show()  # This will open the image with the system viewer
            except Exception as e:
                print(f"Could not open the image: {e}")

if __name__ == "__main__":
    main()
