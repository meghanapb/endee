Endee RAG Document Search System

Endee RAG Document Search is a lightweight Retrieval-Augmented Generation (RAG) pipeline built using Endee OSS (nD) as the vector database.
This project demonstrates semantic search, embedding storage, and context-based answer generation using vector similarity.

1. System Overview

This project implements a complete RAG workflow:

Convert documents into embeddings (384 dimensions)

Store embeddings inside Endee vector database

Retrieve relevant documents using cosine similarity

Generate answers grounded in retrieved context

This is a working example of Retrieval-Augmented Generation — not just vector search.

2. Architecture
User Question
      ↓
Embedding Generation
      ↓
Endee Vector Search (Cosine Similarity)
      ↓
Top-K Retrieval
      ↓
Context-Based Answer Generation

3. Project Structure
rag-doc-search/
│
├── docs.txt                # Source knowledge base
│
├── src/
│   ├── embed.py            # Text → Embedding
│   ├── ingest.py           # Insert documents into Endee
│   ├── query.py            # Test similarity search
│   └── rag_pipeline.py     # Full interactive RAG system
│
└── README.md

4. Requirements
Software

Python 3.10+

Docker

Endee OSS (running on port 8080)

Python Dependencies
pip install requests sentence-transformers msgpack

5. Running Endee
Option 1 — Docker (Recommended)
docker run -p 8080:8080 endee-oss:latest


Verify:

Invoke-RestMethod http://localhost:8080/api/v1/index/list

6. Create Vector Index

Create a cosine similarity index (384 dimensions)

7. Ingest Documents

Ensure docs.txt contains one document per line.

Run:

python -m src.ingest


Verify ingestion:

Invoke-RestMethod http://localhost:8080/api/v1/index/list


8. Test Vector Search
python -m src.query

Expected Output:

Status Code: 200

Similarity Score

Retrieved Document Content

9. Run Full RAG Pipeline (Interactive Mode)
python -m src.rag_pipeline


Example:
Endee RAG System Ready
Type 'exit' to quit.

Ask a question: What is RAG?

Question:
What is RAG?

Answer based on retrieved documents:
RAG stands for Retrieval Augmented Generation.

10. Features Implemented

384-dimensional embeddings

Cosine similarity search

HNSW-based vector indexing (via Endee)

Metadata storage

Interactive RAG interface

Docker-based vector database deployment

11. Key Concepts Demonstrated

Retrieval Augmented Generation (RAG)

Embedding-based search

Nearest neighbor search

Vector indexing

Semantic search vs keyword search

REST API communication

12. Limitations

Uses mock generation (no LLM integration yet)

No document chunking

No similarity threshold filtering

Basic CLI interface only

13. Future Improvements

Add OpenAI / Llama / Local LLM integration

Add document chunking pipeline

Add similarity threshold filtering

Add Streamlit UI

Add PDF ingestion support

Deploy on cloud
