from app.core.celery_app import celery_app


@celery_app.task
def test_celery_task():
    return "Celery is working successfully!"

# Background Jobs with Celery
# bind=True → Celery task instance ko self ke through provide karta hai.
@celery_app.task(
        bind=True,
        max_retries=3,
        default_retry_delay=10
        )
def process_article_id(self,article_id:int):

    try:
        print(f"Artilce id for the porcess id {article_id}")

        if article_id == 888:
            raise ConnectionError("Temporary network error!")

        if article_id == 999:
            raise ValueError("Article processing failed!")

        return{
            "message":"return from Process article",
            "article_id":article_id
        }
    
    except ValueError:
        raise
    
    except Exception as exc:
        # self.retry() → task ko retry karne ke liye schedule karta hai.
        raise self.retry(exc=exc , countdown=5)
