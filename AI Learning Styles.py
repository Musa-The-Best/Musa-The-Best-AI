from google import genai
from google.genai import tpyes
import config
client= genai.Client(api_key=config.MUSA_BEST_API_KEY)
def generate_response(prompt, temprature=0.3);
    try:
        contents = [types.conetent(role="user", parts=[types.Part.from_text(text=prompt)])]
        config_params = types.GenerateCOntentConfig(temprature=temprature)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            content=contents,
            config=config_params
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
def run_activity():
    category = input("Enter a category (e.g., fruit, city, animal): ")
    itwm = input(f"Enter a specific {category}: ")
    print("\n--- ZERO-SHOT ---")
    zero