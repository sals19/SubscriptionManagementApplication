from pathlib import Path

from langchain_openai import ChatOpenAI

from app.rag.document_loader import load_documents
from app.rag.text_splitter import split_documents
from app.rag.vector_store import create_vector_store, search_with_scores
from app.guardrails.retrieval_guardrail import filter_relevant_documents
from app.guardrails.grounding_guardrail import GroundingGuardrail
from app.guardrails.output_guardrail import validate_output

AGENT_SERVICE_DIR = Path(__file__).resolve().parent.parent.parent
KNOWLEDGE_DIR = AGENT_SERVICE_DIR / "knowledge"

class RAGService:

    def __init__(self):
        documents = load_documents(str(KNOWLEDGE_DIR))
        chunks = split_documents(documents)

        self.vector_store = create_vector_store(chunks)

        self.llm = ChatOpenAI(
            model="gpt-6-luna",
        )

        self.grounding_guardrail = GroundingGuardrail()

    def ask(self, question: str) -> dict:

        results = search_with_scores(
            self.vector_store,
            question,
        )

        relevant_documents = filter_relevant_documents(results)

        if not relevant_documents:
            return {
                "answer": "I don't have enough information in my knowlegde base to answer that question.",
                "source": [],
                "grounded": False,
            }

        context = "\n\n".join(
            document.page_content
            for document in relevant_documents
        )

        prompt = f"""
You are a subscription management assistant.

Answer the User's question using ONLY the information contained in the context below.

If the context does not contain enough information to answer the question, say that you do not have enough information.

Do not invent policies, prices, dates, or subscription details.

CONTEXT:
{context}

QUESTION:
{question}
"""

        response = self.llm.invoke(prompt)
        answer = response.content
        if not validate_output(answer):
            return {
                "answer": "I cannot provide that answer",
                "source": [],
                "grounded": False
            }

        is_grounded = self.grounding_guardrail.is_grounded(
            answer, context
        )

        if not is_grounded:
            return {
                "answer": "I don't have enough verified information to answer that question.",
                "sources": [],
                "grounded": False,
                }

        sources = list({
            Path(document.metadata["source"]).name
            for document in relevant_documents
        })

        return {
            "answer": response.content,
            "source": sources,
            "grounded": True,
        }

