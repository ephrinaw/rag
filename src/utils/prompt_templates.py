def get_rag_prompt(question: str, context: str) -> str:
    """
    Returns the prompt for Retrieval-Augmented Generation.
    """
    return f"Question: {question}\nContext: {context}\nAnswer:"

def get_hallucination_check_prompt(generation: str, documents: str) -> str:
    """
    Returns a prompt for checking hallucination in the generated answer.
    """
    return f"Answer: {generation}\nDocuments: {documents}\nIs this answer grounded in the documents? (yes/no)"

def get_relevance_check_prompt(document: str, question: str) -> str:
    """
    Returns a prompt for checking relevance of a document to the question.
    """
    return f"Document: {document}\nQuestion: {question}\nIs this document relevant? (yes/no)"
