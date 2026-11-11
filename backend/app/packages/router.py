from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.packages import service
from app.packages.schemas import PackageResponse

router = APIRouter(prefix="/api/packages", tags=["Packages"])

DatabaseSession = Annotated[Session, Depends(get_db)]


@router.get("", response_model=list[PackageResponse])
def list_packages(db: DatabaseSession):
    return service.list_packages(db)


@router.get("/{slug}", response_model=PackageResponse)
def get_package(slug: str, db: DatabaseSession):
    try:
        return service.get_package_by_slug(db, slug)
    except service.PackageNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Package not found",
        ) from None