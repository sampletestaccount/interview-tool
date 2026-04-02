import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Streamlit Chat", page_icon="") 
st.title("Chatbot")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o"

