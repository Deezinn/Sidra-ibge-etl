from infra.services.extract import LinkGenerator, AsyncExtractor
from domain.constants.links import APIS

import asyncio
import aiohttp

class Extract:
    def __init__(self, linkGenerator: LinkGenerator, apis: dict[str, dict], asyncExtractor: AsyncExtractor):
        self.__async_extract = asyncExtractor.fetch
        self.__apis = apis
        self.__dispatcher = {
            'quarterly': linkGenerator.quarterly,
            'monthly': linkGenerator.monthly,
            'one-month': linkGenerator.one_monthly,
            'three-month': linkGenerator.three_monthly,
            'semester': linkGenerator.semester,
        }

    @staticmethod
    async def _create_context_api(apis: dict, dispatcher: dict) -> dict:
        context: dict = {}

        for serie, cfg in apis.items():
            url: str = cfg['url']
            period: str = cfg['period']
            context[serie] = dispatcher[period](url, serie)
        return context

    async def run(self):
        context = await self._create_context_api(self.__apis, self.__dispatcher)
        semaphore = asyncio.Semaphore(5)

        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=40)
        ) as session:

            async def sem_fetch(url, serie):
                async with semaphore:
                    return await self.__async_extract(
                        session=session,
                        url=url,
                        serie=serie
                    )

            tasks: list = [
                asyncio.create_task(sem_fetch(url, serie))
                for serie, urls in context.items()
                for url in urls
            ]

            results = await asyncio.gather(*tasks)
        return results 
        

