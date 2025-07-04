from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def ingest():
    from backend.rag_pipeline import ingest_document
    with open("data/sample_policy.txt", "rb") as f:
        content = f.read()
    import asyncio
    asyncio.run(ingest_document("sample_policy.txt", content))

with DAG("doc_ingestion_dag", start_date=datetime(2023, 1, 1), schedule_interval="@daily", catchup=False) as dag:
    PythonOperator(task_id="ingest_docs", python_callable=ingest)
