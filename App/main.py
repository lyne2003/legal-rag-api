from fastapi import FastAPI, Query
from rag_logic import search_chunks

app = FastAPI()

@app.get("/query")
def query_case(q: str = Query(...)):
    return search_chunks(q)
# This is a test change to trigger GitHub Actions
