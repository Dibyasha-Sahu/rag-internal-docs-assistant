from ingestion.cleaner import clean_documents, clean_text


def test_clean_text_removes_extra_whitespace():
    text = "Hello\r\n\r\n\r\nWorld   "

    result = clean_text(text)

    assert result == "Hello\n\nWorld"


def test_clean_text_removes_leading_and_trailing_whitespace():
    text = "   Hello World   "

    result = clean_text(text)

    assert result == "Hello World"


def test_clean_documents_preserves_source():
    documents = [
        {
            "source": "documents/test.md",
            "content": "  Hello World  ",
        }
    ]

    result = clean_documents(documents)

    assert result[0]["source"] == "documents/test.md"
    assert result[0]["content"] == "Hello World"