# 📄 MultiDocChat: Conversational Multi-Document RAG System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge\&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge\&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge\&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-RAG_Framework-1C3C3C?style=for-the-badge)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-orange?style=for-the-badge)
![OpenAI](https://img.shields.io/badge/OpenAI-LLM-412991?style=for-the-badge\&logo=openai)
![Gemini](https://img.shields.io/badge/Gemini-Embeddings-4285F4?style=for-the-badge\&logo=google)
![LangSmith](https://img.shields.io/badge/LangSmith-Evaluation-000000?style=for-the-badge)

</div>

---

# 🚀 Overview

MultiDocChat is a low-latency conversational Retrieval-Augmented Generation (RAG) system designed for querying multiple uploaded documents using semantic retrieval and LLM-based reasoning.

The system supports:

* 📂 Multi-document upload and indexing
* 🧠 Conversational memory across chat sessions
* 🔍 Semantic retrieval using Gemini embeddings
* ⚡ FAISS vector indexing with MMR retrieval
* 💬 OpenAI LLM powered responses
* 📊 LangSmith tracing and evaluation
* 🌐 FastAPI backend with Streamlit frontend
* ⚡ End-to-end latency below 3 seconds

---

# 🎯 Objectives

* Build a conversational multi-document RAG system with low inference latency.
* Enable semantic search across uploaded documents using vector retrieval.
* Support coherent multi-turn conversations with session-aware memory.
* Develop scalable backend APIs using FastAPI.
* Evaluate retrieval and generation quality using LangSmith.

---

# 🏗️ System Architecture

```text
                ┌─────────────────────┐
                │     Streamlit UI    │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │      FastAPI        │
                │   REST Endpoints    │
                └─────────┬───────────┘
                          │
          ┌───────────────┼────────────────┐
          ▼                                ▼
 ┌─────────────────┐              ┌─────────────────┐
 │ Document Upload │              │  Chat Endpoint  │
 └────────┬────────┘              └────────┬────────┘
          │                                 │
          ▼                                 ▼
 ┌─────────────────┐              ┌─────────────────┐
 │ Text Chunking   │              │ Conversational  │
 │ Recursive Split │              │ Memory Handling │
 └────────┬────────┘              └────────┬────────┘
          │                                 │
          ▼                                 ▼
 ┌─────────────────┐              ┌─────────────────┐
 │ Gemini Embedding│              │ FAISS Retriever │
 └────────┬────────┘              └────────┬────────┘
          │                                 │
          └──────────────┬──────────────────┘
                         ▼
                ┌─────────────────┐
                │ OpenAI LLM      │
                │ Response Engine │
                └─────────────────┘
```

---

# 🧠 Tech Stack

| Component       | Technology             |
| --------------- | ---------------------- |
| Backend         | FastAPI                |
| Frontend        | Streamlit              |
| RAG Framework   | LangChain              |
| Embedding Model | Gemini Embedding Model |
| LLM             | OpenAI                 |
| Vector Database | FAISS                  |
| Evaluation      | LangSmith              |
| Language        | Python                 |
| API Server      | Uvicorn                |

---

# ✨ Features

## 📂 Multi-Document Upload

* Upload multiple PDF/TXT/DOC files.
* Session-based document handling.
* Separate FAISS indexes per session.

---

## 🔍 Semantic Retrieval

* Gemini embedding generation.
* FAISS vector similarity search.
* MMR (Maximum Marginal Relevance) retrieval.
* Context-aware chunk retrieval.

---

## 💬 Conversational Chat

* Multi-turn conversations.
* Session-aware memory.
* Chat history integration.
* Context-grounded responses.

---

## ⚡ Low Latency

* Fast vector retrieval.
* Optimized chunking pipeline.
* Sub-3-second response latency.

---

## 📊 Evaluation & Monitoring

* LangSmith tracing.
* RAG pipeline observability.
* Response quality monitoring.
* Debugging and evaluation support.

---

# 📁 Project Structure

```text
MultiDocChat/
│
├── main.py
├── streamlit_app.py
├── requirements.txt
├── .env
├── config/
│   └── config.yaml
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── app.js
│
├── data/
│   └── session_files/
│
├── faiss_index/
│   └── session_indexes/
│
├── src/
│   ├── document_ingestion/
│   │   └── data_ingestion.py
│   │
│   ├── document_chat/
│   │   └── retrieval.py
│   │
│   ├── utils/
│   └── exception/
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/MultiDocChat.git
cd MultiDocChat
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / Mac

```bash
source .venv/bin/activate
```

---

# 📦 Required Packages

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🧾 requirements.txt

```txt
fastapi
uvicorn
streamlit
langchain
langchain-community
langchain-openai
langchain-google-genai
langsmith
faiss-cpu
pydantic
jinja2
python-multipart
python-dotenv
pypdf
requests
numpy
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_gemini_key
LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=MultiDocChat
```

---

# ▶️ Running FastAPI Backend

```bash
uvicorn main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# ▶️ Running Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

Frontend runs at:

```text
http://localhost:8501
```

---

# 🔄 RAG Pipeline Workflow

```text
Upload Documents
       ↓
Document Loading
       ↓
Text Chunking
       ↓
Gemini Embedding Generation
       ↓
FAISS Vector Indexing
       ↓
MMR Retrieval
       ↓
OpenAI LLM Response Generation
       ↓
Streamlit Chat Interface
```

---

# 🧩 API Endpoints

## 🩺 Health Check

```http
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

---

## 📂 Upload Documents

```http
POST /upload
```

Returns:

```json
{
  "session_id": "session_123",
  "indexed": true,
  "message": "Indexing complete with MMR"
}
```

---

## 💬 Chat Endpoint

```http
POST /chat
```

Request:

```json
{
  "session_id": "session_123",
  "message": "Summarize the report"
}
```

Response:

```json
{
  "answer": "Generated response here"
}
```

---

# 🧠 Core Components

## 🔹 FastAPI Backend

Responsible for:

* API endpoints
* Session handling
* Document upload
* Retriever loading
* LLM orchestration

---

## 🔹 Streamlit Frontend

Responsible for:

* File uploads
* Chat interface
* Session management
* Displaying responses

---

## 🔹 FAISS Vector Store

Responsible for:

* Storing embeddings
* Fast similarity search
* Efficient retrieval

---

## 🔹 LangChain

Responsible for:

* RAG orchestration
* Prompt chaining
* Retriever pipeline
* Conversational memory

---

## 🔹 LangSmith

Responsible for:

* Tracing
* Evaluation
* Debugging
* Monitoring

---

# 📈 Performance

| Metric            | Value       |
| ----------------- | ----------- |
| Average Latency   | < 3 seconds |
| Retrieval Method  | MMR         |
| Embedding Model   | Gemini      |
| Vector Database   | FAISS       |
| Conversation Type | Multi-turn  |


# 🛠️ Future Improvements

* Add hybrid retrieval (BM25 + Vector Search)
* Add citation-aware responses
* Add authentication system
* Add Redis/PostgreSQL memory persistence
* Add Docker deployment
* Add Kubernetes scaling
  
---

# ⭐ If you found this useful, give the repository a star!
