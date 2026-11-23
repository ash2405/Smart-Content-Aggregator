from celery import Celery
from app.core.config import settings

celery_app = Celery(
    "smart_content_aggregator",
    broker = settings.redis_url,
    backend=settings.redis_url,
    include=["app.tasks"] # Register tasks with Celery
)

celery_app.conf.update(
    task_serializer = 'json',
    accept_content=["json"],
    result_serializer="json",
    timezone="Asia/Kolkata",
    enable_utc=True
)


# Celery() — Celery application create karta hai.
# broker — Redis ko task messages bhejta hai.
# backend — Task execution results store karta hai.
# task_serializer — Task data ko JSON format mein serialize karta hai.
# timezone — Task scheduling ke liye timezone.