from celery import Celery
from celery.schedules import crontab

celery = Celery(
    "worker",
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

celery.conf.beat_schedule = {
    'call-api-at-midnight': {
        'task': 'app.tasks.call_api',
        'schedule': crontab(minute=0, hour=0),
    },
}

celery.autodiscover_tasks(['app'])
