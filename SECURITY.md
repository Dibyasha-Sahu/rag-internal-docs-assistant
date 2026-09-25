# Security Notes

## Dependency Security

### ChromaDB 1.5.9

`pip-audit` currently reports known vulnerabilities affecting
`chromadb==1.5.9`.

At the time of this review, ChromaDB 1.5.9 is the latest stable
version available from PyPI, so the project does not downgrade to
an older release or install an unreleased development version.

## Current Architecture

The application uses:

- `chromadb.PersistentClient`
- A local persistent `chroma_db` directory
- No separate ChromaDB HTTP server
- No `chromadb.HttpClient`
- No exposed ChromaDB network port
- No use of `trust_remote_code` in the application code

The Docker Compose deployment exposes only:

- FastAPI on port 8000
- Streamlit on port 8501

ChromaDB is embedded within the application process and its persistent
database is stored locally.

## Current Mitigation

The application does not deploy a standalone ChromaDB server or expose
ChromaDB directly to the network.

The dependency vulnerability remains tracked because the installed
ChromaDB version is reported by `pip-audit`.

The dependency should be re-evaluated when an upstream stable release
containing the relevant security fixes becomes available.

## Security Validation

### Dependency Audit

The dependency security audit is performed using:

```text
pip-audit -r requirements.txt