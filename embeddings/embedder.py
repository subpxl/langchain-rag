from langchain_ollama import OllamaEmbeddings
from config import OLLAMA_BASE_URL, EMBED_MODEL

def get_embedder():
    return OllamaEmbeddings(
        model=EMBED_MODEL,
        base_url=OLLAMA_BASE_URL
    )

if __name__=="__main__":
    get_embedder()