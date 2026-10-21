from fastapi import FastAPI

from app.api.routes import router
from app.core.logging import (
    configure_logging,
)
from app.core.middleware import (
    request_context_middleware,
)
from app.core.settings import (
    get_settings,
)


settings = get_settings()

configure_logging(
    settings.log_level
)

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description=(
        "Production-oriented FastAPI "
        "starter with PostgreSQL, Redis, "
        "Alembic, readiness checks, "
        "request IDs and JSON logging."
    ),
)

app.middleware("http")(
    request_context_middleware
)

app.include_router(router)
