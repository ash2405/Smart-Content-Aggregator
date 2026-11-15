from unittest.mock import AsyncMock

from httpx import patch
import httpx
import pytest


@pytest.mark.asyncio
async def test_fetch_website_success():
    mock_response = AsyncMock()
    mock_response.text = "<html><body><h1>Test Page</h1></body></html>"

    with patch("app.crawler.fetcher.httpx.AsyncClient") as mock_fetch:
        mock_fetch.return_value = AsyncMock(return_value=mock_response.text)

        mock_response.raise_for_status = lambda: None  # Mock the raise_for_status method to do nothing

        result = await mock_fetch("https://example.com")

        assert result == "<html><body><h1>Test Page</h1></body></html>"

# @pytest.mock.asyncio
# async def test_fetch_website_failure():
#     with patch("app.crawler.fetcher.httpx.AsyncClient") as mock_fetch:
#         mock_fetch.return_value.__aenter__.return_value.get = AsyncMock(
#             side_effect=httpx.connect.ConnectTimeout("Connection timed out")
#         )

#         with pytest.raises(httpx.connect.ConnectTimeout):
#             await mock_fetch("https://example.com")

import pytest
import httpx
from unittest.mock import AsyncMock, patch

from app.crawler.fetcher import fetch_website


@pytest.mark.asyncio
async def test_fetch_website_success():

    mock_response = AsyncMock()
    mock_response.text = "<html><body>Test Page</body></html>"

    with patch("app.crawler.fetcher.httpx.AsyncClient") as mock_client:

        mock_client.return_value.__aenter__.return_value.get = AsyncMock(
            return_value=mock_response
        )

        mock_response.raise_for_status = lambda: None

        result = await fetch_website(
            "https://example.com"
        )

        assert result == "<html><body>Test Page</body></html>"


@pytest.mark.asyncio
async def test_fetch_website_failure():

    with patch("app.crawler.fetcher.httpx.AsyncClient") as mock_client:

        mock_client.return_value.__aenter__.return_value.get = AsyncMock(
            side_effect=httpx.ConnectError("Connection failed")
        )

        with pytest.raises(httpx.HTTPError):
            await fetch_website("https://example.com")
