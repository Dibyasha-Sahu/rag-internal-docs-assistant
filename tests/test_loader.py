from ingestion.loader import load_documents


def test_load_documents_returns_documents():
    documents = load_documents()

    assert len(documents) == 4


def test_loaded_documents_have_required_fields():
    documents = load_documents()

    for document in documents:
        assert "source" in document
        assert "content" in document
        assert document["source"].endswith(".md")
        assert document["content"]


def test_expected_document_categories_are_loaded():
    documents = load_documents()

    sources = [document["source"] for document in documents]

    assert any("devops" in source for source in sources)
    assert any("docker" in source for source in sources)
    assert any("github-actions" in source for source in sources)
    assert any("kubernetes" in source for source in sources)