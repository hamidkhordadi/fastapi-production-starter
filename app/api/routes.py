from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.health import readiness
from app.db.dependencies import get_db
from app.models.item import Item
from app.schemas.item import (
    ItemCreate,
    ItemRead,
)


router = APIRouter()


@router.get("/health")
def health() -> dict:
    return {
        "status": "ok"
    }


@router.get("/ready")
def ready() -> dict:
    result = readiness()

    if not result["ready"]:
        raise HTTPException(
            status_code=503,
            detail=result,
        )

    return result


@router.post(
    "/v1/items",
    response_model=ItemRead,
)
def create_item(
    payload: ItemCreate,
    db: Session = Depends(get_db),
) -> Item:
    item = Item(
        name=payload.name
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item


@router.get(
    "/v1/items",
    response_model=list[ItemRead],
)
def list_items(
    db: Session = Depends(get_db),
) -> list[Item]:
    statement = (
        select(Item)
        .order_by(Item.id.desc())
    )

    return list(
        db.scalars(statement)
    )
