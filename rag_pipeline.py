from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
import os

embeddings = HuggingFaceEmbeddings()
db_path = "vectorstore/faiss_index"
db = FAISS.load_local(db_path, embeddings) if os.path.exists(db_path) else None

async def ingest_document(filename, content):
    global db
    text = content.decode("utf-8")
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = [Document(page_content=chunk) for chunk in splitter.split_text(text)]

    if db:
        db.add_documents(docs)
    else:
        db = FAISS.from_documents(docs, embeddings)
    db.save_local(db_path)

async def process_query(query):
    retriever = db.as_retriever()
    relevant_docs = retriever.get_relevant_documents(query)
    context = "\n".join([doc.page_content for doc in relevant_docs[:3]])
    prompt = f"Answer based on context:\n{context}\n\nQuestion: {query}"
    return f"(Simulated answer): {prompt[:200]}..."
