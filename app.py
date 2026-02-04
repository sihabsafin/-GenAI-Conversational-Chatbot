import streamlit as st
from llm_engine import get_ai_response
from pathlib import Path

# Page config
st.set_page_config(
    page_title="GenAI Conversational Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Load custom CSS
css_path = Path("assets/style.css")
if css_path.exists():
    st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

# Header
st.markdown("## 🤖 GenAI Conversational Chatbot")
st.caption("Powered by Groq • Built with LangChain • Deployed via Streamlit")

# Session state for chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"<div class='chat-bubble-user'>{msg['content']}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div class='chat-bubble-bot'>{msg['content']}</div>",
            unsafe_allow_html=True
        )

# Input box
user_input = st.chat_input("Ask anything...")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.spinner("Thinking..."):
        response = get_ai_response(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.rerun()
