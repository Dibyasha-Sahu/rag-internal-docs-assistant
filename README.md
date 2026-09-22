# RAG Internal Docs Assistant

A production-style Retrieval-Augmented Generation (RAG) application for asking questions about internal technical documentation.

## Current Status

Phase 1 — Project Foundation

The initial FastAPI backend is set up and running successfully.

## Current API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | API information |
| `/health` | GET | Health check |
| `/ready` | GET | Readiness check |
| `/docs` | GET | FastAPI Swagger documentation |

## Technology Stack

- Python
- FastAPI
- Uvicorn
- Git
- GitHub

## Planned Architecture

```text
User
  |
  v
Streamlit UI
  |
  v
NGINX Ingress
  |
  v
FastAPI Backend
  |
  +--> Query Embedding
  |
  +--> ChromaDB
  |
  +--> Top-K Retrieval
  |
  +--> Context Assembly
  |
  +--> LLM
  |
  v
Answer + Citations
Project Goals
Build a RAG-based technical documentation assistant
Retrieve relevant information from internal documents
Generate grounded answers using an LLM
Return source citations with answers
Containerize the application with Docker
Deploy the application on Kubernetes
Package Kubernetes resources using Helm
Implement CI/CD with GitHub Actions
Add monitoring using Prometheus and Grafana
Security

Sensitive credentials will not be committed to the repository.

Use .env.example as the configuration template.

Development

Create and activate a Python virtual environment before installing dependencies.

Install dependencies:

pip install -r requirements.txt

Run the FastAPI application:

uvicorn app.main:app --reload

Open the API documentation:

http://127.0.0.1:8000/docs





