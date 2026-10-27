# Smart Content Aggregator — 38-Day Development Roadmap

## 🎯 Project Goal

Build a production-style **Smart Content Aggregator** using:

* FastAPI
* PostgreSQL
* SQLAlchemy Async
* Repository Pattern
* Service Layer
* Pydantic
* Alembic
* Redis
* Celery
* Web Crawling
* Third-party API Integration
* File Upload
* Rate Limiting
* Background Workers
* Pytest
* Logging
* Custom Exceptions
* Global Error Handling
* API Documentation

### Target

* **Daily:** 2 hours
* **Duration:** ~5 weeks
* **Total:** ~60 hours
* **Sunday:** Revision / Catch-up / Rest

---

# Week 1 — Foundation + Database

## Day 1 — Project Setup

* Create project
* Create virtual environment
* Install FastAPI + dependencies
* Create project folder structure
* Configure `.env`
* Setup `pydantic-settings`
* Create FastAPI application
* Create `/health` endpoint
* Setup Git / `.gitignore`

---

## Day 2 — Logging & Error Handling

* Setup Loguru
* Configure application logging
* Create log files
* Add request logging
* Create custom exceptions
* Create global exception handlers
* Standardize error response

---

## Day 3 — PostgreSQL + SQLAlchemy

* Configure PostgreSQL
* Create async SQLAlchemy engine
* Create `AsyncSession`
* Create `Base`
* Create `get_db()`
* Configure database environment variables

---

## Day 4 — Database Models

* Create `User` model
* Create `Source` model
* Create `Article` model
* Create `ArticleFile` model
* Configure relationships
* Add indexes / constraints
* Review model design

---

## Day 5 — Alembic

* Initialize Alembic
* Configure `alembic/env.py`
* Configure async migrations
* Create first migration
* Run upgrade
* Test downgrade
* Verify database tables

---

## Day 6 — Repository Layer

* Create repository structure
* Create Article repository
* Implement `create()`
* Implement `get()`
* Implement `list()`
* Implement `update()`
* Implement `delete()`

---

## Day 7 — Week 1 Review

* Review project architecture
* Test database connection
* Test CRUD repository methods
* Fix issues
* Refactor code
* Review async SQLAlchemy

---

# Week 2 — Article API + Third-Party Integration

## Day 8 — Pydantic Schemas

* Create `ArticleCreate` schema
* Create `ArticleUpdate` schema
* Create `ArticleResponse` schema
* Create `ArticleListResponse` schema
* Add validation
* Configure `from_attributes`
* Add response examples

---

## Day 9 — Article CRUD API

* Create Article router
* `POST /articles`
* `GET /articles`
* `GET /articles/{id}`
* `PATCH /articles/{id}`
* `DELETE /articles/{id}`
* Connect Router → Service → Repository

---

## Day 10 — Pagination

* Implement page-based pagination
* Add `page`
* Add `limit`
* Return total count
* Validate pagination parameters
* Test pagination

---

## Day 11 — Filtering + Sorting

* Filter by source
* Filter by category
* Filter by status
* Search articles
* Sort by created date
* Sort ascending / descending
* Validate sort parameters

---

## Day 12 — Third-Party API Integration

* Setup HTTPX
* Create integration layer
* Configure API URL
* Configure API key
* Implement API request
* Configure timeout
* Handle API errors
* Handle connection failures

---

## Day 13 — External API → Database

* Fetch external articles
* Validate response
* Transform external data
* Check duplicate articles
* Save articles to database
* Handle partial failures

---

## Day 14 — Week 2 Review

* Test Article APIs
* Test pagination
* Test filtering
* Test sorting
* Test third-party API
* Review Router → Service → Repository architecture

---

# Week 3 — Crawling + File Upload + Redis

## Day 15 — Web Crawling Basics

* Understand HTML structure
* Setup BeautifulSoup
* Make HTTP requests
* Parse HTML
* Extract title
* Extract content
* Extract image / URL
* Respect `robots.txt` and site rules

---

## Day 16 — Article Crawler

* Create crawler module
* Create source configuration
* Fetch website
* Parse articles
* Extract required fields
* Convert crawler data to Article schema
* Save crawled articles

---

## Day 17 — Duplicate Detection

* Define unique article identifier
* Handle duplicate URLs
* Add database constraint/index
* Implement duplicate checking
* Handle duplicate insert errors
* Test duplicate crawling

---

## Day 18 — File Upload

* Create upload endpoint
* Use `UploadFile`
* Validate file size
* Validate content type
* Validate extension
* Generate safe filename
* Save file
* Store file metadata
* Create file delete endpoint

---

## Day 19 — Redis Setup

* Setup Redis
* Configure `REDIS_URL`
* Connect FastAPI with Redis
* Create Redis service
* Implement `SET`
* Implement `GET`
* Implement `DELETE`
* Implement TTL
* Handle Redis connection errors

---

## Day 20 — API Caching

* Cache Article list
* Cache Article details
* Create cache keys
* Serialize response data
* Configure TTL
* Return cached response
* Test cache hit
* Test cache miss

---

## Day 21 — Cache Invalidation + Review

* Invalidate cache on create
* Invalidate cache on update
* Invalidate cache on delete
* Test cache consistency
* Review Redis implementation
* Review crawler
* Review file upload

---

# Week 4 — Rate Limiting + Background Workers

## Day 22 — Rate Limiting

* Design rate limiting
* Implement Redis-based rate limiter
* Limit requests per IP
* Configure request window
* Return HTTP `429`
* Add rate-limit headers
* Test rate limiting

---

## Day 23 — Different Rate Limits

* Public API limit
* Search API limit
* Upload API limit
* Crawler trigger limit
* Configure limits using environment variables
* Test different limits

---

## Day 24 — Celery Setup

* Install Celery
* Configure Celery
* Configure Redis broker
* Create Celery application
* Create worker
* Run worker
* Create first task

---

## Day 25 — Background Jobs

* External article fetch task
* Crawler task
* File processing task
* Trigger background job from API
* Return task/job ID
* Test worker execution

---

## Day 26 — Celery Retry & Failure Handling

* Configure task timeout
* Configure retries
* Configure retry delay
* Handle external API failure
* Handle crawler failure
* Handle task exceptions
* Log worker failures

---

## Day 27 — Job Status

* Create Job model
* Create job status enum
* `POST /jobs/crawl`
* `GET /jobs/{job_id}`
* Implement pending status
* Implement running status
* Implement completed status
* Implement failed status

---

## Day 28 — Week 4 Integration

* FastAPI + Redis
* FastAPI + Celery
* Celery + Redis
* Worker + Database
* Crawler + Worker
* External API + Worker
* Test complete background workflow

---

# Week 5 — Testing + Production Hardening

## Day 29 — Pytest Setup

* Install pytest
* Install pytest-asyncio
* Create `tests/`
* Create test configuration
* Create fixtures
* Configure test database
* Write first test

---

## Day 30 — Repository Tests

* Test `create()`
* Test `get()`
* Test `list()`
* Test `update()`
* Test `delete()`
* Test not-found cases
* Test duplicate cases

---

## Day 31 — Service Tests

* Test business logic
* Test duplicate article handling
* Test source validation
* Test cache behavior
* Test external API failure
* Test crawler failure

---

## Day 32 — API Integration Tests

* Test POST Article
* Test GET Articles
* Test GET Article
* Test PATCH Article
* Test DELETE Article
* Test pagination
* Test filtering
* Test validation errors
* Test `404` responses

---

## Day 33 — Error Handling Hardening

* Standardize API errors
* Handle validation errors
* Handle database errors
* Handle Redis errors
* Handle external API errors
* Handle crawler errors
* Handle unexpected exceptions
* Add proper logging
* Hide sensitive error details

---

## Day 34 — CORS + Environment Configuration

* Configure CORS
* Configure allowed origins
* Configure environment variables
* Create `.env.example`
* Remove hardcoded secrets
* Configure production settings
* Review security configuration

---

## Day 35 — API Documentation

* Clean Swagger documentation
* Add API tags
* Add endpoint summaries
* Add endpoint descriptions
* Add response models
* Add status codes
* Add request examples
* Add response examples
* Document error responses

---

# Final Integration + Buffer

## Day 36 — Full System Testing

* Test complete Article flow
* Test Redis caching
* Test rate limiting
* Test background workers
* Test crawler
* Test third-party API
* Test file upload
* Test database migrations
* Run complete test suite

---

## Day 37 — Refactoring

* Remove duplicate code
* Improve naming
* Improve project structure
* Review services
* Review repositories
* Review database queries
* Review async code
* Improve logging
* Fix remaining bugs

---

## Day 38 — Final Project Review

* Final folder structure review
* Final `.env.example`
* Final `requirements.txt`
* Final Alembic migrations
* Final pytest suite
* Final Swagger documentation
* Create README
* Add setup instructions
* Add architecture diagram
* Add API documentation
* Final Git cleanup

---

# Final Feature Checklist

## Backend

* FastAPI
* PostgreSQL
* SQLAlchemy Async
* Repository Pattern
* Service Layer
* Pydantic
* Alembic

## Caching & Performance

* Redis
* Redis Caching
* Cache Invalidation
* Rate Limiting
* Pagination
* Filtering
* Sorting
* Search

## Background Processing

* Celery
* Background Workers
* Retry Mechanism
* Job Tracking
* Task Status

## External Integrations

* Third-party API Integration
* Web Crawling
* File Upload

## Testing

* Pytest
* Async Testing
* Repository Tests
* Service Tests
* API Integration Tests

## Error Handling & Security

* Logging
* Custom Exceptions
* Global Error Handling
* CORS
* Environment Configuration
* Sensitive Data Protection
* Production Configuration

## Documentation

* API Documentation
* Swagger Documentation
* README
* Architecture Diagram
* Setup Instructions

## Final Cleanup

* Final Project Cleanup
* Git Cleanup
* Code Refactoring
* Remove Duplicate Code
* Review Async Code
* Review Database Queries

---

# 🏗️ Project Architecture

```text
Client
   ↓
FastAPI Router
   ↓
Service Layer
   ↓
Repository Layer
   ↓
PostgreSQL
```

## Extended Architecture

```text
                         ┌─────────────────┐
                         │     Client      │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │  FastAPI Router │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │  Service Layer  │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │Repository Layer │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │   PostgreSQL    │
                         └─────────────────┘


        ┌───────────────────────────────────────────┐
        │              Supporting Services          │
        │                                           │
        │  Redis ←→ FastAPI                        │
        │    │                                      │
        │    └────→ Celery Worker                   │
        │                  │                        │
        │                  ├── Crawler              │
        │                  ├── External API         │
        │                  └── File Processing      │
        │                                           │
        └───────────────────────────────────────────┘
```

---

# 🎯 Final Target

By the end of this roadmap, the project should demonstrate practical experience with:

* FastAPI architecture
* Async programming
* PostgreSQL
* SQLAlchemy ORM
* Repository Pattern
* Service Layer
* Database migrations
* REST API development
* Pagination / filtering / sorting / search
* Third-party API integration
* Web crawling
* File handling
* Redis caching
* Cache invalidation
* Rate limiting
* Celery background processing
* Retry mechanisms
* Job tracking
* Automated testing
* Logging
* Exception handling
* Production configuration
* API documentation
* Clean project architecture

> **Daily commitment:** ~2 hours
> **Total duration:** ~38 working days
> **Estimated effort:** ~60 hours
> **Sunday:** Revision / Catch-up / Rest

---

# 🚀 Completion Criteria

The project can be considered complete when:

* All planned features are implemented
* Database migrations work correctly
* CRUD APIs work correctly
* Pagination, filtering, sorting and search work
* External API integration works
* Crawler works
* File upload works
* Redis caching works
* Cache invalidation works
* Rate limiting works
* Celery workers execute background jobs
* Job status tracking works
* Retry and failure handling works
* Automated tests pass
* Swagger documentation is complete
* `.env.example` is available
* README contains setup instructions
* Project structure is clean
* No secrets are committed to Git
* Final project is ready for portfolio / interview discussion

```
```

----------------------------------------------------------------------------------------------------
# 📁 Roadmap-Aligned Project Folder Structure

The project structure should grow progressively throughout the 38-day roadmap.

Do **not** create every folder on Day 1. Create each layer when its corresponding feature is introduced.

---

# Week 1 — Foundation + Database

## After Day 1

```text
smart-content-aggregator/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   └── core/
│       ├── __init__.py
│       └── config.py
│
├── .env
├── .env.example
├── .gitignore
└── requirements.txt
```

### Day 1 creates

* `app/`
* `app/main.py`
* `app/core/`
* `app/core/config.py`
* `.env`
* `.env.example`
* `.gitignore`
* `requirements.txt`

---

## After Day 2 — Logging + Error Handling

```text
app/
├── __init__.py
├── main.py
│
└── core/
    ├── __init__.py
    ├── config.py
    ├── logger.py
    ├── exceptions.py
    └── exception_handlers.py
```

### Added

* `logger.py`
* `exceptions.py`
* `exception_handlers.py`

### Logs

```text
logs/
└── app.log
```

---

## After Day 3 — PostgreSQL + SQLAlchemy

```text
app/
├── __init__.py
├── main.py
│
├── core/
│   ├── __init__.py
│   ├── config.py
│   ├── logger.py
│   ├── exceptions.py
│   └── exception_handlers.py
│
└── db/
    ├── __init__.py
    ├── database.py
    └── base.py
```

### Added

* `app/db/`
* `database.py`
* `base.py`

---

## After Day 4 — Database Models

```text
app/
└── db/
    ├── __init__.py
    ├── database.py
    ├── base.py
    │
    └── models/
        ├── __init__.py
        ├── user.py
        ├── source.py
        ├── article.py
        └── article_file.py
```

### Added

* `models/`
* `user.py`
* `source.py`
* `article.py`
* `article_file.py`

---

## After Day 5 — Alembic

```text
smart-content-aggregator/
│
├── alembic/
│   ├── versions/
│   │   └── .gitkeep
│   ├── env.py
│   ├── script.py.mako
│   └── README
│
├── alembic.ini
│
└── app/
    └── db/
        ├── database.py
        ├── base.py
        └── models/
```

### Added

* `alembic/`
* `alembic/versions/`
* `alembic/env.py`
* `alembic.ini`

---

## After Day 6 — Repository Layer

```text
app/
├── db/
│   ├── database.py
│   ├── base.py
│   └── models/
│       ├── user.py
│       ├── source.py
│       ├── article.py
│       └── article_file.py
│
└── repositories/
    ├── __init__.py
    └── article_repository.py
```

### Added

* `repositories/`
* `article_repository.py`

Only create repositories that are actually required. The roadmap currently starts with the **Article repository**.

---

# Week 2 — Article API + Third-Party Integration

## After Day 8 — Pydantic Schemas

```text
app/
├── schemas/
│   ├── __init__.py
│   └── article.py
│
├── repositories/
│   ├── __init__.py
│   └── article_repository.py
│
└── db/
    └── models/
```

`article.py` contains:

```text
ArticleCreate
ArticleUpdate
ArticleResponse
ArticleListResponse
```

---

## After Day 9 — Article CRUD API

```text
app/
├── api/
│   ├── __init__.py
│   └── articles.py
│
├── services/
│   ├── __init__.py
│   └── article_service.py
│
├── repositories/
│   ├── __init__.py
│   └── article_repository.py
│
└── schemas/
    ├── __init__.py
    └── article.py
```

### Architecture

```text
Client
   ↓
articles.py
   ↓
article_service.py
   ↓
article_repository.py
   ↓
PostgreSQL
```

---

## After Day 10 — Pagination

No new major folder is required.

Add pagination functionality to:

```text
app/
├── services/
│   └── article_service.py
│
├── repositories/
│   └── article_repository.py
│
└── schemas/
    └── article.py
```

If pagination becomes reusable across multiple APIs, then create:

```text
app/
└── utils/
    └── pagination.py
```

---

## After Day 11 — Filtering + Sorting

Continue inside:

```text
app/
├── api/
│   └── articles.py
│
├── services/
│   └── article_service.py
│
└── repositories/
    └── article_repository.py
```

Filtering and sorting primarily belong in the repository/service flow.

---

## After Day 12 — Third-Party API

```text
app/
└── integrations/
    ├── __init__.py
    ├── http_client.py
    └── external_api.py
```

### Added

* `integrations/`
* `http_client.py`
* `external_api.py`

---

## After Day 13 — External API → Database

No new major folder is required.

The flow becomes:

```text
External API
     ↓
external_api.py
     ↓
article_service.py
     ↓
article_repository.py
     ↓
PostgreSQL
```

---

# Week 3 — Crawling + File Upload + Redis

## After Day 15 — Web Crawling Basics

```text
app/
└── crawler/
    ├── __init__.py
    ├── crawler.py
    └── parser.py
```

---

## After Day 16 — Article Crawler

Add source configuration:

```text
app/
└── crawler/
    ├── __init__.py
    ├── crawler.py
    ├── parser.py
    └── sources.py
```

### Flow

```text
Source
  ↓
Crawler
  ↓
Parser
  ↓
Article Schema
  ↓
Article Service
  ↓
Article Repository
  ↓
PostgreSQL
```

---

## After Day 17 — Duplicate Detection

No new folder required.

Modify:

```text
app/
├── repositories/
│   └── article_repository.py
│
├── services/
│   └── article_service.py
│
└── db/
    └── models/
        └── article.py
```

Database uniqueness constraints belong to the model/database layer.

---

## After Day 18 — File Upload

```text
app/
├── api/
│   └── files.py
│
├── services/
│   └── article_file_service.py
│
├── repositories/
│   └── article_file_repository.py
│
└── schemas/
    └── article_file.py
```

Uploaded files:

```text
uploads/
└── .gitkeep
```

---

## After Day 19 — Redis

```text
app/
└── cache/
    ├── __init__.py
    ├── redis.py
    └── cache_service.py
```

### Added

* Redis connection
* Redis service
* `SET`
* `GET`
* `DELETE`
* TTL

---

## After Day 20 — API Caching

Add:

```text
app/
└── cache/
    ├── __init__.py
    ├── redis.py
    ├── cache_service.py
    └── cache_keys.py
```

### Flow

```text
Client
   ↓
Article API
   ↓
Article Service
   ↓
Redis Cache
   │
   ├── HIT → Return response
   │
   └── MISS
        ↓
   Repository
        ↓
   PostgreSQL
```

---

## After Day 21 — Cache Invalidation

Cache invalidation remains primarily in:

```text
app/
├── services/
│   └── article_service.py
│
└── cache/
    ├── redis.py
    ├── cache_service.py
    └── cache_keys.py
```

---

# Week 4 — Rate Limiting + Background Workers

## After Day 22 — Rate Limiting

```text
app/
└── rate_limit/
    ├── __init__.py
    └── limiter.py
```

### Flow

```text
Request
   ↓
Rate Limiter
   ↓
Redis
   ↓
Allow / HTTP 429
```

---

## After Day 23 — Different Rate Limits

Add configuration to:

```text
app/core/config.py
```

Example configuration:

```text
PUBLIC_API_LIMIT
SEARCH_API_LIMIT
UPLOAD_API_LIMIT
CRAWLER_API_LIMIT
RATE_LIMIT_WINDOW
```

---

## After Day 24 — Celery

```text
app/
└── workers/
    ├── __init__.py
    └── celery_app.py
```

### Added

* Celery application
* Redis broker configuration
* Worker configuration

---

## After Day 25 — Background Tasks

```text
app/
└── workers/
    ├── __init__.py
    ├── celery_app.py
    │
    └── tasks/
        ├── __init__.py
        ├── article_tasks.py
        ├── crawler_tasks.py
        └── file_tasks.py
```

### Task responsibilities

```text
article_tasks.py
    → External article fetching

crawler_tasks.py
    → Web crawling

file_tasks.py
    → File processing
```

---

## After Day 26 — Retry + Failure Handling

Modify:

```text
app/
├── workers/
│   ├── celery_app.py
│   └── tasks/
│       ├── article_tasks.py
│       ├── crawler_tasks.py
│       └── file_tasks.py
│
└── core/
    ├── exceptions.py
    └── logger.py
```

---

## After Day 27 — Job Tracking

Add Job model:

```text
app/
└── db/
    └── models/
        └── job.py
```

Add schema:

```text
app/
└── schemas/
    └── job.py
```

Add repository:

```text
app/
└── repositories/
    └── job_repository.py
```

Add service:

```text
app/
└── services/
    └── job_service.py
```

Add API:

```text
app/
└── api/
    └── jobs.py
```

### Job architecture

```text
POST /jobs/crawl
        ↓
    Job Service
        ↓
   Create Job
        ↓
     Celery
        ↓
     Worker
        ↓
Update Job Status
```

---

# Week 5 — Testing + Production Hardening

## After Day 29 — Pytest

```text
tests/
├── __init__.py
├── conftest.py
└── test_health.py
```

### Added

* Test configuration
* Fixtures
* Test database
* First test

---

## After Day 30 — Repository Tests

```text
tests/
├── conftest.py
│
└── unit/
    └── repositories/
        └── test_article_repository.py
```

---

## After Day 31 — Service Tests

```text
tests/
└── unit/
    └── services/
        └── test_article_service.py
```

---

## After Day 32 — API Integration Tests

```text
tests/
└── integration/
    └── api/
        └── test_articles.py
```

---

## After Day 33 — Error Handling Hardening

Modify:

```text
app/
└── core/
    ├── exceptions.py
    ├── exception_handlers.py
    └── logger.py
```

Add tests for:

```text
tests/
├── unit/
│   └── services/
│
└── integration/
    └── api/
```

---

## After Day 34 — CORS + Environment

Modify:

```text
app/
└── core/
    └── config.py
```

And:

```text
.env
.env.example
```

No secrets should be stored in `.env.example`.

---

## After Day 35 — API Documentation

Documentation is primarily added to:

```text
app/api/
```

and schemas:

```text
app/schemas/
```

The main API documentation is automatically exposed through:

```text
/docs
/redoc
```

---

# Final Integration

## After Day 36

At this point the complete structure should exist.

```text
smart-content-aggregator/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── health.py
│   │   ├── articles.py
│   │   ├── files.py
│   │   └── jobs.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── logger.py
│   │   ├── exceptions.py
│   │   └── exception_handlers.py
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── base.py
│   │   └── models/
│   │       ├── __init__.py
│   │       ├── user.py
│   │       ├── source.py
│   │       ├── article.py
│   │       ├── article_file.py
│   │       └── job.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── article.py
│   │   ├── article_file.py
│   │   └── job.py
│   │
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── article_repository.py
│   │   ├── article_file_repository.py
│   │   └── job_repository.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── article_service.py
│   │   ├── article_file_service.py
│   │   └── job_service.py
│   │
│   ├── integrations/
│   │   ├── __init__.py
│   │   ├── http_client.py
│   │   └── external_api.py
│   │
│   ├── crawler/
│   │   ├── __init__.py
│   │   ├── crawler.py
│   │   ├── parser.py
│   │   └── sources.py
│   │
│   ├── cache/
│   │   ├── __init__.py
│   │   ├── redis.py
│   │   ├── cache_service.py
│   │   └── cache_keys.py
│   │
│   ├── rate_limit/
│   │   ├── __init__.py
│   │   └── limiter.py
│   │
│   └── workers/
│       ├── __init__.py
│       ├── celery_app.py
│       └── tasks/
│           ├── __init__.py
│           ├── article_tasks.py
│           ├── crawler_tasks.py
│           └── file_tasks.py
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   ├── script.py.mako
│   └── README
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   │
│   ├── unit/
│   │   ├── repositories/
│   │   │   └── test_article_repository.py
│   │   ├── services/
│   │   │   └── test_article_service.py
│   │   ├── integrations/
│   │   └── crawler/
│   │
│   └── integration/
│       ├── api/
│       │   └── test_articles.py
│       ├── database/
│       ├── redis/
│       └── workers/
│
├── uploads/
│   └── .gitkeep
│
├── logs/
│   └── .gitkeep
│
├── .env
├── .env.example
├── .gitignore
├── alembic.ini
├── requirements.txt
├── pytest.ini
└── README.md
```

---

# Day 37 — Refactoring

Review the structure and check:

*  No unnecessary folders
*  No duplicate functionality
*  Router contains only API concerns
*  Service contains business logic
*  Repository contains database operations
*  Schemas contain validation/serialization
*  Integrations contain external API logic
*  Crawler contains crawling logic
*  Cache contains Redis logic
*  Workers contain background tasks
*  Tests mirror application responsibilities

---

# Day 38 — Final Structure Review

Final checks:

*  Folder structure is clean
*  Imports are organized
*  No circular dependencies
*  No unused files
*  No unnecessary abstractions
*  `.env.example` is complete
*  `requirements.txt` is complete
*  Alembic migrations are correct
*  Test structure is complete
*  README explains project structure
*  Architecture diagram matches actual implementation
*  Swagger documentation matches implemented APIs

---

# 🧭 Final Dependency Direction

The intended dependency direction is:

```text
API Router
    ↓
Service
    ↓
Repository
    ↓
Database
```

Supporting components are accessed where required:

```text
Service
   ├── Repository
   ├── Cache
   ├── Integration
   └── Crawler
```

Background processing:

```text
API
 ↓
Service
 ↓
Celery Task
 ↓
Worker
 ↓
Repository / Crawler / Integration
```

The goal is to keep responsibilities separated without creating folders or abstractions before they are actually needed.
