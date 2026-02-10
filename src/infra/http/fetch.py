import aiohttp


class AsyncExtractor:
    TIMEOUT = 5
    """
    _summary_
    """
    async def fetch(self, session: aiohttp.ClientSession, url: str, serie: str) -> dict:
        async with session.get(url=url, timeout=self.TIMEOUT) as response:
            print('Processo iniciado')
            data: dict = await response.json()
            print(f'extraindo {serie} status: {response.status}')
            response.raise_for_status()
            print('processo finalizado')
            return {"serie": serie, "data": data}
