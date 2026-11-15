from unittest.mock import AsyncMock, patch

import pytest

from app.crawler.config import BOOKS_SOURCE
from app.crawler.runner import runner_cwarling


@pytest.mark.asyncio
async def test_crawler_empty_res():
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
        
        mock_fetch.return_value = "<html></html>"
        mock_parse.return_value = []
        mock_mapper.return_value = []

        result = await runner_cwarling(
            config=BOOKS_SOURCE,
            source_id=1,
            db=mock_data
        )

        assert result["fetch_articles"] == 0
        assert result["saved_articles_count"] == 0
        assert len(result["save_articles"]) == 0
        assert result["skipped_duplicates_count"] == 0

        mock_create.assert_not_called()
        