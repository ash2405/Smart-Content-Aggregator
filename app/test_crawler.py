import asyncio

from app.scraping.crawler import crawl_books


# getting all pages datas
async def main():
    books = await crawl_books(
        start_url="https://books.toscrape.com/",
        max_pages=3
    )

    print("\nTotal books collected:", len(books))

    for book in books[:5]:
        print(book["title"])


if __name__ == "__main__":
    asyncio.run(main())