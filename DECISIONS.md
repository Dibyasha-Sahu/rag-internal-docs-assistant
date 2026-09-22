# Architecture & Technical Decisions

This document records important technical decisions made during the development of the RAG Internal Docs Assistant.

## 1. Backend Framework

**Decision:** FastAPI

**Reason:**
FastAPI provides a lightweight, modern Python framework for building REST APIs and automatically provides OpenAPI/Swagger documentation.

---

## 2. RAG Architecture

**Decision:** Retrieval-Augmented Generation (RAG)

**Reason:**
The assistant should answer questions using the project's internal technical documentation instead of relying only on the language model's general knowledge.

The RAG flow will be:

```text
User Question
      |
      v
Query Embedding
      |
      v
ChromaDB
      |
      v
Top-K Relevant Chunks
      |
      v
Context Assembly
      |
      v
LLM
      |
      v
Answer + Citations
3. Vector Database

Decision: ChromaDB

Reason:
ChromaDB provides a simple local vector database suitable for storing document embeddings and performing similarity-based retrieval during development.

4. Embeddings

Decision: Sentence Transformers

Reason:
Sentence-transformers will be used to convert documents and user questions into vector embeddings for semantic retrieval.

5. User Interface

Decision: Streamlit

Reason:
Streamlit provides a simple way to build a professional interactive interface for the RAG assistant without introducing unnecessary frontend complexity.

6. Containerization

Decision: Docker

Reason:
Docker provides consistent application environments and makes the application easier to test, deploy, and run across different systems.

7. Kubernetes

Decision: Kubernetes with kind for local deployment

Reason:
The project is intended to demonstrate practical Kubernetes deployment skills while keeping the infrastructure local and resource-efficient.

8. Kubernetes Packaging

Decision: Helm

Reason:
Helm will package the Kubernetes manifests and make application configuration easier to manage.

9. CI/CD

Decision: GitHub Actions

Reason:
GitHub Actions will automate testing, security validation, Docker image building, and container image publishing.

10. Observability

Decision: Prometheus and Grafana

Reason:
Prometheus will collect application metrics and Grafana will provide dashboards for monitoring the application.

11. Security

Decision: Do not commit secrets to Git

Sensitive credentials such as LLM API keys will be stored outside the repository.

The repository will contain .env.example with placeholder configuration values.



