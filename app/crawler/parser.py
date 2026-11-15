from urllib.parse import urljoin

from bs4 import BeautifulSoup

from app.crawler.config import CrawlerSourceConfig


def parse_article(
        html: str,
        config: CrawlerSourceConfig,
):
    soup = BeautifulSoup(html, "lxml")

    articles = []

    article_elements = soup.select(
        config.article_list_selector
    )

    for element in article_elements:
        title_element = element.select_one(
            config.title_selector
        )

        content_element = element.select_one(
            config.content_selector
        )

        image_element = (
            element.select_one(config.image_selector)
            if config.image_selector else None
        )

        link_element = element.select_one(
            config.link_selector
        )   

        if not title_element:
            continue

        title = title_element.get_text(strip=True)

        content = (
            content_element.get_text("" ,strip=True)
            if content_element else None
        )

        url = (
            urljoin(config.base_url,link_element.get("href"))
            if link_element and link_element.get("href")
            else None
        )

        image_url = (
            urljoin(config.base_url, image_element.get("src"))
            if image_element and image_element.get("src")
            else None
        )

        articles.append({
            "title": title,
            "content": content,
            "url": url,
            "image_url": image_url,
        })

    return articles

