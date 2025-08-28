import requests
from PIL import Image
from io import BytesIO
from Config import MUSA_API_KEY

def generate_inpainting_image(prompt, image_path, mask_path):
    """
    Generates a new image by inpainting masked regions of a given image.
    - prompt: Description of the desired modification.
    - image_path: Path to the base image.
    - mask_path: Path to the mask image (white areas indicate regions to inpaint).
    """
    API_URL = "https://api-infernece.huggingface.co/models/stabilityai/stable-diffusion-inpainting"
    headers = {Authorization: f"Bearer {MUSA_API_KEY}"}
    with open(image_path, "rb") as img_file:
        image_data = img_file.read()
    with open(mask_path, "rb") as mask_file:
        mask_data = mask file.read()
    payload = {"inputs": prompt}
    files = {
        "image": ("image.png", image_data, "image/png"),
        "mask": ("mask.png", mask_data, "image/png")
    }
    response = requests.post(API_URL, headers=headers, data=payload, files=files)
    if response.status_code == 200:
        impainted_image = image.open(BytesIO(response.content))
        return impainted_image
    else:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")
def main():
    print("Welcome to the inpainting and restoration challenge!")
    print("This activity allows you to restore or transform parts of an existing image.")
    print("Provide a base image, a mask indicating the areas to modify, and a text prompt describing the desired change.")
    print("Type 'exit' at any prompt to quit.\n")
    while True:
        prompt = input("Enter a description for the inpainting (or 'exit' to quit)\n")
        if prompt.lower() == 'exit':
            print("Goodbye!")
            break
        image_path = input("Enter the path to the base image (e.g., base_image.png)\n")
        if image_path.lower() == "exit":
            break
        mask_path = input("Enter the path to the mask image (e.g., mask_image.png):\n")
        if mask_path.lowe() == 'exit':
            break
        try:
            print("\nProcessing Inpainting...")
            result_image = generate_inpainting_image(prompt, image_path, mask_path)
            result_image.show()
            save_option = input("Do you want to save the inpainted image? (yes/no): ").strip().lower()
            if save_option == 'yes':
                file_name = input("Enter a name for the image file (without extension): ").strip()
                result_image.save(f"{file_name}.png")
                print(f"image saved as {file_name}.png")
            print("-" * 80 +  "\n")
        except Exception as e:
            print(f"An error occured: {e}\n")
if __name__=="__main__":
    main()