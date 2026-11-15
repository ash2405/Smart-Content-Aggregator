from unittest.mock import AsyncMock, patch

import pytest

from app.crawler.config import BOOKS_SOURCE
from app.crawler.runner import runner_cwarling
from app.schemas.article import ArticleCreate
from app.exceptions.exceptions_log import ConflictException


@pytest.mark.asyncio
async def test_run_crawler_skips_duplicates():
    mock_db =  AsyncMock()

    mock_articles = [
        ArticleCreate(
            title="Python Book",
            url="https://example.com/python",
            content="Learn Python",
            source_id=1,
            status="Publish"
        ),
        ArticleCreate(
            title="FastAPI Book",
            url="https://example.com/fastapi",
            content="Learn FastAPI",
            source_id=1,
            status="Publish"
        )
    ]

    with patch(
         "app.crawler.runner.fetch_website", new_callable=AsyncMock
         ) as mock_fetch,patch(
             "app.crawler.runner.parse_article"
             ) as mock_parse, patch(
                 "app.crawler.runner.transform_external_article"
                 ) as mock_mapper,patch(
                     "app.crawler.runner.create_article_service", new_callable=AsyncMock
                 ) as mock_create:

        mock_fetch.return_value = "<html>Testing Skips Duplicates</html>"

        mock_parse.return_value = [
            {"title":"Python Book"},
            {"title":"FastAPI Book"}
        ]

        mock_mapper.return_value = mock_articles
        

        mock_create.side_effect = [
            ConflictException("already exist"),
            mock_articles[1]
        ]

        result = await runner_cwarling(
            config=BOOKS_SOURCE,
            source_id=1,
            db=mock_db
        )

        assert result["fetch_articles"] == 2
        assert result["saved_articles_count"] == 1
        assert len(result["save_articles"]) == 1
        assert result["skipped_duplicates_count"] == 1
