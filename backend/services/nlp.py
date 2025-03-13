import spacy

nlp = spacy.load("en_core_web_sm")

def parse_query(query: str) -> dict:
    """Parse a query and extract entities using spaCy."""
    doc = nlp(query)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return {"entities": entities}