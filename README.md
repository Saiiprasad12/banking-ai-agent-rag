# 🧠 Banking AI Agent with RAG & LangChain

An end-to-end AI/ML project for a **banking client**, demonstrating how to use **LangChain agents**, **RAG pipelines**, and **FastAPI** for document-based automation. This system allows intelligent querying over policy documents and enables workflow automation using containerized services.

---

## 🚀 Features

- 🤖 LangChain-powered AI agents for process automation
- 📄 Custom Retrieval-Augmented Generation (RAG) for document querying
- ⚡ FastAPI backend with asynchronous support
- 🐳 Dockerized services and scalable deployment
- ⏱️ Airflow DAG for scheduled document ingestion
- 📊 OpenTelemetry-integrated observability
- 🔌 Java-compatible modular backend architecture

---

## 📁 Project Structure

```bash
banking-ai-agent-rag/
├── README.md
├── requirements.txt
├── .gitignore
├── backend/
│   ├── main.py              # FastAPI app
│   ├── agent.py             # LangChain agent setup
│   └── rag_pipeline.py      # RAG processing logic
├── airflow/
│   └── dag_load_docs.py     # Airflow DAG to ingest documents
├── docker/
│   └── Dockerfile           # Backend Docker container
├── data/
│   └── sample_policy.txt    # Sample policy document

