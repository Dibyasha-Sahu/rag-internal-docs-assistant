from app.schemas.query import QueryRequest, QueryResponse, Source


def test_query_request_accepts_question():
    request = QueryRequest(
        question="What is Kubernetes?"
    )

    assert request.question == "What is Kubernetes?"


def test_source_accepts_document_and_chunk():
    source = Source(
        document="documents/kubernetes/kubernetes-basics.md",
        chunk=2,
    )

    assert source.document == "documents/kubernetes/kubernetes-basics.md"
    assert source.chunk == 2


def test_query_response_accepts_answer_and_sources():
    response = QueryResponse(
        answer="Kubernetes is a container orchestration platform.",
        sources=[
            Source(
                document="documents/kubernetes/kubernetes-basics.md",
                chunk=0,
            )
        ],
    )

    assert response.answer == "Kubernetes is a container orchestration platform."
    assert len(response.sources) == 1
    assert response.sources[0].chunk == 0