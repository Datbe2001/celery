from time import sleep

import requests
from app.celery_worker import celery_instance


class TaskHandlerCelery:
    @staticmethod
    @celery_instance.task(name='app.tasks.TaskHandler.call_api')
    def call_api():
        sleep(2)
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        return response.json()


celery_task_handler = TaskHandlerCelery()
