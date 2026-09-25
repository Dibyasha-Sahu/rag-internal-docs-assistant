import chromadb

from ingestion.loader import load_documents
from ingestion.cleaner import clean_documents
from ingestion.chunker import chunk_documents
from ingestion.embedder import embed_chunks


CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "rag_documents"


def get_collection():
    client = chromadb.PersistentClient(path=CHROMA_PATH)

    return client.get_or_create_collection(
        name=COLLECTION_NAME
    )


def ingest_documents():
    documents = load_documents()
    cleaned_documents = clean_documents(documents)

    chunks = chunk_documents(
        cleaned_documents,
        chunk_size=800,
        chunk_overlap=100,
    )

    embedded_chunks = embed_chunks(chunks)

    collection = get_collection()

    ids = []
    documents_data = []
    embeddings = []
    metadatas = []

    for chunk in embedded_chunks:
        ids.append(
            f"{chunk['source']}::chunk-{chunk['chunk_id']}"
        )

        documents_data.append(chunk["content"])
        embeddings.append(chunk["embedding"])

        metadatas.append(
            {
                "source": chunk["source"],
                "chunk_id": chunk["chunk_id"],
            }
        )

    collection.upsert(
        ids=ids,
        documents=documents_data,
        embeddings=embeddings,
        metadatas=metadatas,
    )

    return len(embedded_chunks)


if __name__ == "__main__":
    count = ingest_documents()

    print(f"Ingestion completed successfully.")
    print(f"Chunks stored: {count}")