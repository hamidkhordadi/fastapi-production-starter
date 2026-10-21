from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_liveness() -> None:
    response = client.get(
        "/health"
    )

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok"
    }


def test_request_id_header() -> None:
    response = client.get(
        "/health",
        headers={
            "X-Request-ID":
                "test-request-123"
        },
    )

    assert (
        response.headers[
            "X-Request-ID"
        ]
        == "test-request-123"
    )
