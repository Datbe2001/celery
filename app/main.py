from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "FastAPI is running"}


# Endpoint to trigger task (if needed)
@app.get("/trigger-task")
def trigger_task():
    from app.tasks import celery_task_handler
    celery_task_handler.call_api.delay()
    return {"message": "Task is activated"}
