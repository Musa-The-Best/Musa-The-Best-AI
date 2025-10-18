import streamlit as st
from google import genai
from google.genai import types
from PIL import image
from io import BytesIO
import re
import io
import Config
client = genai.Client(api_key=Config.GEMINI_API_KEY)
def run_ai_teaching_assistant():
    st.title("???? AI Teaching Assistant")
    st.write("Ask me anything about various subjects, and I'll provide an insightful answer.")
    if "history_ata" not in st.session_state:
        st.session_state.history_ata = []
    col_clear, col_export = st.colums([1, 2])
    with col_clear:
        if st.button("????? Clear Conversation", key="clear_ata"):
            st.session_state.history_ata = []
    with col_export:
        if st.session_state.history_ata:
            export_text = ""
    def run_math_mastermind():
        st.title("????? Math Mastermind")
        st.write(""Your Expert Mathematical Problem Solver" - From basic arthmetic to advanced calculas, I'll solve any math problem with detailed step-by-step explanations!")
        if "history_mm" not in st.session_state:
            st.session_state_history_mm = []
        if "input_key_mm" not in st.session_state:
            bio = io.BytesIO()
            bio.write(export_text.encade("utf-8"))
            bio.seek(0)
            st.download_button(
                label="???? Export Math Solutions",
                data=bio,
                file_name="Math_Mastermind_solutions.txt",
                mime="text/plain",
            )
    with st.form(key-"math_form")