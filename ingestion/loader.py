from pathlib import Path

DOCUMENTS_DIR = Path("documents")


def load_documents():
    documents = []

    for file_path in DOCUMENTS_DIR.rglob("*.md"):
        content = file_path.read_text(encoding="utf-8")

        documents.append(
            {
                "source": str(file_path),
                "content": content,
            }
        )

    return documents


if __name__ == "__main__":
    documents = load_documents()

    print(f"Loaded documents: {len(documents)}")

    for document in documents:
        print(f"- {document['source']}")