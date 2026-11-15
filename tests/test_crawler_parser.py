
from app.crawler.config import BOOKS_SOURCE
from app.crawler.parser import parse_article


def test_parse_articles():

    html = """
    <html>
        <body>
            <article class="product_pod">
                <h3>
                    <a href="catalogue/python-book_1/index.html"
                       title="Python Book">
                        Python Book
                    </a>
                </h3>

                <div class="product_price">
                    <p class="price_color">£25.00</p>
                </div>

                <img src="media/python-book.jpg"
                     alt="Python Book">
            </article>
        </body>
    </html>
    """

    result = parse_article(
        html=html,
        config=BOOKS_SOURCE
    )

    assert len(result) == 1

    assert result[0]["title"] == "Python Book"

    assert result[0]["content"] == "£25.00"

    assert result[0]["url"] == (
        "https://books.toscrape.com/catalogue/python-book_1/index.html"
    )

    assert result[0]["image_url"] == (
        "https://books.toscrape.com/media/python-book.jpg"
    )
