from celery import Celery
from celery.schedules import crontab


class CeleryWorker:
    def __init__(self):
        self.celery = Celery(
            "worker",
            broker="redis://localhost:6379/0",
            backend="redis://localhost:6379/0"
        )
        self.celery.conf.beat_schedule = {
            'call-api-at-midnight': {
                'task': 'app.tasks.TaskHandler.call_api',
                'schedule': crontab(minute=41, hour=7),
            },
        }
        self.celery.autodiscover_tasks(['app'])
        self.celery.conf.broker_connection_retry_on_startup = True


# Initialize celery instance for use in other files
celery_instance = CeleryWorker().celery
