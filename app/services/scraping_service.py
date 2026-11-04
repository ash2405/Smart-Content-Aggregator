from app.schemas.scraped_book import ScrapedBookSchema


def transform_scraped_book(
    book: ScrapedBookSchema,
    source_id: int,
) -> dict:
    return {
        "title": book.title,
        "url": str(book.url),
        "content": f"Price: {book.price}. Availability: {book.availability}",
        "source_id": source_id,
        "published_at": None,
    }