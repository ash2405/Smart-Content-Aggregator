import asyncio

from app.schemas.scraped_book import ScrapedBookSchema
from app.scraping.fetcher import fetcher_html
from app.scraping.get_all_parse import parse_html
from app.services.external_news_service import transform_external_article
from app.services.scraping_service import transform_scraped_book

# function for creating data with validation and set data value for db insert
async def main():
    url = "https://books.toscrape.com/"

    html = await fetcher_html(url)

    books = parse_html(
        html=html,
        base_url=url
    )

    validate_book = [
        ScrapedBookSchema.model_validate(book)
        for book in books
    ]
    print("validate_book:", validate_book[0])

    transform_data = transform_scraped_book(
        book=validate_book[0],
        source_id=1
    )

    print("transform data:",transform_data)
    print("Total books:", len(books))
    print("Total validate book:", len(validate_book))


    # for book in books[:5]:
    #     print("\nBook Details:")
    #     print("Title:", book["title"])
    #     print("Price:", book["price"])
    #     print("Availability:", book["availability"])
    #     print("URL:", book["url"])


if __name__ == "__main__":
    asyncio.run(main())