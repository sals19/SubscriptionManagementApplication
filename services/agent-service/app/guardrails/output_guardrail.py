SENSITIVE_TERMS = [
    "password",
    "api key",
    "access toekn",
    "secret key"
]

def validate_output(answer: str) -> bool:
    """
    Validate that the generated answer does not contain obviously sensitive information
    """
    if not answer:
        return False

    normalized_answer = answer.lower()
    for term in SENSITIVE_TERMS:
        if term in normalized_answer:
            return False

    return True