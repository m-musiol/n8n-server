import chromadb

client = chromadb.HttpClient(host="127.0.0.1", port=8001)
collection = client.get_collection("pdf_texts")

results = collection.query(
    query_texts=["floppy disk"],
    n_results=3
)

for doc, dist in zip(results["documents"], results["distances"]):
    print("📄 Dokument:", doc)
    print("📏 Ähnlichkeit:", dist)
    print("-" * 40)
