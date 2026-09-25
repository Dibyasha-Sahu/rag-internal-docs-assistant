import os

import requests
import streamlit as st
from dotenv import load_dotenv


load_dotenv()


API_URL = "http://api:8000/query"
API_KEY = os.getenv("API_KEY")


st.set_page_config(
    page_title="RAG Internal Docs Assistant",
    page_icon="📚",
    layout="centered",
)


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:
    st.title("📚 RAG Assistant")

    st.write(
        "Internal technical documentation "
        "question-answering system."
    )

    st.divider()

    st.subheader("Project Stack")

    st.write("• Streamlit")
    st.write("• FastAPI")
    st.write("• Sentence Transformers")
    st.write("• ChromaDB")
    st.write("• Groq LLM")

    st.divider()

    st.caption("RAG Internal Docs Assistant")
    st.caption("Phase 6 — Streamlit UI")


# -----------------------------
# Main UI
# -----------------------------

st.title("📚 RAG Internal Docs Assistant")

st.write(
    "Ask questions about the internal technical "
    "documentation and get answers with document sources."
)


question = st.text_input(
    "Enter your question",
    placeholder="e.g. What is Kubernetes?",
)


ask_button = st.button(
    "🔍 Ask Question",
    use_container_width=True,
)


if ask_button:

    if not question.strip():
        st.warning("Please enter a question.")

    elif not API_KEY:
        st.error("API key is not configured.")

    else:

        try:

            with st.spinner(
                "Searching documentation and generating answer..."
            ):

                response = requests.post(
                    API_URL,
                    headers={
                        "X-API-Key": API_KEY,
                    },
                    json={
                        "question": question,
                    },
                    timeout=60,
                )

            if response.status_code == 200:

                data = response.json()

                st.divider()

                st.subheader("💡 Answer")

                st.write(data["answer"])

                st.divider()

                st.subheader("📚 Sources")

                sources = data.get("sources", [])

                if sources:

                    for index, source in enumerate(
                        sources,
                        start=1,
                    ):

                        document = source.get(
                            "document",
                            "unknown",
                        )

                        chunk = source.get(
                            "chunk",
                            "unknown",
                        )

                        with st.expander(
                            f"Source {index}: {document}"
                        ):

                            st.write(
                                f"**Document:** {document}"
                            )

                            st.write(
                                f"**Chunk:** {chunk}"
                            )

                else:

                    st.info(
                        "No source information was returned."
                    )

            elif response.status_code == 401:

                st.error(
                    "Authentication failed. "
                    "Check the API key configuration."
                )

            elif response.status_code == 429:

                st.warning(
                    "Rate limit exceeded. "
                    "Please try again later."
                )

            else:

                st.error(
                    f"API request failed "
                    f"with status code "
                    f"{response.status_code}"
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "Could not connect to the FastAPI backend. "
                "Make sure FastAPI is running on port 8000."
            )

        except requests.exceptions.Timeout:

            st.error(
                "The request timed out. "
                "Please try again."
            )

        except Exception as error:

            st.error(
                f"Unexpected error: {error}"
            )