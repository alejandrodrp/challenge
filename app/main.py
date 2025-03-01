from fastapi import FastAPI
from app.controllers.central_router import central_router

app = FastAPI()

# Incluir el router central en la aplicación FastAPI
app.include_router(central_router)
