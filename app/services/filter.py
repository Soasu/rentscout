from app.models.schemas import PropertySchema
from typing import List

def filter_properties(properties: List[PropertySchema]) -> List[PropertySchema]:
    return sorted(
        [p for p in properties if p.price > 0],
        key=lambda x: x.price
    )[:1000]