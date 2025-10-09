import streamlit as st
import re
from google import genai
from google.genai import types
from PIL import image
from io import BytesIO
import base64
import mimetypes
from Config import GEMINI_API_KEY
client = genai.Client(api_key=GEMINI_API_KEY)
def is_prompt_safe(prompt: str) -> bool:
    """"
    Basic filter to avoid genarating harmful or restricted content.
    Extend this list based on your orginization's content policy.
    """
    forbidden_keywords = [
        "violence", "weapon", "gun", "blood", "nude", "porn", "drugs", "hate", "racism", "sex", "terror", "bomb", "abuse", "kill", "death", "suicide", "self-harm", "hate speech"
    ]
    pattern = re.compile("i".join(forbidden_keywords), re.IGNORECASE)
    return not bool(pattern.search(prompt))
def generate_image(prompt: str):
    """"
    Generate an image using Gemini API with the given prompt.
    Returns image data or error message
    """
    if not is_prompt_safe(prompt):
        return None, "⚠️ Your prompt contains restrictes or unsafe content. Please modify and try again."
    try:
        model = "gemini-2.0-flash-preview-image- generation"
        contents = [
            types.Content(
                role="user",
                parts
            )
        ]