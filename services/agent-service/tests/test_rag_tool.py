from dotenv import load_dotenv
from pathlib import Path

AGENT_SERVICE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = AGENT_SERVICE_DIR.parent.parent

load_dotenv(PROJECT_ROOT / ".env")

from app.tools.rag_tools import search_knowledge_base

def test_search_knowledge_base():

    result = search_knowledge_base.invoke({
        "question": "What happens if I cancel my subscription?"
    })

    print("\nRAG tool result:")
    print(result)

    assert len(result["source"]) > 0
    assert result["grounded"] is True