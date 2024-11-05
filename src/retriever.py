from src.vector_store import VectorStoreManager

# Initialize the vector store manager
vector_store_manager = VectorStoreManager()

def retrieve_documents(question, user_documents=None):
    """
    Retrieves documents relevant to the question from the vector store
    or from user-provided documents if available.
    Args:
        question (str): The user's question.
        user_documents (list): Optional list of user-uploaded documents.
    Returns:
        List of relevant documents.
    """
    if user_documents:
        vector_store_manager.add_documents(user_documents)  # Add user documents to the store temporarily
        results = vector_store_manager.search(question)
        return [doc.content for doc in results]

    # Otherwise, search the existing vector store
    results = vector_store_manager.search(question)
    return [doc.content for doc in results]
