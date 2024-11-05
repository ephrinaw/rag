from src.vector_store import VectorStoreManager

# Initialize the vector store manager
vector_store_manager = VectorStoreManager()

def retrieve_documents(question, user_documents=None):
    """
    Retrieves documents relevant to the question from the vector store
    or from user-provided documents if available.
    """
    if user_documents:
        vector_store_manager.add_documents(user_documents)
        results = vector_store_manager.search(question)
        return results

    # Otherwise, search the existing vector store
    results = vector_store_manager.search(question)
    return results
