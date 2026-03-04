from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.runnables import RunnablePassthrough
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from prompts.rag_prompts import get_rag_prompt

from vectorstore.store import get_vectorstore
from config import CHAT_MODEL, OLLAMA_BASE_URL


# --- Session memory store ---
store = {}

def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


# --- Format retrieved docs ---
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def get_rag_chain():
    llm = ChatOllama(
        model=CHAT_MODEL,
        base_url=OLLAMA_BASE_URL
    )

    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    prompt = get_rag_prompt()

#     prompt = ChatPromptTemplate.from_messages([
#         ("system", """You are a helpful assistant. Use the following context to answer the question.
# If you don't know the answer, say you don't know.

# Context:
# {context}"""),
#         MessagesPlaceholder(variable_name="chat_history"),
#         ("human", "{input}"),
#     ])

    # Core RAG chain
    rag_chain = (
        RunnablePassthrough.assign(
            context=lambda x: format_docs(retriever.invoke(x["input"]))
        )
        | prompt
        | llm
        | StrOutputParser()
    )

    # Wrap with message history
    chain_with_history = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
    )

    return chain_with_history


if __name__ == "__main__":
    chain = get_rag_chain()

    # Pass session_id to track conversations
    response = chain.invoke(
        {"input": "What is this document about?"},
        config={"configurable": {"session_id": "user_123"}},
    )
    print(response)

    # Follow-up — memory is retained
    response = chain.invoke(
        {"input": "Can you elaborate on the first point?"},
        config={"configurable": {"session_id": "user_123"}},
    )
    print(response)