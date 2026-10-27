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