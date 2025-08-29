import os
import requests
from PIL import Image

def add():
    # Define the user for the images folder, processes each image in that folder
    # using Hugging Face API for captioning, and saves results to a text file.

    # Step 1. Input user for folder path
    folder_path = input("Enter the path to your images folder (press Enter for 'images'): ").strip()
    if not folder_path:
        folder_path = "images"  # Default folder
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' path does not exist. Exiting.")
        return

    # Step 2. Hugging Face API details
    HUG_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
    API_KEY = "your_huggingface_api_key"  # Replace with your actual key
    headers = {"Authorization": f"Bearer {API_KEY}"}

    # Step 3. Find images and caption each
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not image_files:
        print(f"No image files found in '{folder_path}'. Exiting.")
        return

    captions = []

    for img_file in image_files:
        img_path = os.path.join(folder_path, img_file)
        print(f"Processing {img_file}...")

        # Step 3.1: Load image
        try:
            image = Image.open(img_path)
        except Exception as e:
            print(f"Error loading {img_file}: {e}")
            continue

        # Step 3.2: Send POST request to Hugging Face
        with open(img_path, "rb") as f:
            response = requests.post(HUG_URL, headers=headers, data=f.read())
        if response.status_code != 200:
            print(f"Error from API for {img_file}: {response.status_code}")
            continue

        # Step 3.3: Check API output
        result = response.json()
        if "error" in result:
            print(f"API returned error for {img_file}: {result['error']}")
            continue

        # Step 3.4: Extract caption (assuming first result is most likely true)
        caption = result[0]['generated_text'] if isinstance(result, list) else None
        if caption:
            print(f"Caption: {caption}")
            captions.append(f"{img_file}: {caption}")
        else:
            print(f"No caption generated for {img_file}")

    # Step 4. Save captions to summary file
    output_file = os.path.join(folder_path, "captions_summary.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(captions))

    print(f"\nCaptions written into {output_file}. Please check for errors or try different images.")

if __name__ == "__main__":
    add()
