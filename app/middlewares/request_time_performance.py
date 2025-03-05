from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import time
import logging

logger = logging.getLogger("uvicorn")


class RequestTimePerformanceMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        logger.info(f"Processed request in {process_time:.4f} seconds")
        return response
