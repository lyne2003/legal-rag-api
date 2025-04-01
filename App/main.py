from fastapi import FastAPI, Query
from rag_logic import search_chunks

app = FastAPI()

@app.get("/query1")
def query_case(q: str = Query(...)):
    returjjjn search_chunks(q)

