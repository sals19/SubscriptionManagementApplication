from langchain_core.tools import tool

from app.rag.rag_service import RAGService

rag_service = RAGService()

@tool
def search_knowledge_base(question: str) -> dict:
    """
    Search the subscription knowledge base for information about
    subscription plans, billing, cancellation policies, and FAQs.

    Use this tool for questions about subscription policies and
    general subscription information.
    """

    return rag_service.ask(question)



        