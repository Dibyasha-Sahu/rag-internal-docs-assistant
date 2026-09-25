from app.rag.context import build_context


def test_build_context_includes_document_content():
    results = {
        "documents": [
            [
                "Kubernetes is a container orchestration platform."
            ]
        ],
        "metadatas": [
            [
                {
                    "source": "documents/kubernetes/kubernetes-basics.md",
                    "chunk_id": 0,
                }
            ]
        ],
    }

    context = build_context(results)

    assert "Kubernetes is a container orchestration platform." in context


def test_build_context_includes_source_and_chunk():
    results = {
        "documents": [
            ["Docker packages applications into containers."]
        ],
        "metadatas": [
            [
                {
                    "source": "documents/docker/docker-basics.md",
                    "chunk_id": 2,
                }
            ]
        ],
    }

    context = build_context(results)

    assert "documents/docker/docker-basics.md" in context
    assert "Chunk: 2" in context


def test_build_context_handles_multiple_results():
    results = {
        "documents": [
            [
                "First document content.",
                "Second document content.",
            ]
        ],
        "metadatas": [
            [
                {
                    "source": "documents/test1.md",
                    "chunk_id": 0,
                },
                {
                    "source": "documents/test2.md",
                    "chunk_id": 1,
                },
            ]
        ],
    }

    context = build_context(results)

    assert "First document content." in context
    assert "Second document content." in context
    assert "documents/test1.md" in context
    assert "documents/test2.md" in context


def test_build_context_handles_empty_results():
    results = {
        "documents": [[]],
        "metadatas": [[]],
    }

    context = build_context(results)

    assert context == ""