import requests
from bs4 import BeautifulSoup
import logging
import os

logging.basicConfig(level=logging.INFO, filename='data_ingestion/scraper.log')

def scrape_regulations(url="https://www.sec.gov/rules"):
    """Scrape regulatory text from a given URL."""
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = [p.get_text(strip=True) for p in soup.find_all('p') if p.get_text(strip=True)]
        logging.info(f"Scraped {len(texts)} regulations from {url}")
        return texts
    except Exception as e:
        logging.error(f"Scraping failed: {e}")
        return []

def save_to_file(texts, filepath="data_ingestion/data/regulations.txt"):
    """Save scraped texts to a file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("\n".join(texts))

if __name__ == "__main__":
    texts = scrape_regulations()
    if texts:
        save_to_file(texts)