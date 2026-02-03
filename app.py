from fastapi import FastAPI
import chromadb
import ollama

app = FastAPI()
chroma_client = chromadb.PersistentClient(path="./db")
collection = chroma_client.get_or_create_collection("docs")

#  Connect to the Ollama server running in the Docker container
# ollama_client = ollama.Client(host="http://host.docker.internal:11434") 


@app.post("/query")
def query(q: str):
    results = collection.query(query_texts=[q], n_results=1)
    context = results["documents"][0][0] if results["documents"] else ""

    answer = ollama.generate( # Update to Ollama Client when using Docker
        model = "tinyllama",
        prompt = f"Context:\n{context}\n\nQuestion: {q}\n\nAnswer clearly and concisely:"
    )

    return {"answer": answer["response"]}

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/add")
def add_knowledge(text: str):
    try:
        import uuid
        doc_id = str(uuid.uuid4())

        collection.add(documents=[text], ids=[doc_id]) # Add the text to the Chroma collection
        
        return {"status": "success", "message": "Content added to knowledge base successfully", "id": doc_id}
    except Exception as e:
        return {"status": "error", "message": str(e)}