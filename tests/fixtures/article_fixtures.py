import pytest

from tests.mocks.article_mock import MOCK_ARTICLE, MOCK_ARTICLES


# For Create Article Test
@pytest.fixture
def mock_article():
    return MOCK_ARTICLE.copy()

# For Get Articles List
@pytest.fixture
def mock_article_list():
    return {
            "items":[article.copy() for article in MOCK_ARTICLES],
            "total": len(MOCK_ARTICLES),
            "skip": 0,
            "limit": 100
            }