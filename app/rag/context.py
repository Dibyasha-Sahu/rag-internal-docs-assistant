def build_context(results):
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    context_parts = []

    for document, metadata in zip(documents, metadatas):
        source = metadata.get("source", "unknown") if metadata else "unknown"
        chunk_id = metadata.get("chunk_id", "unknown") if metadata else "unknown"

        context_parts.append(
            f"[Source: {source} | Chunk: {chunk_id}]\n"
            f"{document}"
        )

    return "\n\n".join(context_parts)