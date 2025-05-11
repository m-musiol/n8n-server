from fastapi import FastAPI
import chromadb

app = FastAPI()

client = chromadb.Client()  # lokaler HTTP-Client (Start erfolgt unten)
collection = client.get_or_create_collection(name="vertraege")

@app.get("/")
def root():
    return {"message": "Chroma API läuft"}

@app.post("/add")
def add_document(id: str, text: str):
    collection.add(documents=[text], ids=[id])
    return {"status": "ok"}

@app.get("/search")
def search(query: str):
    result = collection.query(query_texts=[query], n_results=3)
    return result
