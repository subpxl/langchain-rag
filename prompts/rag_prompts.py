from langchain_core.prompts import PromptTemplate

SYSTEM_PROMPT = """You are a precise assistant.
Answer ONLY using the provided context.
If the answer is not in the context, say "I don't know".
Do not hallucinate.
"""

RAG_PROMPT = PromptTemplate(
    input_variables=["context", "input"],
    template="""
{system_prompt}

Context:
{context}

Question:
{input}

Answer:
"""
)

def get_rag_prompt():
    return RAG_PROMPT.partial(system_prompt=SYSTEM_PROMPT)

if __name__ == "__main__":
    get_rag_prompt()