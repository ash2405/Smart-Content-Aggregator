from sqlalchemy.ext.asyncio import AsyncSession
from app.crawler.config import CrawlerSourceConfig
from app.crawler.fetcher import fetch_website
from app.crawler.mapper import transform_external_article
from app.crawler.parser import parse_article
from app.exceptions.exceptions_log import ConflictException
from app.services.article import create_article_service


async def runner_cwarling(
        config: CrawlerSourceConfig,
        source_id: int,
        db: AsyncSession
):
    # fetch the website content
    html = await fetch_website(config.base_url)

    # parse the articles from the HTML content
    articles = parse_article(html, config)

    # transform the articles into the desired schema
    transformed_articles = transform_external_article(articles, source_id)

    save_articles =[]
    skip_duplicates = []

    for article in transformed_articles:
        try:
            save_article = await create_article_service(article, db)

            save_articles.append(save_article)
        except ConflictException:
            skip_duplicates.append(article)

    return {
        "fetch_articles": len(articles),
        "saved_articles_count": len(save_articles),
        "save_articles": save_articles,
        "skipped_duplicates_count": len(skip_duplicates),
        "skipped_articles": skip_duplicates,
    }