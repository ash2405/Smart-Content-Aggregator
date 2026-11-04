import asyncio

from app.scraping.fetcher import fetcher_html
from app.scraping.get_all_parse import get_next_page_url, parse_html

# getting all text data from the web page
async def crawl_books(
    start_url:str,
    max_pages:int = 3    
):
    current_url = start_url
    all_books = []

    for page_number in range(max_pages):
        if current_url is None:
            break

        # dealy for user agent
        if page_number > 0:
            # crwaling will take 1 second brake in every page request
            await asyncio.sleep(1)
        print(f"Crawling page: {page_number + 1} : current_url")

        html = await fetcher_html(current_url)

        books = parse_html(
            html=html,
            base_url=current_url
        )

        all_books.extend(books)

        current_url = get_next_page_url(
            html=html,
            current_url=current_url
        )

    return all_books
