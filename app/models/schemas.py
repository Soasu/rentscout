from pydantic import BaseModel
from typing import Optional

class PropertyBase(BaseModel):
    source: str
    external_id: str
    title: str
    price: float
    rooms: Optional[int]
    area: Optional[float]
    location: Optional[dict]
    photos: list[str] = []

class PropertyCreate(PropertyBase):
    pass

class Property(PropertyBase):
    id: str
    
    class Config:
        orm_mode = True
