from sqlalchemy import create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    sessionmaker,
)

from app.core.settings import (
    get_settings,
)


settings = get_settings()


class Base(DeclarativeBase):
    pass


engine_kwargs: dict = {
    "pool_pre_ping": True,
}

if not settings.database_url.startswith(
    "sqlite"
):
    engine_kwargs.update(
        {
            "pool_size":
                settings.db_pool_size,
            "max_overflow":
                settings.db_max_overflow,
        }
    )


engine = create_engine(
    settings.database_url,
    **engine_kwargs,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)
