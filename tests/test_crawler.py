import pytest

from app.crawler.fetcher import fetch_website
from app.crawler.config import BOOKS_SOURCE
from app.crawler.parser import parse_article

@pytest.mark.asyncio
async def test_fetch_and_parse_book():

    html = await fetch_website(BOOKS_SOURCE.base_url)

    assert html
    assert '<html' in html.lower()

    articles = parse_article(html, BOOKS_SOURCE)

    assert len(articles) > 0

    print(f"Found {len(articles)} articles.")

    assert articles[0]["title"]
    assert articles[0]["url"]