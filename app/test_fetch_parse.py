import asyncio

from app.scraping.fetcher import fetcher_html
from app.scraping.parser import parse_html

# get all title from the web page
async def main():
    url = "https://books.toscrape.com/"

    html = await fetcher_html(url)

    result = parse_html(html)

    print("Website:", result["page_title"])

    print("\nBooks found:", len(result["books"]))

    for title in result["books"]:
        print(title)


if __name__ == "__main__":
    asyncio.run(main())