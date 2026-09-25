import chromadb

from app.rag.embeddings import embed_text


CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "rag_documents"
DEFAULT_TOP_K = 5


def get_collection():
    client = chromadb.PersistentClient(path=CHROMA_PATH)

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    return collection


def retrieve_documents(query, top_k=DEFAULT_TOP_K):
    query_embedding = embed_text(query)

    collection = get_collection()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
    )

    return results