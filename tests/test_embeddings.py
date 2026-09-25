from app.rag.embeddings import embed_text


def test_embed_text_returns_list():
    embedding = embed_text("What is Kubernetes?")

    assert isinstance(embedding, list)


def test_embed_text_returns_384_dimensions():
    embedding = embed_text("What is Docker?")

    assert len(embedding) == 384


def test_embed_text_contains_numeric_values():
    embedding = embed_text("What is GitHub Actions?")

    assert all(
        isinstance(value, (int, float))
        for value in embedding
    )


def test_different_text_produces_valid_embeddings():
    first_embedding = embed_text("What is Kubernetes?")
    second_embedding = embed_text("What is Docker?")

    assert len(first_embedding) == 384
    assert len(second_embedding) == 384
    assert first_embedding != second_embedding