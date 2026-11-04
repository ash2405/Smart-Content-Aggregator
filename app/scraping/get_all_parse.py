from bs4 import BeautifulSoup
from urllib.parse import urljoin

# get all selector data from class also
def parse_html(html: str, base_url: str):
    soup = BeautifulSoup(html, "lxml")

    books = soup.select("article.product_pod")

    book_data = []

    for book in books:
        title_tag = book.select_one("h3 a")
        price_tag = book.select_one(".price_color")
        availability_tag = book.select_one(
            ".availability"
        )

        book_data.append({
            "title": title_tag.get("title"),
            "price": price_tag.get_text(strip=True),
            "availability": availability_tag.get_text(strip=True),
            "url": urljoin(
                base_url,
                title_tag.get("href")
            )
        })

    return book_data


# function for crawling getting next page
def get_next_page_url(html: str, current_url: str):
    soup = BeautifulSoup(html, "lxml")

    next_link = soup.select_one("li.next a")

    if next_link is None:
        return None

    return urljoin(
        current_url,
        next_link.get("href")
    )

    # li.next a — website ka Next button find karta hai.
    # get("href") — next page ka link deta hai.
    # urljoin() — relative link ko complete URL banata hai.
    # Next page nahi hai toh None return karega.