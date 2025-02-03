from time import sleep

import requests
from app.celery_worker import celery


@celery.task
def call_api():
    # Replace the URL below with the API you want to call
    sleep(2)
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    return response.json()
