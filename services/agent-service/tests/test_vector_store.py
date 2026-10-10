from pathlib import Path

from dotenv import load_dotenv

from app.rag.document_loader import load_documents
from app.rag.text_splitter import split_documents
from app.rag.vector_store import create_vector_store

AGENT_SERVICE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = AGENT_SERVICE_DIR.parent.parent

KNOWLEDGE_DIR = AGENT_SERVICE_DIR / "knowledge"
ENV_FILE = PROJECT_ROOT / ".env"

load_dotenv(ENV_FILE)

def test_vector_store_search():
    documents = load_documents(str(KNOWLEDGE_DIR))
    chunks = split_documents(documents)

    vector_store = create_vector_store(chunks)

    result = vector_store.similarity_search(
        "What happens if I cancel my subscription?",
        k=2
    )

    assert len(result) > 0
    print("\nSearch Results:")
    for index, document in enumerate(result):
        print(f"\n--- RESULT {index+1} ---")
        print("Source:", document.metadata.get("source"))
        print(document.page_content)