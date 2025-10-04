import streamlit as st
from google import genai
from google.genai import types
import config

# Initialize the Gemini API client
client = genai.Client(api_key=config.GEMINI_API_KEY)

# Function to generate AI response from Gemini API
def generate_response(prompt, temperature=0.3):
    """Generate a response from Gemini API."""
    try:
        contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
        config_params = types.GenerateContentConfig(temperature=temperature)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=contents,
            config=config_params
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI Setup
def setup_ui():
    st.title("AI Teaching Assistant")
    st.write("Welcome! You can ask me anything about various subjects, and I'll provide an answer.")

    # Get user input (question)
    user_input = st.text_input("Enter your question here:")

    if user_input:
        # Show the user's input
        st.write(f"**Your question:** {user_input}")

        # Generate AI response from Gemini API
        response = generate_response(user_input)

        # Display AI's response
        st.write(f"**AI's answer:** {response}")
    else:
        st.write("Please enter a question to ask.")

# Main function to run the app
def main():
    setup_ui()

if __name__ == "__main__":
    main()
