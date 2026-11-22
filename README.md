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
         
## Automated Testing with Pytest
 * install the package: pip show pytest pytest-asyncio httpx
 * install missing dependencies: pip install pytest pytest-asyncio httpx
   - pytest: Python tests run karne ke liye.
   - pytest-asyncio: async FastAPI/SQLAlchemy code test karne ke liye.
   - httpx: API endpoints ko test client ke through request bhejne ke liye.
 * Varify the package : python -m pytest --version
 * For basic testing : test_basic.py
 * Run the test case : python -m pytest -v
 * check tests/health : test_health_endpoint
 * Run the test case : python -m pytest tests/test_health.py -v
 * Test POST Article API
   - tests/test_articles.py
      * Health API
      * Create Article — POST
      * Get Articles — GET
      * Get Article by ID
      * Delete Article
      * Update Article — PUT
      * Article Not Found — 404
      * Invalid Article Data — 422
   - tests/conftest.py : for common "client"

## SQLite testing dependency with mock data
   ```text
   tests/
   │
   ├── mocks/
   │   ├── __init__.py
   │   ├── article_mock.py
   │   ├── source_mock.py
   │   └── user_mock.py
   │
   ├── conftest.py
   ├── test_articles.py
   ├── test_sources.py
   └── test_users.py
   ```
   > For Seperate test function python -m pytest tests/test_articles.py::test_get_article_by_id -v -s
   > For all test function python -m pytest tests/test_articles.py
   * Work on test_article:
   * To check covrage: pip install pytest-cov
   * Run on cmd : pytest --cov=app -v
   * Generate an HTML coverage report : pytest --cov=app --cov-report=html
   * Open Html file : start htmlcov/index.html
   * Detail Html coverage report : pytest --cov=app --cov-report=html
   * Open Html file : start htmlcov/index.html
## Article data add with Crawling
   ```text
   Crawler configuration
   Website fetcher
   HTML parser
   Article mapper
   Crawler runner
   Mapper, parser aur fetcher unit tests
   Runner integration tests
   Duplicate article handling
   Fetch failure handling
   Empty response handling
   ```
   ``` text
   app
     |- crawler
         |- config.py
         |- fetcher.py
         |- parser.py
         |- mapper.py
         |- runner.py

      -----------------------
      - Fetch
         Website ka HTML download.

      - Parse
         HTML se article information extract.
      
      - Map
         Data ko ArticleCreate schema mein convert.
      
      - Save
         Existing Article service se database mein save.

      - Skip duplicates
         Already existing articles ko skip.
   ```
   
 * tests/test_crawler.py
 * pytest -v -s tests/test_crawler.py
 * tests/test_crawler_mapper.py
 * pytest -v tests/test_crawler_mapper.py
 * test_crawler_parser.py
 * pytest -v tests/test_crawler_parser.py
 * tests/test_crawler_fetcher.py
 * pytest -v tests/test_crawler_fetcher.py
 * tests/test_crawler_runner.py
 * pytest -v tests/test_crawler_runner.py
 * tests/test_crawler_runner_error.py
 * pytest -v tests/test_crawler_runner_error.py
 * tests/test_crawler_runner_empty_res.py 
 * ## Handle Duplicate Insert Errors
  ```
  - app/services/article.py
      from sqlalchemy.exc import IntegrityError
 ```
   - tests/test_article_service.py

## Cwarling By Router Endpoint
* Route   : app/routes/crawler.py
* Schemas : app/schemas/crawler.py
* tests/test_trigger_crawler.py
* pytest -v tests/test_trigger_crawler.py
* tests/test_trigger_crawler_not_found.py
* Test invalid id
```
Crawler API integration and its tests
  * API endpoint connected to crawler runner.
  * Response schema and validation.
  * Success response test (200).
  * Source not found test (404).
  * Invalid source ID test (422).
  * Complete test suite executed.
```
## Background Workers
FastAPI provides BackgroundTasks to execute work after sending the HTTP response.
* Create a background task function : app/crawler/tasks.py
* app/routes/crawler.py
* update for background : app/schemas/crawler.py
* background task at service-level test : tests/test_crawler_tasks.py

## File Upload
```
Implementation

- File upload using UploadFile
- File size, content type, and extension validation
- Safe server-side filename generation
- Saving files to disk
- Storing file metadata in PostgreSQL
- Delete file endpoint
```
 -  app/routes/file.py

## Redis Setup
* Understand Redis : Redis is an in-memory data store. It stores data primarily in RAM, so reading and writing data is very fast.
* We'll use Redis for:
  * Caching — Store frequently requested article data.
  * Rate Limiting — Track how many requests an IP makes.
  * Celery Broker — Send background jobs to Celery workers.

* Create a Redis Cloud account
   * Open Redis Cloud. : https://cloud.redis.io/#/login/?socialMethod=google&utm_source=chatgpt.com&utm_medium=ai-assistant
   * Create Database and obtain the detail.
   * Configure REDIS_URL in .env
   * Install Redis Python Client : pip install redis
   * Verify installed package : pip show redis
   * Update requirements : pip freeze > requirements.txt
   * Create a new file : app/config/redis.py
   * Test Redis Connection : app/core/redis.py
   * Test connection : tests/test_redis.py
   * Integrate Redis with FastAPI Lifespan
      - FastAPI start ho → Redis connection verify ho.
      - Application running ho → Redis client available rahe.
      - FastAPI shutdown ho → Redis connection properly close ho.
   * Add return and raise : app/core/redis.py 
   * Create : app/services/redis.py  Implement SET, GET, DELETE operations
   * Implement TTL (Time To Live) : TTL ka matlab hai kisi Redis key ki expiration time.
   * Test Redis Service : tests/test_redis_getset.py
   * Redis connection error handling

## API Caching
```
Caching implement karne ke baad:
- First request: Database se data fetch hoga aur Redis mein save hoga.
- Second request: Redis se data return hoga.
- Redis mein data nahi mila: Database se fetch karke Redis mein save karenge.
```
   * Cache Article list
   * Cache Article details
   * Create cache keys
       - Create Cache key in service/article/get_articles_service
   * Serialize response data
   * Configure TTL
   * Return cached response
   * Test cache hit
   * Test cache miss
   * Cache Keys Review
   * Task Done
      - Cache Article list
      - Cache Article details
      - Create cache keys
      - Serialize response data
      - Configure TTL
      - Return cached response
      - Test cache hit
      - Test cache miss

## Cache Invalidation + Review
   * Cache invalidation on Create
      -  app/service/redis.py : invalidate_cache()
   * Cache invalidation on Update
      - app/service/article: 
   * Cache invalidation on Delete
      - app/service/article: 
   * Cache consistency tests
      - app/service/article: 
   * Redis + Crawler + File Upload review
      - GET /articles/1 — detail cache create karo.
      - GET /articles/ — list cache create karo.
      - DELETE /articles/1 — article delete karo.
      - GET /articles/1 — expected 404 Not Found.
      - GET /articles/ — deleted article response.
## Rate Limit
```
Rate Limiting ka meaning hai: Ek user kitni API requests ek fixed time period mein kar sakta hai, uski limit set karna.
   Why use Rete Limit
   1. Prevent API abuse: Koi user continuously requests nahi bhej sake.
   2. Protect server: Server par unnecessary load reduce hota hai.
   3. Prevent brute-force attacks: Login APIs ko repeated attempts se protect karna.
   4. Fair usage: Ek user saare server resources consume nahi kar sake.
```
* Install Rate Limiting Library : pip install slowapi
* Installation verify : pip show slowapi
* Create Rate Limiter Configuration
   - app/core/rate_limiter.py
* Register Rate Limiter in FastAPI : app/main.py
* Apply Rate Limit on an API : app/routes/article
* Global rate limit vs Route-specific rate limit
   - Route-Specific Rate Limit : Set on every route
   - Global rate limit : default_limits=["100/minute"]
* Rate Limiting with Redis
   - Problem:
      - Server restart hone par counters reset ho sakte hain.
      - Multiple FastAPI workers/processes ke beech counters share nahi honge.
   - Solution: Redis storage use karenge, taaki rate-limit counters Redis mein maintain hon.
   - Configure Redis Storage : pip install limits : if not installed
   - app/core/rate_limiter : storage_uri=settings.redis_url
