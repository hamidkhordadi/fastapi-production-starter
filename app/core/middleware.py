import logging
from time import perf_counter
from uuid import uuid4

from fastapi import Request


logger = logging.getLogger(
    "request"
)


async def request_context_middleware(
    request: Request,
    call_next,
):
    request_id = (
        request.headers.get(
            "X-Request-ID"
        )
        or str(uuid4())
    )

    started = perf_counter()

    response = await call_next(
        request
    )

    duration_ms = int(
        (
            perf_counter()
            - started
        )
        * 1000
    )

    response.headers[
        "X-Request-ID"
    ] = request_id

    logger.info(
        (
            f"{request.method} "
            f"{request.url.path} "
            f"{response.status_code} "
            f"{duration_ms}ms"
        ),
        extra={
            "request_id":
                request_id
        },
    )

    return response
