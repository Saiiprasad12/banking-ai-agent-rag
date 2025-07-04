from fastapi import FastAPI, UploadFile, File
from backend.rag_pipeline import process_query, ingest_document
import asyncio

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Banking AI Agent is live."}

@app.post("/query")
async def query_llm(payload: dict):
    question = payload.get("question")
    if not question:
        return {"error": "Missing 'question' in request."}
    answer = await process_query(question)
    return {"answer": answer}

@app.post("/upload")
async def upload_doc(file: UploadFile = File(...)):
    content = await file.read()
    await ingest_document(file.filename, content)
    return {"status": f"{file.filename} ingested"}
