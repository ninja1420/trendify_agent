import streamlit as st
import requests
from constants import API_URL

# Page configuration
st.set_page_config(
    page_title="✨ FashionFinder GenZ 💖",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .chat-box { background-color: #f8f0fc; border-radius: 12px; padding: 10px; margin-bottom: 10px; }
    .user-msg { background-color: #ffe5f1; }
    .agent-msg { background-color: #e0f7fa; }
    </style>
    """, unsafe_allow_html=True
)

# Sidebar controls
st.sidebar.header("⚙️ Settings")
provider = st.sidebar.radio("Model Provider", ("Groq", "OpenAI"))
if provider == "Groq":
    model_names = ["llama3-70b-8192", "llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
else:
    model_names = ["gpt-4o-mini"]
model_name = st.sidebar.selectbox("Model", model_names)
allow_search = st.sidebar.checkbox("Allow Web Search 🔍", value=True)

# Main header
st.title("👗 FashionFinder 💬")
st.subheader("Ask me anything about the latest fashion trends! 🌟")
st.write("Just type your question below and hit the button. I'm here to sprinkle some style magic ✨")

# Initialize session state for chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Input area
user_input = st.text_input("Your fashion question... 💡", key="user_input")
ask_btn = st.button("Ask Agent! 🤖")

# Display trending tags
with st.expander("🔥 Trending Tags Demo 🔥", expanded=False):
    cols = st.columns(4)
    tags = ["#StreetStyle", "#SustainableFashion", "#Y2KRevival", "#Athleisure"]
    for col, tag in zip(cols, tags):
        if col.button(tag):
            user_input = tag
            ask_btn = True

# Handle ask button
if ask_btn and user_input.strip():
    with st.spinner("Glam up your answer... 💅"):
        payload = {
            "model_name": model_name,
            "model_provider": provider,
            "messages": [user_input],
            "allow_search": allow_search
        }
        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code != 200:
                st.error("Error: Unable to fetch response from the server.")
                st.stop()
            st.subheader("Agent Response:")
            st.markdown(f'***Final Response***:{response.json()}')
    
        except Exception as e:
            st.error(f"Oops! Something went wrong: {e}")
            st.stop()

# Footer
st.markdown("---")
st.caption("Built with ❤️ by FashionFinder | Powered by LangGraph API")
