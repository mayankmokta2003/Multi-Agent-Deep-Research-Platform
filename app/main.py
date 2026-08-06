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