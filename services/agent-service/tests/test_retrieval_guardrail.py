from pathlib import Path

from dotenv import load_dotenv

from app.guardrails.retrieval_guardrail import filter_relevant_documents
from app.rag.document_loader import load_documents
from app.rag.text_splitter import split_documents
from app.rag.vector_store import create_vector_store, search_with_scores


AGENT_SERVICE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = AGENT_SERVICE_DIR.parent.parent

KNOWLEDGE_DIR = AGENT_SERVICE_DIR / "knowledge"

load_dotenv(PROJECT_ROOT / ".env")


def test_relevant_question():
    documents = load_documents(str(KNOWLEDGE_DIR))
    chunks = split_documents(documents)

    vector_store = create_vector_store(chunks)

    results = search_with_scores(
        vector_store,
        "What happens when I cancel my subscription?"
    )

    print("\nRESULTS:")

    for document, score in results:
        print("\nScore:", score)
        print(document.page_content)

    relevant_documents = filter_relevant_documents(results)

    assert len(relevant_documents) > 0

def test_irrelevant_question():
    documents = load_documents(str(KNOWLEDGE_DIR))
    chunks = split_documents(documents)

    vector_store = create_vector_store(chunks)

    results = search_with_scores(
        vector_store,
        "How do I repair the transmission in my car?"
    )

    print("\nIRRELEVANT QUESTION RESULTS:")

    for document, score in results:
        print("\nScore:", score)
        print(document.page_content)

    relevant_documents = filter_relevant_documents(results)

    assert len(relevant_documents) == 0