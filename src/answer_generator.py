from langchain_ollama import ChatOllama
from src.utils.prompt_templates import format_docs

def generate_answer(question, documents):
    llm = ChatOllama(model="llama3.2:3b-instruct-fp16", temperature=0)
    formatted_docs = format_docs(documents)
    prompt = f"Question: {question}\nContext: {formatted_docs}\nAnswer:"
    answer = llm.invoke([prompt])
    return answer
