from sqlalchemy import text

from app.core.redis_client import (
    redis_client,
)
from app.db.database import engine


def database_health() -> bool:
    try:
        with engine.connect() as conn:
            conn.execute(
                text("SELECT 1")
            )

        return True

    except Exception:
        return False


def redis_health() -> bool:
    try:
        return bool(
            redis_client.ping()
        )

    except Exception:
        return False


def readiness() -> dict:
    db_ok = database_health()
    redis_ok = redis_health()

    return {
        "ready": (
            db_ok
            and redis_ok
        ),
        "checks": {
            "database": db_ok,
            "redis": redis_ok,
        },
    }
