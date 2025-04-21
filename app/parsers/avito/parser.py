import httpx
from bs4 import BeautifulSoup
from app.models.schemas import PropertyCreate
from app.core.config import settings
from tenacity import retry, stop_after_attempt

class AvitoParser:
    BASE_URL = "https://www.avito.ru"

    @retry(stop=stop_after_attempt(3))
    async def parse_listing(self, city: str) -> list[PropertyCreate]:
        url = f"{self.BASE_URL}/{city}/sdam/na_sutki"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            return self._parse_html(response.text)

    def _parse_html(self, html: str) -> list[PropertyCreate]:
        soup = BeautifulSoup(html, "lxml")
        properties = []
        
        for item in soup.select("[data-marker='item']"):
            try:
                props = {
                    "source": "avito",
                    "external_id": item["data-item-id"],
                    "title": item.select_one("[itemprop='name']").text,
                    "price": float(item.select_one("[itemprop='price']")["content"]),
                    "link": self.BASE_URL + item.select_one("a[data-marker='item-title']")["href"]
                }
                properties.append(PropertyCreate(**props))
            except Exception as e:
                print(f"Error parsing item: {e}")
        return properties
