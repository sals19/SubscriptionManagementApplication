from langchain_chroma import Chroma

from app.rag.embeddings import get_embedding_model

def create_vector_store(chunks):

    embedding_model = get_embedding_model()
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        collection_name="subscription_knowledge"
    )
    return vector_store

def search_with_scores(vector_score, query: str, k: int = 3):
    return vector_score.similarity_search_with_relevance_scores(
        query,
        k=k,
    )
