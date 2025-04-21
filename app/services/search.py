from typing import List
from app.models.schemas import PropertyCreate, Property
from app.parsers.avito.parser import AvitoParser
from app.parsers.cian.parser import CianParser
from app.db.crud import save_properties

class SearchService:
    def __init__(self):
        self.parsers = [AvitoParser(), CianParser()]

    async def search(self, city: str) -> List[Property]:
        all_properties = []
        for parser in self.parsers:
            try:
                results = await parser.parse_listing(city)
                all_properties.extend(results)
            except Exception as e:
                print(f"Parser {parser.__class__.__name__} failed: {e}")
        
        await save_properties(all_properties)
        return all_properties
