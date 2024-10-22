from celery import Celery

celery_app = Celery('traceintel', broker='redis://localhost:6379/0')

@celery_app.task
def run_scheduled_scan(keyword):
    # Dummy task logic
    return f"Running scheduled scan for: {keyword}"
