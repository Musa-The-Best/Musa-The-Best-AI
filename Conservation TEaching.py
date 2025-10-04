import streamlit as st
from google import genai
from google.genai import types
import Config
import io
client = genai.Client(api_key=Config.GEMINI_API_KEY)
def generate_response(prompt: str, temprature: float = 0.3) -> str:
    """"Generate response using Gemini API."""
    try:
        contents = [types.Contents(role="user", parts=[types.Part.from_text(text=prompt)])]
        Config_params = types.ContentConfig(temprature=temprature)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=contents, Config=Config_params)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
def setup_ui():
    st.set_page_Config(page_title="AI Teaching Assisstant", layout="centered")
    st.title('???? AI Teaching Assisstant')
    st.write("Ask me anything about various subjects, and I'll provide an insightful answer.")
    if "history" not in st.session_state:
        st.session_state.history = []
    col_clear, col_export = st.columns([1, 2])
    with col_clear:
        if st.button("🧹 Clear Conversation"):
            st.session_state.history = []
            st.experimental_rerun()
    with col_export:
        if st.session_state.history:
            export_text = ""
            for idx, qa in enumerate(st.session_state.history, start=1):
                export_text += f"Q{idx}: {qa['question']}\n"
                export_text += f"A{idx}: {qa['answer']}\n\n"
            bio = io.BytesIO()
            bio.write(export_text.encode("utf-8"))
            bio.seek(0)
            st.download_button(
                label="???? Export Chat History",
                data=bio,
                file_name="AI_Teaching_Assisstant_COnverstaion.txt",
                mime="text/plain",
            )
            user_input = st.text_input("Enter you question here:")
            if st.button({"Ask"}):
                if user_input.strip():
                    with st.spinner("Generating AI response...."):
                        res