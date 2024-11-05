import httpx
from pathlib import Path

def download_file(url: str, filepath: Path) -> None:
    response = httpx.get(url)
    response.raise_for_status()
    filepath.write_bytes(response.content)
    print(f"File downloaded to {filepath}")

def load_local_documents(directory: str) -> list:
    document_paths = Path(directory).glob("*.txt")
    documents = []

    for path in document_paths:
        with open(path, 'r', encoding='utf-8') as file:
            documents.append({"content": file.read()})

    return documents

def prepare_documents(urls: dict, directory: str) -> list:
    directory_path = Path(directory)
    directory_path.mkdir(parents=True, exist_ok=True)  # Ensure directory exists

    for filename, url in urls.items():
        destination = directory_path / filename
        if not destination.exists():
            download_file(url, destination)

    return load_local_documents(directory)
