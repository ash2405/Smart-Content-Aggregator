from app.crawler.mapper import (
    convert_to_article_schema,
    transform_external_article
)

from app.schemas.article import ArticleCreate


def test_convert_to_article_schema():

    article_data = {
        "title": "Python Tutorial",
        "content": "Learn Python programming.",
        "url": "https://example.com/python",
        "image_url": "https://example.com/python.jpg"
    }

    result = convert_to_article_schema(
        article_data,
        source_id=1
    )

    assert isinstance(result, ArticleCreate)
    assert result.title == "Python Tutorial"
    assert result.source_id == 1


def test_convert_articles_to_schema():

    articles = [
        {
            "title": "FastAPI Tutorial",
            "content": "Learn FastAPI.",
            "url": "https://example.com/fastapi",
            "image_url": None
        },
        {
            "title": "Python Tutorial",
            "content": "Learn Python.",
            "url": "https://example.com/python",
            "image_url": None
        }
    ]

    result = transform_external_article(
        articles,
        source_id=1
    )

    assert len(result) == 2
    assert all(isinstance(item, ArticleCreate) for item in result)