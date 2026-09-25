def chunk_text(text, chunk_size=800, chunk_overlap=100):
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if chunk_overlap < 0:
        raise ValueError("chunk_overlap cannot be negative")

    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size")

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end >= len(text):
            break

        start = end - chunk_overlap

    return chunks


def chunk_documents(documents, chunk_size=800, chunk_overlap=100):
    chunked_documents = []

    for document in documents:
        chunks = chunk_text(
            document["content"],
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

        for index, chunk in enumerate(chunks):
            chunked_documents.append(
                {
                    "source": document["source"],
                    "chunk_id": index,
                    "content": chunk,
                }
            )

    return chunked_documents


if __name__ == "__main__":
    from cleaner import clean_documents
    from loader import load_documents

    documents = load_documents()
    cleaned_documents = clean_documents(documents)

    chunked_documents = chunk_documents(
        cleaned_documents,
        chunk_size=800,
        chunk_overlap=100,
    )

    print(f"Created chunks: {len(chunked_documents)}")

    for chunk in chunked_documents[:5]:
        print(
            f"- {chunk['source']} "
            f"| chunk_id={chunk['chunk_id']} "
            f"| characters={len(chunk['content'])}"
        )