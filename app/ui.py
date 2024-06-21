"""_summary_
"""

from helpers.langchain_helper import generate
from dotenv import load_dotenv
import streamlit as st
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

load_dotenv()


st.title("langchain Chat Application")

import streamlit as st
import random
import time


# Streamed response emulator
def response_generator(text):
    response = generate(text)
    
    yield response
        
st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    print("prompt",prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    
uploaded_file = st.sidebar.file_uploader("Choose a file", type="pdf")

if uploaded_file:
    print(f"file uploaded : {uploaded_file}")
    bytes_data = uploaded_file.getvalue()
    