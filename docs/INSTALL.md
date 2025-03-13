# Installation Guide

## Prerequisites
- Python 3.9+
- Node.js 16+
- Docker & Docker Compose
- Git

## Steps
1. Clone the repository: `git clone ...`
2. Install backend dependencies: `pip install -r backend/requirements.txt`
3. Install frontend dependencies: `npm install --prefix frontend`
4. Run data ingestion: `python data_ingestion/scheduler.py`
5. Train model: `python model_training/train.py`
6. Start services: `docker-compose up --build`