import logging
from contextlib import asynccontextmanager


from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.database.connection import engine
from app.packages.router import router as packages_router

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    engine.dispose()


app = FastAPI(
    title="Travel Agency API",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(packages_router)


@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}


@app.get("/ready", tags=["Health"])
def readiness():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except SQLAlchemyError:
        logger.warning("Database readiness check failed")
        raise HTTPException(
            status_code=503,
            detail="Database unavailable",
        ) from None

    return {"status": "ready", "database": "connected"}