import re


def clean_text(text):
    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Remove trailing whitespace from each line
    text = "\n".join(line.rstrip() for line in text.splitlines())

    # Replace multiple blank lines with a single blank line
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove leading and trailing whitespace
    return text.strip()


def clean_documents(documents):
    cleaned_documents = []

    for document in documents:
        cleaned_documents.append(
            {
                "source": document["source"],
                "content": clean_text(document["content"]),
            }
        )

    return cleaned_documents


if __name__ == "__main__":
    from loader import load_documents

    documents = load_documents()
    cleaned_documents = clean_documents(documents)

    print(f"Cleaned documents: {len(cleaned_documents)}")

    for document in cleaned_documents:
        print(
            f"- {document['source']} "
            f"({len(document['content'])} characters)"
        )