from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "FastAPI is running"}


# Endpoint to trigger task (if needed)
@app.get("/trigger-task")
def trigger_task():
    from app.tasks import call_api
    call_api.delay()
    return {"message": "Task is activated"}
