# from fastapi import FastAPI
# from app.api.routes.research_routes import router as research_router
# from app.api.routes.system_routes import router as system_router
# from app.database.base import Base
# from app.database.connection import engine



# app = FastAPI(
#     title="ResearchOS API",
#     description="Production-grade AI Research Assistant",
#     version="1.0.0",
# )

# Base.metadata.create_all(bind=engine)

# app.include_router(research_router, prefix="/api/v1")
# app.include_router(system_router, prefix="/api/v1")





from fastapi import FastAPI
from slowapi import Limiter 
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
from app.api.routes.research_routes import router as research_router
import os
from app.config.settings import get_settings

print("hello")
settings = get_settings()
print("loaded")
os.environ["LANGSMITH_API_KEY"] = settings.LANGSMITH_API_KEY
os.environ["LANGCHAIN_TRACING_V2"] = str(settings.LANGCHAIN_TRACING_V2).lower()
os.environ["LANGSMITH_PROJECT"] = settings.LANGSMITH_PROJECT


print(os.environ.get("LANGSMITH_API_KEY"))
print(os.environ.get("LANGCHAIN_TRACING_V2"))
print(os.environ.get("LANGSMITH_PROJECT"))


limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter

app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)


app.include_router(
    research_router,
    prefix="/api/v1"
)



# DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5433/researchos
# DATABASE_URL=postgresql+psycopg2://postgres:postgres@db:5432/researchos