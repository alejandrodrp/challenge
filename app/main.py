from fastapi import FastAPI
from app.controllers.central_router import central_router
from app.middlewares.request_time_performance import RequestTimePerformanceMiddleware

app = FastAPI()

# Middlewares
app.add_middleware(RequestTimePerformanceMiddleware)

# Rutas
app.include_router(central_router)
