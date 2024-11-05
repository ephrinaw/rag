import streamlit_app as st
from src.main import Chatbot

# Initialize chatbot
chatbot = Chatbot()

# Load some documents into the local data
documents = ["Local document 1 content...", "Local document 2 content..."]
chatbot.load_documents(documents)

st.title("LLM-Powered Chatbot with Local and Internet Search")

# User input
question = st.text_input("Ask a question:")

if st.button("Submit"):
    if question:
        answer = chatbot.answer_question(question)
        st.write("Answer:", answer)
    else:
        st.write("Please enter a question.")
