# FastAPI Production Starter

A clean-room production-oriented FastAPI starter demonstrating a practical
backend foundation for containerized services.

## Stack

- FastAPI
- PostgreSQL
- SQLAlchemy 2
- Alembic
- Redis
- Docker Compose
- Pydantic Settings
- Structured JSON logging
- Request ID propagation
- Liveness and readiness endpoints
- Automated tests

## Architecture

Client
  |
  v
FastAPI
  |
  +--> Request ID middleware
  |
  +--> JSON logs
  |
  +--> PostgreSQL / SQLAlchemy
  |
  +--> Redis
  |
  +--> Health / Readiness

Database schema changes are handled by Alembic migrations.

## Health model

`GET /health`

Liveness only. It confirms that the API process is running.

`GET /ready`

Readiness checks PostgreSQL and Redis. It returns HTTP 503 if a required
dependency is unavailable.

This distinction is useful for container orchestration and reverse proxies.

## Run

    docker compose up --build -d

API:

    http://localhost:8084

Documentation:

    http://localhost:8084/docs

## Example

Create an item:

    curl -X POST \
      http://localhost:8084/v1/items \
      -H 'Content-Type: application/json' \
      -d '{"name":"Demo Item"}'

List items:

    curl http://localhost:8084/v1/items

## Migrations

The compose stack runs:

    alembic upgrade head

before the API service starts.

## Production-oriented patterns

- dependency health checks
- DB connection pre-ping
- configurable DB pool sizing
- isolated DB sessions
- migration-driven schema management
- structured logs
- request correlation IDs
- environment-based configuration
- container dependency ordering
- no credentials committed to source

## Privacy

This repository is a standalone clean-room showcase.

It contains no customer data, private infrastructure configuration,
production credentials, or proprietary application code.
