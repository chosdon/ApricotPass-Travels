from pydantic import BaseModel, ConfigDict, Field


class PackageResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    slug: str
    title: str = Field(min_length=1, max_length=150)
    duration_days: int = Field(gt=0)
    duration_nights: int = Field(ge=0)
    description: str = Field(min_length=1)