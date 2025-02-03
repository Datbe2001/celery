# Celery

## Requirement
- Python 3.10

## Run dev
- install requirements
```sh
 pip install --no-cache-dir -r requirements.txt
```

## Run celery
```sh
 celery -A app.celery_worker:celery worker --beat --loglevel=info
```

## Run app
```sh
 uvicorn app.main:app --host 0.0.0.0 --port 8000
```