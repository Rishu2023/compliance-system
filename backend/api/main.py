from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.services.nlp import parse_query
from backend.models.response import generate_response
from backend.utils.encryption import encrypt_data
import logging

app = FastAPI(title="Regulatory Compliance API")
logging.basicConfig(level=logging.INFO, filename='backend/compliance.log')

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
async def query_compliance(request: QueryRequest):
    """Process a compliance query and return AI-generated response."""
    try:
        parsed = parse_query(request.question)
        response = generate_response(request.question)
        encrypted_response = encrypt_data(response.encode()).hex()
        logging.info(f"Query: {request.question}, Encrypted Response: {encrypted_response}")
        return {"question": request.question, "response": response, "entities": parsed["entities"]}
    except Exception as e:
        logging.error(f"Query failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Check the health of the API."""
    return {"status": "healthy"}