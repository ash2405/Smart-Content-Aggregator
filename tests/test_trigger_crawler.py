from unittest.mock import AsyncMock, patch

import pytest


@pytest.mark.asyncio
def test_trigger_crawler(client):

    with patch(
        "app.routes.crawler.runner_cwarling",
        new_callable=AsyncMock) as runner_cwarling:

        runner_cwarling.return_value = {
                    "fetch_articles": 20,
                    "saved_articles_count": 0,
                    "save_articles":[],
                    "skipped_duplicates_count": 0,
                    "skipped_articles": [],
        }

        response = client.post('/crawler/run/2')

        assert response.status_code == 200

        data = response.json()
        assert data["success"] is True
        assert data["data"]["fetch_articles"] == 20
        assert data["data"]["saved_articles_count"] == 0
        assert data["data"]["skipped_duplicates_count"] == 0

        runner_cwarling.assert_awaited_once()