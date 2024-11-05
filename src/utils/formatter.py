def format_text(text: str) -> str:
    """
    Formats text by removing extra whitespace, newlines, and converting to lowercase.
    """
    return " ".join(text.strip().split()).lower()

def format_docs(documents: list) -> str:
    """
    Formats a list of document contents into a single text block.
    """
    return "\n".join([doc["content"] for doc in documents])
