import asyncio

from app.scraping.fetcher import fetcher_html

# get all html tag data from the web page
async def main():
    url = "https://books.toscrape.com"

    html = await fetcher_html(url)

    print(html[:1000])


if __name__ == "__main__":
    asyncio.run(main())