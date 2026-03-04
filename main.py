from loaders.text_loader import load_and_chunk
from vectorstore.store import get_vectorstore
from rag.chain import get_rag_chain

DATA_PATH = "data/documents.txt"

def ingest():
    docs = load_and_chunk(DATA_PATH)
    get_vectorstore(docs)

def chat():
    chain = get_rag_chain()

    while True:
        query = input(">> ")
        if query.lower() in ("exit", "quit"):
            break

        result = chain.invoke(
            {"input": query},
            config={"configurable": {"session_id": "main"}},
        )
        print(result)

if __name__ == "__main__":
    ingest()   
    chat()