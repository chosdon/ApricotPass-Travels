from app.packages.schemas import PackageResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.packages.models import Package


def list_published_packages(db: Session) -> list[Package]:
    statement = (
        select(Package)
        .where(Package.publication_status == "published")
        .order_by(Package.id)
    )

    return list(db.scalars(statement).all())


def find_published_package_by_slug(
    db: Session,
    slug: str,
) -> Package | None:
    statement = select(Package).where(
        Package.slug == slug,
        Package.publication_status == "published",
    )

    return db.scalar(statement)


def list_packages() -> list[PackageResponse]:
    return [package.model_copy(deep=True) for package in _SAMPLE_PACKAGES]


def find_package_by_slug(slug: str) -> PackageResponse | None:
    for package in _SAMPLE_PACKAGES:
        if package.slug == slug:
            return package.model_copy(deep=True)

    return None