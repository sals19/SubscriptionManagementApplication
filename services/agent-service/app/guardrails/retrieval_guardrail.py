MIN_RELEVANCE_SCORE = 0.5

def filter_relevant_documents(results):
    """
    keep only those documents whose relevance score is high enough.
    """

    relevant_documents = []
    for document, score in results:
        if score >= MIN_RELEVANCE_SCORE:
            relevant_documents.append(document)

    return relevant_documents