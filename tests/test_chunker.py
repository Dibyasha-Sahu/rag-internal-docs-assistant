from ingestion.chunker import chunk_documents, chunk_text


def test_chunk_text_creates_expected_chunks():
    text = "abcdefghijklmnopqrstuvwxyz"

    chunks = chunk_text(
        text,
        chunk_size=10,
        chunk_overlap=2,
    )

    assert chunks == [
        "abcdefghij",
        "ijklmnopqr",
        "qrstuvwxyz",
    ]


def test_chunk_text_rejects_invalid_chunk_size():
    try:
        chunk_text("hello", chunk_size=0)
        assert False
    except ValueError as error:
        assert str(error) == "chunk_size must be greater than 0"


def test_chunk_text_rejects_invalid_overlap():
    try:
        chunk_text(
            "hello",
            chunk_size=10,
            chunk_overlap=10,
        )
        assert False
    except ValueError as error:
        assert str(error) == "chunk_overlap must be smaller than chunk_size"


def test_chunk_documents_preserves_metadata():
    documents = [
        {
            "source": "documents/test.md",
            "content": "abcdefghijklmnopqrstuvwxyz",
        }
    ]

    chunks = chunk_documents(
        documents,
        chunk_size=10,
        chunk_overlap=2,
    )

    assert chunks[0]["source"] == "documents/test.md"
    assert chunks[0]["chunk_id"] == 0
    assert chunks[0]["content"] == "abcdefghij"