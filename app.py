import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="MultiDocChat")

st.title("📄 Multi Document Chatbot")

# -------------------------
# Session state
# -------------------------
if "session_id" not in st.session_state:
    st.session_state.session_id = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------
# Upload section
# -------------------------
st.header("Upload Documents")

uploaded_files = st.file_uploader(
    "Upload files",
    accept_multiple_files=True
)

if st.button("Upload & Index"):
    if uploaded_files:

        files = []

        for file in uploaded_files:
            files.append(
                ("files", (file.name, file.getvalue()))
            )

        with st.spinner("Uploading and indexing..."):

            response = requests.post(
                f"{API_URL}/upload",
                files=files
            )

        if response.status_code == 200:

            data = response.json()

            st.session_state.session_id = data["session_id"]

            st.success("Documents indexed successfully!")

            st.write("Session ID:")
            st.code(st.session_state.session_id)

        else:
            st.error(response.text)

# -------------------------
# Chat section
# -------------------------
st.header("Chat")

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask a question")

if prompt:

    if not st.session_state.session_id:
        st.error("Please upload documents first.")

    else:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        payload = {
            "session_id": st.session_state.session_id,
            "message": prompt
        }

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                response = requests.post(
                    f"{API_URL}/chat",
                    json=payload
                )

                if response.status_code == 200:

                    answer = response.json()["answer"]

                    st.markdown(answer)

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer
                        }
                    )

                else:
                    st.error(response.text)