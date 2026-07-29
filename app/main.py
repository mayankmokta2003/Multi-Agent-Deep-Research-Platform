from fastapi import FastAPI
from app.api.routes.research_routes import router as research_router

app = FastAPI(
    title="ResearchOS API",
    description="Production-grade AI Research Assistant",
    version="1.0.0",
)

app.include_router(research_router, prefix="/api/v1")
