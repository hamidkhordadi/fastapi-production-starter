from app.core.settings import Settings


def test_default_settings() -> None:
    settings = Settings(
        _env_file=None
    )

    assert (
        settings.app_name
        == "FastAPI Production Starter"
    )

    assert (
        settings.db_pool_size
        == 5
    )
