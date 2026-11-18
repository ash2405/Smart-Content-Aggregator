from loguru import logger

from app.crawler.runner import runner_cwarling
from app.crawler.config import BOOKS_SOURCE
from app.db.session import AsyncSessionLocal

async def run_crawling_bg(source_id:int):
    logger.info(f"Background crawler started for source_id={source_id}")

    try:
        # AsyncSessionLocal() — background task apna independent database session create karega.
        async with AsyncSessionLocal() as db:

            # runner_cwarling() — existing crawler logic execute karega.
            response = await runner_cwarling(
                db=db,
                source_id= source_id,
                config=BOOKS_SOURCE   
            )

            # logger.info() — execution information log karega.
            logger.info(
                f"Background crawler completed: {response['saved_articles_count']} articles saved"
            )

    except Exception:
        # logger.exception() — error aur traceback log karega.
        logger.exception(
            f"Background crawler failed for source_id={source_id}"
        )

