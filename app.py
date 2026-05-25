import streamlit as st
import requests
import time

# =========================================================
# CONFIG
# =========================================================

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="MultiDocChat",
    page_icon="📄",
    layout="wide"
)

# =========================================================
# SESSION STATE
# =========================================================

if "session_id" not in st.session_state:
    st.session_state.session_id = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if "documents_uploaded" not in st.session_state:
    st.session_state.documents_uploaded = False

# =========================================================
# STREAMING FUNCTION
# =========================================================

def stream_response(response_text):

    for word in response_text.split():

        yield word + " "

        time.sleep(0.03)

# =========================================================
# HEADER
# =========================================================

st.title("📄 Multi Document Chatbot")

st.markdown(
    "Upload documents and chat with your RAG system."
)

st.divider()

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("📂 Upload Documents")

    uploaded_files = st.file_uploader(
        label="Upload PDF / DOCX / TXT",
        type=["pdf", "docx", "txt"],
        accept_multiple_files=True
    )

    if st.button("Upload & Index"):

        if not uploaded_files:

            st.warning(
                "Please upload at least one document."
            )

        else:

            files = []

            for file in uploaded_files:

                files.append(
                    (
                        "files",
                        (
                            file.name,
                            file.getvalue(),
                            file.type
                        )
                    )
                )

            try:

                with st.spinner(
                    "Uploading and indexing documents..."
                ):

                    response = requests.post(
                        f"{API_URL}/upload",
                        files=files
                    )

                if response.status_code == 200:

                    data = response.json()

                    st.session_state.session_id = data["session_id"]

                    st.session_state.documents_uploaded = True

                    st.success(
                        "Documents indexed successfully!"
                    )

                    st.code(
                        st.session_state.session_id,
                        language="text"
                    )

                else:

                    st.error(response.text)

            except requests.exceptions.ConnectionError:

                st.error(
                    "Cannot connect to FastAPI backend.\n"
                    "Make sure uvicorn server is running."
                )

# =========================================================
# CHAT HISTORY
# =========================================================

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

# =========================================================
# CHAT INPUT
# =========================================================

prompt = st.chat_input(
    "Ask a question about your documents..."
)

if prompt:

    if not st.session_state.documents_uploaded:

        st.warning(
            "Please upload documents first."
        )

    else:

        # -------------------------------------------------
        # USER MESSAGE
        # -------------------------------------------------

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):

            st.markdown(prompt)

        # -------------------------------------------------
        # REQUEST PAYLOAD
        # -------------------------------------------------

        payload = {
            "session_id": st.session_state.session_id,
            "message": prompt
        }

        # -------------------------------------------------
        # ASSISTANT RESPONSE
        # -------------------------------------------------

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                try:

                    response = requests.post(
                        f"{API_URL}/chat",
                        json=payload
                    )

                    if response.status_code == 200:

                        answer = response.json()["answer"]

                        full_response = st.write_stream(
                            stream_response(answer)
                        )

                        st.session_state.messages.append(
                            {
                                "role": "assistant",
                                "content": full_response
                            }
                        )

                    else:

                        st.error(response.text)

                except requests.exceptions.ConnectionError:

                    st.error(
                        "Cannot connect to FastAPI backend."
                    )