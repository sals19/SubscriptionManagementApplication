from dotenv import load_dotenv
from pathlib import Path

from app.rag.rag_service import RAGService

AGENT_SERVICE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = AGENT_SERVICE_DIR.parent.parent

load_dotenv(PROJECT_ROOT / ".env")

def test_cancellation_question():

    rag = RAGService()
    result = rag.ask("What happens if I cancel my subscription?")

    print("\nRAG Result:")
    print(result)

    assert result["grounded"] is True
    assert len(result["source"]) > 0

def test_unrelated_question():

    rag = RAGService()
    result = rag.ask("How do I repair my car transmission?")

    print("\nUnrelated result:")
    print(result)

    assert result["grounded"] is False
    assert result["source"] == []
