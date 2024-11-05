from src.answer_generator import generate_answer
from src.config import Config
from src.retriever import retrieve_documents
from src.hallucination_checker import check_hallucination
from src.web_search import perform_web_search
from src.document_loader import prepare_documents

def main(question, user_documents=None):
    documents = retrieve_documents(question, user_documents)

    # If no relevant documents are found, perform a web search
    if not documents:
        documents = perform_web_search(question)

    answer = generate_answer(question, documents)

    # Check for hallucination in the generated answer
    if check_hallucination(answer, documents, question):
        return answer
    else:
        return "Answer might contain hallucinations. Please verify."

if __name__ == "__main__":
    # Prepare predefined documents
    urls = {
        "doc1.txt": "https://example.com/doc1.txt",
        "doc2.txt": "https://example.com/doc2.txt"
    }
    prepare_documents(urls, Config.DOCUMENT_DIRECTORY)
    
    # Run chatbot
    question = input("Enter your question: ")
    print(main(question))
