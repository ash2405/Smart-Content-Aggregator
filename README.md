# Smart Content Aggregator API — Setup Flow

## Create Virtual Environment

   ```bash
   python -m venv venv
   venv\Scripts\activate
   python --version
   ```

## Install Initial Dependencies

   ```bash
   pip install fastapi "uvicorn[standard]" pydantic-settings python-dotenv loguru
   pip freeze > requirements.txt
   ```

   Check installed packages:

   ```bash
   pip list
   ```

## Create Project Structure

   ```text
   smart-content-aggregator/
   ├── app/
   │   ├── core/
   │   │   ├── config.py
   │   │   ├── logging.py
   │   │   └── lifespan.py
   │   ├── db/
   │   │   ├── session.py
   │   │   └── base.py
   │   └── main.py
   ├── .env
   ├── .env.example
   ├── .gitignore
   └── requirements.txt
   ```

   Configure environment variables and application settings in `app/core/config.py`.

   **Important:** `.env` mein secrets rakho aur use Git mein commit mat karo. `.env.example` mein sirf placeholder values rakho.

## Run the FastAPI Application

   ```bash
   uvicorn app.main:app --reload
   ```

   Open these URLs:

   * API documentation: http://127.0.0.1:8000/docs
   * Health endpoint: http://127.0.0.1:8000/health

## Logging and Error Handling

   * `app/core/logging.py` — Configure Loguru logging.
   * `app/core/lifespan.py` — Handle application startup and shutdown.
   * `app/core/exceptions.py` — Define custom exceptions.
   * `app/core/exception_handlers.py` — Handle exceptions and standardize error responses.
   * `app/core/middleware.py` — Add request logging middleware, if required.

   Register exception handlers and middleware when creating the FastAPI application.

## PostgreSQL + Async SQLAlchemy

   Install dependencies:

   ```bash
   pip install sqlalchemy asyncpg
   pip freeze > requirements.txt
   ```

   Configure the database:

   1. Add `DATABASE_URL` to `.env`.
   2. Add `database_url: str` to `app/core/config.py`.
   3. Create `app/db/session.py` to configure the async engine, session factory, and `get_db()`.
   4. Create `app/db/base.py` to define the SQLAlchemy `Base`.
   5. Test the database connection using `SELECT 1`.

## Next Steps

   * Create database models: User, Source, Article, ArticleFile.
   * Configure Alembic for database migrations.
   * Create CRUD operations and API routes.
   * Add request validation and database error handling.
   * Write tests using pytest.
   * Add Redis caching, rate limiting, background tasks, and external API integration.

## Model
   * User model : app/model/user.py
   * Install Alembic
      - pip install alembic
      - pip freeze > requirements.txt
   * alembic init alembic 
   * pip install "sqlalchemy[asyncio]"
   * pip show greenlet
   * pip freeze > requirements.txt
   * python -c "from app.core.config import settings; print(settings.database_url.split('://')[0])"
   * alembic revision --autogenerate -m "create users table"
   * alembic upgrade head
   * create model: user, source , article
   * To verify the all model
      * python -c "from app.models import User, Source, Article, ArticleFile; print('All models imported successfully')"

## SQL Editor Queries
   * TO check all tables
      - SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
        ORDER BY table_name;
   * TO check the relation
      
## Source APIs
   * app/schemas/source.py
   * python -c "from app.schemas.source import SourceCreate, SourceResponse; print('Source schemas imported successfully')"
   * endpoints for Source
      - Get
      - Post
      - Update
      - Delete
   - Auto Test
      > pip install pytest pytest-asyncio httpx
      > - pytest — tests run karne ke liye.
      > - pytest-asyncio — async functions test karne ke liye.
      > - httpx — FastAPI endpoints ko test client se call karne ke liye.
      -  pip freeze > requirements.txt
      * pip install pytest pytest-asyncio httpx
## Article APIs
   * app/schemas/article.py
   * python -c "from app.schemas.article import ArticleCreate, ArticleResponse; print('Article schemas imported successfully')"
   * start work on endpoint
      - app/repositories/article.py
      - app/services/article.py
      - app/routers/article.py
   * Search by title — article title mein keyword search.
   * Filter by source — kisi particular source ke articles.
   * Pagination — skip and limit se results control karna.
   * Sorting — latest articles pehle dikhana.
## Article File
   * Model Create: article_file.py
   * pip install python-multipart
   * Service : app/service/article_file.py
   * Repository : app/repository/article_file.py
   * Routes : app/routes/article_file.py
## HTTPX
   > For calling external Api Request from the Fast API we need HTTPX
   * pip install httpx
   * update required.txt : pip freeze > requirements.txt
   * Run on Terminal : python -c "import httpx; print(httpx.__version__)"
      - (If print the version shows then installation done)
   ```text
    External API
        |
        v
   Fetch articles
        |
        v
   Validate response
        |
        v
   Transform into Article schema
        |
        v
   Check duplicate URL
        |
        v
   Save to PostgreSQL
        |
        v
   Return import summary
   ```
   * External API: Create schema app/schemas/external_news.py
   * Add validation check in app/service/external_new_service.py: 
   * Add transform function in app/service/external_new_service.py: (transform_external_article)
   * Add this external data into article table in db: app/repository/article: create_external_article
   * Update function on app/service/article save_external_article to add article in DB with all checks 
## Web Scraping & Crawling
   ``` bash
    Web Scraping = Website se specific data extract karna.
    Example: Kisi news website se ye information nikalni hai:
    - Article title
    - Article URL
    - Published date
    - Article content

    Web Crawling = Websites ke pages aur links ko automatically discover aur visit karna.

    Fetch articles directly from websites instead of relying only on third-party APIs.
   ```

   * Install BeautifulSoup and required dependencies.
      - pip install beautifulsoup4 lxml
      - Verify installation: python -c "from bs4 import BeautifulSoup; import lxml; print('Scraping dependencies installed successfully')"
      ``` text
       Why these libraries?
        - BeautifulSoup4: Extracts information from HTML.
        - lxml: Helps parse HTML efficiently.
        - httpx: Already installed; we'll use it to fetch website HTML.
      ```
   * Fetch website HTML using HTTPX.
      - create fetcher file app/scraping/featcher.py
      - create html to call for testing : app/test_fetch_html.py
   * Extract article title and content using BeautifulSoup.
      - app/scraping/parser.py
      - app/test_fetch_parse.py
      - check validation : app/schemas/scraped_book.py
      - add in to : app/test_fetch_parse.py - ScrapedBookSchema.model_validate(book)
   * Validate scraped data using Pydantic.
   * Save scraped articles in PostgreSQL.
   * Web Crawling (Multiple Pages)
      - app/scraping/parser.py : add function get_next_page_url
      - app/scraping/crawler.py
      - app/test_crawler.py
   ```text
   Page 1
|  
|  -- Extract 20 books
|  
|  -- Find Next Page link
          |
          v
        Page 2
          |
          |-- Extract 20 books
          |
          |-- Find Next Page link
                  |
                  v
                Page 3
   ```
   ```
   Abhi tumhara crawler continuously pages fetch kar raha hai. Real-world websites par bahut fast requests bhejne se server overload ho sakta hai ya website tumhari requests block kar sakti hai.
   Isliye crawler ko responsible banana zaroori hai.
   ```

   * User-Agent add in Fetcher mein : app/scraping/fetcher.py
     -  headers = {
        "User-Agent": "SmartContentAggregator/1.0"
      }
      
   * Add delay in Crwalling : app/scraping/crawler.py
   * Handle scraping errors Scraping Error Handling.
      - Real-world scraping mein multiple errors aa sakte hain:
         - Website unavailable.
         - Request timeout.
         - Connection failure.
         - HTTP 403 / 404 / 500.
         - Invalid HTML response.
      * Update : app/scraping/fetcher.py with try and expect
      * Retry Mechanism implementation
         > If we request to any webpage if it failed so on place of return error it will try again to get content for the web page.
         ```
         Request 1 → Failed
              ↓
         Wait 1 second
              ↓
         Request 2 → Failed
              ↓
         Wait 2 seconds
              ↓
         Request 3 → Success
         ```
         * update code : app/scraping/fetcher.py
         