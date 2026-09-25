from app.rag.embeddings import embed_text


def embed_chunks(chunks):
    embedded_chunks = []

    for chunk in chunks:
        embedded_chunks.append(
            {
                "source": chunk["source"],
                "chunk_id": chunk["chunk_id"],
                "content": chunk["content"],
                "embedding": embed_text(chunk["content"]),
            }
        )

    return embedded_chunks