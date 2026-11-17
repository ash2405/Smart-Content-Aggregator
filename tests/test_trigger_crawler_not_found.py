from unittest.mock import patch

import pytest

from app.exceptions.exceptions_log import NotFoundException

@pytest.mark.asyncio
def test_trigger_crawler_not_found(client):
    with patch("app.routes.crawler.runner_cwarling") as runner_cwarling:

        runner_cwarling.side_effect = NotFoundException("Source Detail not found")

        response = client.post('/crawler/run/221')

        data = response.json()

        assert response.status_code == 404

        assert data['detail'] == "Source Detail not found"

        runner_cwarling.assert_awaited_once()


def test_trigger_crawler_invalid_source_id(client):

    response = client.post("/crawler/run/abc")

    assert response.status_code == 422
