import time

from fastapi import APIRouter, Depends
from fastapi.responses import Response
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

from app.auth import verify_api_key
from app.metrics import REQUEST_COUNT, REQUEST_LATENCY
from app.rag.context import build_context
from app.rag.generator import generate_answer
from app.rag.retriever import retrieve_documents
from app.rate_limit import rate_limit
from app.schemas.query import QueryRequest, QueryResponse

router = APIRouter()


@router.post(
    "/query",
    response_model=QueryResponse,
    dependencies=[
        Depends(verify_api_key),
        Depends(rate_limit),
    ],
)
def query_documents(request: QueryRequest):
    start_time = time.time()

    results = retrieve_documents(request.question, top_k=3)

    context = build_context(results)

    generated = generate_answer(
        request.question,
        context,
    )

    sources = []

    metadatas = results.get("metadatas", [[]])[0]

    for metadata in metadatas:
        if metadata:
            sources.append(
                {
                    "document": metadata.get("source", "unknown"),
                    "chunk": metadata.get("chunk_id", -1),
                }
            )

    REQUEST_COUNT.inc()

    REQUEST_LATENCY.observe(
        time.time() - start_time
    )

    return QueryResponse(
        answer=generated["answer"],
        sources=sources,
    )


@router.get("/metrics")
def metrics():
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )