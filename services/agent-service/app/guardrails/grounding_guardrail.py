from langchain_openai import ChatOpenAI

class GroundingGuardrail:

    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-6-luna"
        )

    def is_grounded(self, answer: str, context: str) -> bool:

        prompt = f"""
You are a grounding evaluator.

Determine whether the ANSWER is fully supported by the CONTEXT.

Do not judge whether the answer is generally true.
Only determine whether it is supported by the supplied context.

Return exactly one word:

YES
or
NO

CONTEXT:
{context}

ANSWER:
{answer}
"""

        response = self.llm.invoke(prompt)
        return response.content.strip().upper() == "YES"