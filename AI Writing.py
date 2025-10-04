import os
import openai
import streamlit as st
from streamlit_chat import message as st_message

# Initialize OpenAI
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Chatbot personality & response logic
def chatbot_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",   # You can replace with "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are Sigma Counselor. You give helpful but slightly sarcastic responses."},
            {"role": "user", "content": user_input},
        ],
    )
    return response['choices'][0]['message']['content']

# Streamlit UI
st.set_page_config(page_title="Sigma Chatbot", page_icon="🤖")
st.title("Sigma Chatbot 🤖")

if "messages" not in st.session_state:
    st.session_state.messages = []  # Store conversation history

# Input box for user
user_input = st.text_input("You: ", "", key="input")

if st.button("Send") and user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get bot response
    bot_reply = chatbot_response(user_input)

    # Add bot message
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

# Display chat history
for i, msg in enumerate(st.session_state.messages):
    if msg["role"] == "user":
        st_message(msg["content"], is_user=True, key=str(i))
    else:
        st_message(msg["content"], key=str(i))
