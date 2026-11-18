
from unittest.mock import AsyncMock, patch

import pytest

from app.crawler.tasks import run_crawling_bg
from app.exceptions.exceptions_log import BadRequestException


@pytest.mark.asyncio
async def test_run_crawler_task_success():

    with patch(
        "app.crawler.tasks.AsyncSessionLocal"
    ) as mock_session, patch(
        "app.crawler.tasks.runner_cwarling",
        new_callable=AsyncMock
    ) as mock_runner, patch(
        "app.crawler.tasks.logger"
    ) as mock_logger:
        
        # mock_session.return_value → mocked session factory ka returned context manager.
        # __aenter__.return_value → async with ke andar milne wala DB object.
        # mock_db → wahi mocked DB object jo db variable mein assign hoga.

        mock_db = mock_session.return_value.__aenter__.return_value

        mock_runner.return_value = {
            "save_articles": 5
        }

        await run_crawling_bg(source_id=2)

        mock_runner.assert_awaited_once()

        # ************ ----- IMP ----- ************
        assert mock_runner.call_args.kwargs["source_id"] == 2
        assert mock_runner.call_args.kwargs["db"] is mock_db
        # ************ ----- IMP ----- ************

        mock_logger.info.assert_called()


@pytest.mark.asyncio
async def test_run_crawler_task_failur():
    with patch(
        "app.crawler.tasks.AsyncSessionLocal"
    ) as mock_async, patch(
        "app.crawler.tasks.runner_cwarling"
    ) as mock_runner, patch(
        "app.crawler.tasks.logger"
    ) as mock_logger:


        mock_runner.side_effect=Exception("Crawler failed")

        await run_crawling_bg(source_id=3)
        
        mock_runner.assert_awaited_once()

        mock_logger.exception.assert_called_once()