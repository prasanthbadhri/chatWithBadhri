from langchain_mistralai import ChatMistralAI
import streamlit as st

st.title("Chat with Badhri")

with st.sidebar:
    st.title("Provide your Mistral API Key")
    mistral_api_key = st.text_input("Mistral API Key", type="password")
if not mistral_api_key:
    st.error("Please enter your Mistral API Key in the sidebar.")
    st.stop()

llm = ChatMistralAI(mistral_api_key = mistral_api_key, temperature=0.6)

question = st.text_input("enter the question: ")

if question:
    response = llm.invoke(question)
    st.write(response.content)

# Command to run the streamlit files is : streamlit run <fileaname>