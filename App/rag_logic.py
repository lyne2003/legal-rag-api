import json

# Load preprocessed data
with open("embedded_chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

def search_chunks(query):
    return [c for c in chunks if query.lower() in c["chunk"].lower()][:5]
