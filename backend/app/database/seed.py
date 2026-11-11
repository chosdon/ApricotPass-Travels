from sqlalchemy.dialects.postgresql import insert

from app.database.connection import SessionLocal
from app.packages.models import Package

SAMPLE_PACKAGES = [
    {
        "id": "PKG-001",
        "slug": "leh-tour",
        "title": "Leh Tour",
        "duration_days": 5,
        "duration_nights": 4,
        "description": "A sample itinerary exploring Leh and nearby places.",
        "publication_status": "published",
    },
    {
        "id": "PKG-002",
        "slug": "leh-nubra-tour",
        "title": "Leh–Nubra Tour",
        "duration_days": 6,
        "duration_nights": 5,
        "description": "A sample journey through Leh and Nubra Valley.",
        "publication_status": "published",
    },
    {
        "id": "PKG-003",
        "slug": "leh-nubra-pangong-tour",
        "title": "Leh–Nubra–Pangong Tour",
        "duration_days": 7,
        "duration_nights": 6,
        "description": "A sample journey through Leh, Nubra, and Pangong.",
        "publication_status": "published",
    },
]


def seed():
    statement = (
        insert(Package)
        .values(SAMPLE_PACKAGES)
        .on_conflict_do_nothing()
        .returning(Package.id)
    )

    with SessionLocal.begin() as db:
        inserted_ids = db.execute(statement).scalars().all()

    print(f"Inserted {len(inserted_ids)} sample packages.")


if __name__ == "__main__":
    seed()