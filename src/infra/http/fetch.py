import aiohttp


class AsyncExtractor:
    TIMEOUT = 5
    """
    _summary_
    """
    async def fetch(self, session: aiohttp.ClientSession, url: str, serie: str) -> dict:
        async with session.get(url=url, timeout=self.TIMEOUT) as response: # pyright: ignore[reportArgumentType]
            data: dict = await response.json()
            response.raise_for_status()
            return {"serie": serie, "data": data}
