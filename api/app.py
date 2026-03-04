from fastapi import FastAPI
from pydantic import BaseModel
from rag.chain import get_rag_chain

app = FastAPI(title="RAG API")

rag_chain = get_rag_chain()


class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
    sources: list[str]


@app.post("/chat", response_model=QueryResponse)
def chat(req: QueryRequest):
    result = rag_chain.invoke({"question": req.question})

    sources = []
    for doc in result.get("source_documents", []):
        sources.append(doc.metadata.get("source", "unknown"))

    return {
        "answer": result["answer"],
        "sources": sources
    }