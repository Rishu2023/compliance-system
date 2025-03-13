import pytesseract
from PIL import Image
import json
import os
import logging

logging.basicConfig(level=logging.INFO, filename='data_ingestion/preprocessor.log')

def process_text_file(filepath="data_ingestion/data/regulations.txt"):
    """Clean and structure text data into JSON."""
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    structured_data = [
        {"text": line, "metadata": {"jurisdiction": "SEC", "date": "2023-10-01"}}
        for line in lines
    ]
    return structured_data

def process_image(image_path):
    """Extract text from an image using OCR."""
    try:
        text = pytesseract.image_to_string(Image.open(image_path))
        return {"text": text.strip(), "metadata": {"jurisdiction": "SEC", "date": "2023-10-01"}}
    except Exception as e:
        logging.error(f"OCR failed for {image_path}: {e}")
        return None

def save_json(data, output_path="data_ingestion/data/regulations.json"):
    """Save processed data as JSON."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    text_data = process_text_file()
    # Example image processing (assumes an image exists locally)
    image_data = process_image("data_ingestion/data/sample_regulation.png") or []
    all_data = text_data + ([image_data] if image_data else [])
    save_json(all_data)