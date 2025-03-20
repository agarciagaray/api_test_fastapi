import uvicorn

from fastapi import FastAPI
from .database.base import Base
from sqlalchemy import create_engine
from .core.config import settings

DATABASE_URL = settings.DATABASE_URL  # Replace with the actual settings attribute for the database URL
engine = create_engine(DATABASE_URL)
from .api.v1.endpoints import auth, users

# Crea las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API IGD Mili",
    version="0.1.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

# Incluye los routers
app.include_router(auth.router)
app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)