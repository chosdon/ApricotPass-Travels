from sqlalchemy.orm import Session

from app.packages import repository
from app.packages.schemas import PackageResponse


class PackageNotFoundError(Exception):
    """The requested package is unavailable to the public."""


def list_packages(db: Session) -> list[PackageResponse]:
    packages = repository.list_published_packages(db)

    return [
        PackageResponse.model_validate(package)
        for package in packages
    ]


def get_package_by_slug(
    db: Session,
    slug: str,
) -> PackageResponse:
    package = repository.find_published_package_by_slug(db, slug)

    if package is None:
        raise PackageNotFoundError(slug)

    return PackageResponse.model_validate(package)