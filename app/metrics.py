from prometheus_client import Counter, Histogram


REQUEST_COUNT = Counter(
    "rag_request_count",
    "Total number of RAG API requests",
)

REQUEST_LATENCY = Histogram(
    "rag_request_latency_seconds",
    "RAG API request latency in seconds",
)