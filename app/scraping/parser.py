from bs4 import BeautifulSoup

# function is for getting all title data which are showing in soup.select(...)
def parse_html(html:str):
   
    # get page title
    soup = BeautifulSoup(html,"lxml")

    # get title 
    page_title = soup.title.string.strip()

    # get all title
    books = soup.select("article.product_pod h3 a")

    book_titles = [
        book.get("title")
        for book in books
    ]

    return {
        "page_title": page_title,
        "books": book_titles
    }


# BeautifulSoup(html, "lxml") — HTML ko parse karta hai.

# soup.title — webpage ka title find karta hai.

# soup.select("article.product_pod h3 a") — CSS selector se saare book links find karta hai.