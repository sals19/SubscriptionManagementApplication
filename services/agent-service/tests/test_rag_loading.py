from pathlib import Path

from app.rag.document_loader import load_documents
from app.rag.text_splitter import split_documents


BASE_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = BASE_DIR / "knowledge"


def test_load_documents():
    documents = load_documents(str(KNOWLEDGE_DIR))

    assert len(documents) > 0

    print("\nLoaded documents:", len(documents))

    for document in documents:
        print("\nSOURCE:")
        print(document.metadata.get("source"))

        print("\nCONTENT:")
        print(document.page_content[:200])


def test_split_documents():
    documents = load_documents(str(KNOWLEDGE_DIR))

    chunks = split_documents(documents)

    assert len(chunks) > 0

    print("\nNumber of chunks:", len(chunks))

    for index, chunk in enumerate(chunks[:5]):
        print(f"\n--- CHUNK {index + 1} ---")
        print("Source:", chunk.metadata.get("source"))
        print(chunk.page_content)