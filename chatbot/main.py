from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from legal_terms import legal_terms  # Import the legal terms data

app = FastAPI()

# Set up Jinja2 template renderer
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/legal-question/{term}")
async def get_legal_term(term: str):
    term = term.lower()
    # If the term exists in the dictionary, return the definition
    if term in legal_terms:
        return {"term": term, "definition": legal_terms[term]}
    else:
        return {"error": "Sorry, I don't know this term. Please try asking something else."}
