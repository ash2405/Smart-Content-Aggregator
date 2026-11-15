from pydantic import BaseModel


class CrawlerSourceConfig(BaseModel):
    name: str
    base_url: str
    article_list_selector: str
    title_selector: str
    content_selector: str
    image_selector: str | None = None
    link_selector: str = "a"


BOOKS_SOURCE = CrawlerSourceConfig(
    name="Books to Scrape",
    base_url="https://books.toscrape.com/",
    article_list_selector="article.product_pod",
    title_selector="h3 a",
    content_selector=".product_price .price_color",
    image_selector="img",
)