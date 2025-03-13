from apscheduler.schedulers.blocking import BlockingScheduler
from scraper import scrape_regulations, save_to_file
from preprocessor import process_text_file, save_json
import logging

logging.basicConfig(level=logging.INFO, filename='data_ingestion/scheduler.log')

def scheduled_task():
    """Run scraping and preprocessing on a schedule."""
    texts = scrape_regulations()
    if texts:
        save_to_file(texts)
        data = process_text_file()
        save_json(data)
        logging.info("Scheduled task completed.")

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(scheduled_task, 'interval', hours=24)
    scheduled_task()  # Initial run
    scheduler.start()