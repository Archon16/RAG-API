# 🚀 RAG API – Production-Grade DevOps & AI Project

> **A real-world Retrieval Augmented Generation (RAG) API built with production DevOps practices**  
> Covers API design, vector databases, containerization, Kubernetes deployment, and CI pipelines for AI systems.

---

## 🔥 Why This Project Stands Out

Most AI demos stop at *“it works locally.”*  
This project goes further and focuses on **production concerns**:

- ✅ Deterministic CI testing for non-deterministic LLM outputs  
- ✅ Containerized AI workloads using Docker  
- ✅ Kubernetes deployment with self-healing and service networking  
- ✅ CI pipelines that protect **data quality**, not just code quality  

This mirrors how **real companies ship AI-backed APIs**.

---

## 🧠 What This API Does

This is a **Retrieval Augmented Generation (RAG) API** that:

1. Accepts a user query via REST API  
2. Retrieves relevant context from a **vector database (ChromaDB)**  
3. Augments the prompt with retrieved knowledge  
4. Generates an answer using a **local LLM (Ollama – tinyllama)**  
5. Returns a grounded, context-aware response  

---

## 🏗 High-Level Architecture

Client
↓
FastAPI (/query)
↓
ChromaDB (Vector Search)
↓
Context + Query
↓
Ollama (LLM)
↓
Response


### CI Flow for AI Reliability

Git Push
↓
GitHub Actions
↓
Mock LLM Mode
↓
Semantic Tests
↓
Fail Build if Knowledge Quality Drops


---

## 🛠 Tech Stack

| Layer | Technology |
|-----|-----------|
| API | FastAPI, Python, Uvicorn |
| AI / RAG | Ollama (tinyllama), ChromaDB |
| Containers | Docker |
| Orchestration | Kubernetes (Minikube) |
| CI/CD | GitHub Actions |
| Testing | Semantic tests with mocked LLM |

---

## 📂 Repository Structure

├── app.py
├── embed.py
├── docs/
├── db/
├── semantic_test.py
├── Dockerfile
├── deployment.yaml
├── service.yaml
└── .github/workflows/
└── ci.yaml


---

## ⚡ Quick Start (Local – No Docker)

### Prerequisites
- Python 3.10+
- Ollama installed
- tinyllama model

bash - ```ollama pull tinyllama```

# Setup & Run

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload

# Test the API

POST http://127.0.0.1:8000/query?q=What is Kubernetes?

# 📄 Swagger UI:

http://127.0.0.1:8000/docs

# 🐳 Run with Docker

docker build -t rag-api .
docker run -p 8000:8000 rag-api

Or pull from Docker Hub:

docker pull archon16/rag-api-app:latest
docker run -p 8000:8000 archon16/rag-api-app:latest

# ☸️ Deploy to Kubernetes (Minikube)

minikube start
eval $(minikube docker-env)
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

## Access the service:

minikube service rag-app-service

# Kubernetes Features Demonstrated

Deployments & Pods
NodePort Services
Label selectors & traffic routing
Self-healing (ReplicaSet recreation)

# 🔁 CI/CD for AI Systems (Key Highlight)

## Problem
LLM outputs are non-deterministic, causing flaky CI tests.

## Solution Implemented
- Added Mock LLM Mode for CI
- Semantic tests validate meaning, not exact text
- CI fails when required concepts are missing from the knowledge base
- This ensures bad data never reaches production.

# 🧪 Semantic Testing Example
✔ Response contains required concept: "orchestration"
✖ Fail build if missing

# 📌 Key Learnings

- Designing RAG systems end-to-end
- Making AI systems testable in CI pipelines
- Containerizing and orchestrating AI APIs
- Applying DevOps best practices to ML/AI workloads
