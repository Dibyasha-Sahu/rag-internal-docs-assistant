from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "rag_request_count",
    "Total number of RAG API requests",
)

REQUEST_LATENCY = Histogram(
    "rag_request_latency_seconds",
    "RAG API request latency in seconds",
)

PROMPT_TOKENS = Counter(
    "rag_prompt_tokens",
    "Total number of prompt tokens used by RAG requests",
)

COMPLETION_TOKENS = Counter(
    "rag_completion_tokens",
    "Total number of completion tokens used by RAG requests",
)

TOTAL_TOKENS = Counter(
    "rag_total_tokens",
    "Total number of tokens used by RAG requests",
)