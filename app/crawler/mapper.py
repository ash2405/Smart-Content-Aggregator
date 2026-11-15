from app.schemas.article import ArticleCreate


def convert_to_article_schema(
        article_data:dict,
        source_id:int,
)-> ArticleCreate:
    return ArticleCreate(
        title=article_data.get("title"),
        content=article_data.get("content"),
        url=article_data.get("url"),
        image_url=article_data.get("image_url"),
        source_id=source_id,
        status=article_data.get("status", "Publish"),
        published_at=article_data.get("published_at"),
        category=article_data.get("category"),

    )

def transform_external_article(
        articles:list[dict],
        source_id:int
)-> list[ArticleCreate]:
    converted_articles = []

    for article in articles:
        if not article.get("title") or not article.get("url"):
            continue

        converted_articles.append(
            convert_to_article_schema(
                article_data=article,
                source_id=source_id
            )
        )

    return converted_articles
