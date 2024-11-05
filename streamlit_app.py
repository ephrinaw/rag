import streamlit_app as st
from src.main import main

st.title("Student-wellbeing Chatbot")

question = st.text_input("Enter your question:")
if question:
    answer = main(question)
    st.write("Answer:", answer)
