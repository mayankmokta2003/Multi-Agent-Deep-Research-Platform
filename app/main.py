from fastapi import FastAPI
from app.api.routes.research_routes import router as research_router
from app.api.routes.system_routes import router as system_router
from app.database.base import Base
from app.database.connection import engine
from app.models.research_model import Research

app = FastAPI(
    title="ResearchOS API",
    description="Production-grade AI Research Assistant",
    version="1.0.0",
)

Base.metadata.create_all(bind=engine)

app.include_router(research_router, prefix="/api/v1")
app.include_router(system_router, prefix="/api/v1")
