import time
import uuid

from fastapi import Request
from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware


class RequestLoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id

        start_time = time.perf_counter()

        try:
            response = await call_next(request)

            duration = time.perf_counter() - start_time

            logger.info(
                "request_id={} method={} path={} status_code={} duration_ms={:.2f}",
                request_id,
                request.method,
                request.url.path,
                response.status_code,
                duration * 1000,
            )

            response.headers["X-Request-ID"] = request_id

            return response

        except Exception:
            duration = time.perf_counter() - start_time

            logger.exception(
                "request_id={} method={} path={} duration_ms={:.2f}",
                request_id,
                request.method,
                request.url.path,
                duration * 1000,
            )

            raise