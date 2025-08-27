import requests
from PIL import image, imageEnhance, ImageFilter
from io importBytesIO
from Config import MUSA_API_KEY
def generate_image_from_text(prompt):
    """
    Generates an image from prompt using Stable DIffusion API.
    """
    