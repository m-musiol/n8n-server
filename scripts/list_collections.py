import chromadb

client = chromadb.HttpClient(host="127.0.0.1", port=8001)
collections = client.list_collections()

for c in collections:
    print("🗂️ Collection:", c.name)
