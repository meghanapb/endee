# 🔍 Endee RAG Document Search System

A lightweight **Retrieval-Augmented Generation (RAG)** pipeline powered by **Endee OSS (nD)** vector database. This project demonstrates semantic search, embedding storage, and context-grounded answer generation.

---

## 📖 System Overview
This project implements a complete RAG workflow:
1.  **Embedding**: Converts documents into 384-dimensional vectors.
2.  **Storage**: Persists embeddings within the Endee Vector Database.
3.  **Retrieval**: Uses Cosine Similarity to find relevant context.
4.  **Generation**: Produces answers grounded strictly in retrieved data.

---


## 📂 Project Structure
```text
rag-doc-search/
├── docs.txt             # Source knowledge base
├── src/
│   ├── embed.py         # Text → Embedding logic
│   ├── ingest.py        # Document insertion into Endee
│   ├── query.py         # Similarity search testing
│   └── rag_pipeline.py  # Full interactive RAG interface
└── README.md
``` 


## 🛠️ Requirements & Setup
Software
Python: 3.10+
Docker: For running Endee OSS
Endee OSS: Running on port 8080
1. Run Endee Database (Docker)
      docker run -p 8080:8080 endee-oss:latest

2. Install Dependencies
      pip install requests sentence-transformers msgpack

## 🚀 Execution Guide
Step 1: Ingest Documents
Ensure docs.txt has your content (one document per line), then run:
      python -m src.ingest

Step 2: Test Vector Search
Verify the similarity scores and retrieved content:
      python -m src.query

Step 3: Run Interactive RAG
Start the full pipeline to ask questions against your data:
      python -m src.rag_pipeline


## ✨ Features
High-Dimensional Embeddings: 384-dimensional vector support.
Optimized Search: HNSW-based vector indexing via Endee.
Metric: Cosine similarity for accurate semantic matching.
Deployment: Docker-based vector database deployment.

## 🚧 Limitations & Roadmap
-- Current Limitations
1. Uses mock generation (no LLM integration yet)
2. No document chunking
3. No similarity threshold filtering
4. CLI-based interface only
5. No production-grade authentication handling

-- Future Improvements
1. Integrate OpenAI / Llama / Local LLMs.
2. Implement recursive character text splitting (chunking).
3. Build a Streamlit UI for web-based interaction.
4. Add PDF and Markdown ingestion support.
