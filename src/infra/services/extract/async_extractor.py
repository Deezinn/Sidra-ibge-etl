import aiohttp

class AsyncExtractor:
    async def fetch(self, session: aiohttp.ClientSession, url: str, serie: str) -> dict:
        async with session.get(url) as response:
            data = await response.json()
            return {
                "serie": serie,
                "data": data
            }