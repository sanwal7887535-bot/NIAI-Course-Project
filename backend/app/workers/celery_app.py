from celery import Celery

from app.core.config import settings

celery_app = Celery("shortlisting", broker=settings.REDIS_URL, backend=settings.REDIS_URL,
                    include=["app.workers.tasks.parse_cv"])
celery_app.conf.task_default_queue = "default"
