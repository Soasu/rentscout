from fastapi import APIRouter, Depends, Query, HTTPException
from app.dependencies.parsers import get_parsers
from app.models.schemas import PropertySchema
from app.services.filter import filter_properties
from app.services.cache import cache
from app.utils.logger import logger

router = APIRouter()

@router.get("/properties", response_model=list[PropertySchema])
@cache(expire=300)
async def get_properties(
    city: str = Query(..., min_length=2),
    property_type: str = Query("Квартира"),
    parsers: list = Depends(get_parsers)
):
    try:
        all_properties = []
        for parser in parsers:
            try:
                data = await parser.parse(city, {"type": property_type})
                all_properties.extend(data)
            except Exception as e:
                logger.error(f"Parser {parser.__class__.__name__} failed: {str(e)}")
        
        return filter_properties(all_properties)
    
    except Exception as e:
        logger.critical(f"API Error: {str(e)}")
        raise HTTPException(500, "Internal Server Error")