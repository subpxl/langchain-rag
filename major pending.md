Retrieval & Prompt Core

Retrieval evaluation

Prompt versioning

Citation grounding

Explicit hallucination prohibition

Force “I don’t know” on missing context

Limit verbosity

Ingestion & Storage

Persistent vector store

Document metadata (source, id, timestamp)

Deduplication or controlled re-ingestion

Clear ingestion command or API

Tuned chunking (400–800 chars, 10–20% overlap)

Tuned retrieval k (3–5)

Basic metadata filtering

Session Memory

Per-session memory only (no global memory)

Memory window limit

Reset endpoint

Logging & Observability

Log question

Log retrieved document IDs

Log latency

Log final answer

Log errors

Store logs to file or database

Evaluation & Testing

20–50 test questions with expected answers

Measure retrieval hit rate

Measure “I don’t know” rate

Track hallucinations

Regression tests

Retrieval Quality (Post-MVP)

Reranking

Hybrid search

API Hardening

API key authentication

Rate limiting

Async endpoints

Health endpoint (/health)

Proper error responses

Timeout handling

Input length limits

Prompt injection guards

Deployment

Dockerized API

Environment variable configuration

Health checks

Simple restart strategy

UX (Minimal but Complete)

Return citations

Show sources

Return confidence score (simple heuristic)

Feedback endpoint