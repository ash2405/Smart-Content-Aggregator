# Smart Content Aggregator API — 5 Week Roadmap

**Daily Time:** 2 Hours  
**Duration:** ~5 Weeks  
**Total:** ~60 Hours  
**Sunday:** Revision / Catch-up / Rest

---

# Week 1 — Foundation + Database

## Day 1 — Project Setup

- Create project
- Create virtual environment
- Install FastAPI + dependencies
- Create project folder structure
- Configure `.env`
- Setup `pydantic-settings`
- Create FastAPI application
- Create `/health` endpoint
- Setup Git / `.gitignore`

---

## Day 2 — Logging & Error Handling

- Setup Loguru
- Configure application logging
- Create log files
- Add request logging
- Create custom exceptions
- Create global exception handlers
- Standardize error response

---

## Day 3 — PostgreSQL + SQLAlchemy

- Configure PostgreSQL
- Create async SQLAlchemy engine
- Create `AsyncSession`
- Create `Base`
- Create `get_db()`
- Configure database environment variables

---

## Day 4 — Database Models

- Create User model
- Create Source model
- Create Article model
- Create ArticleFile model
- Configure relationships
- Add indexes / constraints
- Review model design

---

## Day 5 — Alembic

- Initialize Alembic
- Configure `alembic/env.py`
- Configure async migrations
- Create first migration
- Run `upgrade`
- Test `downgrade`
- Verify database tables

---

## Day 6 — Repository Layer

- Create repository structure
- Create Article repository
- Implement `create()`
- Implement `get()`
- Implement `list()`
- Implement `update()`
- Implement `delete()`

---

## Day 7 — Week 1 Review

- Review project architecture
- Test database connection
- Test CRUD repository methods
- Fix issues
- Refactor code
- Review async SQLAlchemy

---

# Week 2 — Article API + Third-Party Integration

## Day 8 — Pydantic Schemas

- Create `ArticleCreate` schema
- Create `ArticleUpdate` schema
- Create `ArticleResponse` schema
- Create `ArticleListResponse` schema
- Add validation
- Configure `from_attributes`
- Add response examples

---

## Day 9 — Article CRUD API

- Create Article router
- `POST /articles`
- `GET /articles`
- `GET /articles/{id}`
- `PATCH /articles/{id}`
- `DELETE /articles/{id}`
- Connect Router → Service → Repository

---

## Day 10 — Pagination

- Implement page-based pagination
- Add `page`
- Add `limit`
- Return total count
- Validate pagination parameters
- Test pagination

---

## Day 11 — Filtering + Sorting

- Filter by source
- Filter by category
- Filter by status
- Search articles
- Sort by created date
- Sort ascending / descending
- Validate sort parameters

---

## Day 12 — Third-Party API Integration

- Setup HTTPX
- Create integration layer
- Configure API URL
- Configure API key
- Implement API request
- Configure timeout
- Handle API errors
- Handle connection failures

---

## Day 13 — External API → Database

- Fetch external articles
- Validate response
- Transform external data
- Check duplicate articles
- Save articles to database
- Handle partial failures

---

## Day 14 — Week 2 Review

- Test Article APIs
- Test pagination
- Test filtering
- Test sorting
- Test third-party API
- Review Router → Service → Repository architecture

---

# Week 3 — Crawling + File Upload + Redis

## Day 15 — Web Crawling Basics

- Understand HTML structure
- Setup BeautifulSoup
- Make HTTP requests
- Parse HTML
- Extract title
- Extract content
- Extract image / URL
- Respect `robots.txt` and site rules

---

## Day 16 — Article Crawler

- Create crawler module
- Create source configuration
- Fetch website
- Parse articles
- Extract required fields
- Convert crawler data to Article schema
- Save crawled articles

---

## Day 17 — Duplicate Detection

- Define unique article identifier
- Handle duplicate URLs
- Add database constraint / index
- Implement duplicate checking
- Handle duplicate insert errors
- Test duplicate crawling

---

## Day 18 — File Upload

- Create upload endpoint
- Use `UploadFile`
- Validate file size
- Validate content type
- Validate extension
- Generate safe filename
- Save file
- Store file metadata
- Create file delete endpoint

---

## Day 19 — Redis Setup

- Setup Redis
- Configure `REDIS_URL`
- Connect FastAPI with Redis
- Create Redis service
- Implement `SET`
- Implement `GET`
- Implement `DELETE`
- Implement TTL
- Handle Redis connection errors

---

## Day 20 — API Caching

- Cache Article list
- Cache Article details
- Create cache keys
- Serialize response data
- Configure TTL
- Return cached response
- Test cache hit
- Test cache miss

---

## Day 21 — Cache Invalidation + Review

- Invalidate cache on create
- Invalidate cache on update
- Invalidate cache on delete
- Test cache consistency
- Review Redis implementation
- Review crawler
- Review file upload

---

# Week 4 — Rate Limiting + Background Workers

## Day 22 — Rate Limiting

- Design rate limiting
- Implement Redis-based rate limiter
- Limit requests per IP
- Configure request window
- Return HTTP 429
- Add rate-limit headers
- Test rate limiting

---

## Day 23 — Different Rate Limits

- Public API limit
- Search API limit
- Upload API limit
- Crawler trigger limit
- Configure limits using environment variables
- Test different limits

---

## Day 24 — Celery Setup

- Install Celery
- Configure Celery
- Configure Redis broker
- Create Celery application
- Create worker
- Run worker
- Create first task

---

## Day 25 — Background Jobs

- External article fetch task
- Crawler task
- File processing task
- Trigger background job from API
- Return task / job ID
- Test worker execution

---

## Day 26 — Celery Retry & Failure Handling

- Configure task timeout
- Configure retries
- Configure retry delay
- Handle external API failure
- Handle crawler failure
- Handle task exceptions
- Log worker failures

---

## Day 27 — Job Status

- Create Job model
- Create job status enum
- `POST /jobs/crawl`
- `GET /jobs/{job_id}`
- Implement pending status
- Implement running status
- Implement completed status
- Implement failed status

---

## Day 28 — Week 4 Integration

- FastAPI + Redis
- FastAPI + Celery
- Celery + Redis
- Worker + Database
- Crawler + Worker
- External API + Worker
- Test complete background workflow

---

# Week 5 — Testing + Production Hardening

## Day 29 — Pytest Setup

- Install pytest
- Install pytest-asyncio
- Create `tests/`
- Create test configuration
- Create fixtures
- Configure test database
- Write first test

---

## Day 30 — Repository Tests

- Test create
- Test get
- Test list
- Test update
- Test delete
- Test not-found cases
- Test duplicate cases

---

## Day 31 — Service Tests

- Test business logic
- Test duplicate article handling
- Test source validation
- Test cache behavior
- Test external API failure
- Test crawler failure

---

## Day 32 — API Integration Tests

- Test POST Article
- Test GET Articles
- Test GET Article
- Test PATCH Article
- Test DELETE Article
- Test pagination
- Test filtering
- Test validation errors
- Test 404 responses

---

## Day 33 — Error Handling Hardening

- Standardize API errors
- Handle validation errors
- Handle database errors
- Handle Redis errors
- Handle external API errors
- Handle crawler errors
- Handle unexpected exceptions
- Add proper logging
- Hide sensitive error details

---

## Day 34 — CORS + Environment Configuration

- Configure CORS
- Configure allowed origins
- Configure environment variables
- Create `.env.example`
- Remove hardcoded secrets
- Configure production settings
- Review security configuration

---

## Day 35 — API Documentation

- Clean Swagger documentation
- Add API tags
- Add endpoint summaries
- Add endpoint descriptions
- Add response models
- Add status codes
- Add request examples
- Add response examples
- Document error responses

---

# Final Integration + Buffer

## Day 36 — Full System Testing

- Test complete Article flow
- Test Redis caching
- Test rate limiting
- Test background workers
- Test crawler
- Test third-party API
- Test file upload
- Test database migrations
- Run complete test suite

---

## Day 37 — Refactoring

- Remove duplicate code
- Improve naming
- Improve project structure
- Review services
- Review repositories
- Review database queries
- Review async code
- Improve logging
- Fix remaining bugs

---

## Day 38 — Final Project Review

- Final folder structure review
- Final `.env.example`
- Final `requirements.txt`
- Final Alembic migrations
- Final pytest suite
- Final Swagger documentation
- Create README
- Add setup instructions
- Add architecture diagram
- Add API documentation
- Final Git cleanup

---

# Final Feature Checklist

## Backend

- FastAPI
- PostgreSQL
- SQLAlchemy Async
- Repository Pattern
- Service Layer
- Pydantic
- Alembic

## Redis & Performance

- Redis
- Redis Caching
- Cache Invalidation
- Rate Limiting
- Pagination
- Filtering
- Sorting
- Search

## Background Processing

- Celery
- Background Workers
- Retry Mechanism
- Job Tracking
- Task Failure Handling

## External Integrations

- Third-party API Integration
- HTTPX
- Web Crawling
- BeautifulSoup
- Duplicate Detection

## File Handling

- File Upload
- File Validation
- File Metadata
- Safe File Names
- File Delete

## Testing

- Pytest
- pytest-asyncio
- Unit Tests
- Repository Tests
- Service Tests
- API Integration Tests
- Async Testing
- Test Database

## Error Handling & Security

- Logging
- Custom Exceptions
- Global Error Handling
- CORS
- Environment Configuration
- `.env.example`
- Secret Management
- Sensitive Error Protection

## API Documentation

- Swagger / OpenAPI
- API Tags
- Endpoint Summaries
- Endpoint Descriptions
- Request Examples
- Response Examples
- Status Codes
- Error Documentation

## Final Project

- README
- Setup Instructions
- Architecture Diagram
- Final Folder Structure
- Final Requirements
- Final Alembic Migrations
- Final Test Suite
- Final Swagger Documentation
- Git Cleanup
- Final Project Review

---

# Project Architecture

```text
                         Client
                           │
                           ▼
                    ┌─────────────┐
                    │   FastAPI   │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
        Rate Limiter     Cache       Router
              │            │            │
              └────────────┼────────────┘
                           │
                           ▼
                    Service Layer
                           │
                           ▼
                  Repository Layer
                           │
                           ▼
                     PostgreSQL
                           │
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
      Redis              Celery          External APIs
        │                  │                  │
        │                  ▼                  │
        │              Workers                │
        │                  │                  │
        │          ┌───────┴───────┐          │
        │          ▼               ▼          │
        │       Crawler      File Processing  │
        │                                      │
        └──────────────────────────────────────┘