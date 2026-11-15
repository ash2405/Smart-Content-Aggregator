from unittest.mock import AsyncMock, patch
from app.crawler.config import BOOKS_SOURCE
from app.crawler.runner import runner_cwarling
from app.exceptions.exceptions_log import BadRequestException

import httpx
import pytest


@pytest.mark.asyncio
async def test_crawler_runner_error():
    mock_data = AsyncMock()

    with patch(
           "app.crawler.runner.fetch_website", new_callable=AsyncMock
           ) as mock_fetch,patch(
               "app.crawler.runner.parse_article"
               ) as mock_parse, patch(
                   "app.crawler.runner.transform_external_article"
                   ) as mock_mapper,patch(
                       "app.crawler.runner.create_article_service", new_callable=AsyncMock
                   ) as mock_create:  
        
        mock_fetch.side_effect = httpx.ConnectError(
            BadRequestException("Connection Error")
        )

        with pytest.raises(httpx.ConnectError):
            await runner_cwarling(
                config=BOOKS_SOURCE,
                source_id=1,
                db=mock_data
            )

            mock_create.assert_not_called()
            mock_parse.assert_not_called()
