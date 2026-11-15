from unittest.mock import AsyncMock, patch

import pytest
from sqlalchemy.exc import IntegrityError

from app.schemas.article import ArticleCreate
from app.exceptions.exceptions_log import ConflictException
from app.services.article import create_article_service


@pytest.mark.asyncio
async def test_check_duplicate_article_url():
    db = AsyncMock()

    article = ArticleCreate(
        title="Duplicate Test Article",
        url="https://example.com/duplicate-test",
        content="Test content",
        source_id=1,
    )

    with patch(
        "app.services.article.get_source_by_id",
        new_callable=AsyncMock
    ) as get_source_by_id, patch(
        "app.services.article.get_article_by_url",
        new_callable=AsyncMock
    ) as get_article_by_url, patch(
        "app.services.article.create_article_item",
        new_callable=AsyncMock
    ) as create_article_item :

        get_source_by_id.return_value = object()
        get_article_by_url.return_value = None
        create_article_item.return_value = object()

        db.commit.side_effect = IntegrityError(
            "INSERT",
            {},
            Exception("duplicate key value violates unique constraint"),
        )

        with pytest.raises(ConflictException):
            await create_article_service(article ,db)

        db.rollback.assert_awaited_once()
