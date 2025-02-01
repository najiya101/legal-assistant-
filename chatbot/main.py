# main.py
from fastapi import FastAPI
from legal_terms import legal_terms  # Import the legal terms data

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Legal Terms Chatbot!"}

@app.get("/legal-question/{term}")
async def get_legal_term(term: str):
    term = term.lower()
    # If the term exists in the dictionary, return the definition
    if term in legal_terms:
        return {"term": term, "definition": legal_terms[term]}
    else:
        return {"error": "Sorry, I don't know this term. Please try asking something else."}
