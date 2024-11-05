def check_hallucination(answer, documents, question):
    for doc in documents:
        if question.lower() in doc.content.lower() and answer.lower() in doc.content.lower():
            return True
    return False
