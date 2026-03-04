from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from langchain_qdrant import QdrantVectorStore
from embeddings.embedder import get_embedder
from config import QDRANT_URL, COLLECTION_NAME

# nomic-embed-text produces 768-dim vectors
VECTOR_SIZE = 768


def get_vectorstore(documents=None):
    embedder = get_embedder()
    client = QdrantClient(url=QDRANT_URL)

    if not client.collection_exists(COLLECTION_NAME):
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE),
        )
        print(f"[vectorstore] Created collection '{COLLECTION_NAME}' on {QDRANT_URL}")

    if documents:
        return QdrantVectorStore.from_documents(
            documents=documents,
            embedding=embedder,
            collection_name=COLLECTION_NAME,
            url=QDRANT_URL,
        )

    return QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
        embedding=embedder,
    )