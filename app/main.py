from fastapi import FastAPI

app = FastAPI(
    title="RAG Internal Docs Assistant",
    description="RAG-based assistant for internal technical documentation",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "RAG Internal Docs Assistant API",
        "status": "running",
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    } 

@app.get("/ready")
def ready():
    return {
        "status": "ready"
    }       