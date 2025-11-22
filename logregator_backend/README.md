# Logregator backend

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run fake logs

```bash
API_URL="http://localhost:8000/api/log/add" API_TOKEN="12345" python logs.py
```