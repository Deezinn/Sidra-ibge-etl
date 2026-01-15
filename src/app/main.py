from pipeline import Extract
from infra.services.extract import AsyncExtractor, LinkGenerator

from domain.constants.links import APIS
import asyncio

class Main:
    def __init__(self, extractor: Extract):
        self.__extract = extractor
    
    async def run(self):
       await extractor.run()
            
if __name__ == '__main__':
    extractor = Extract(linkGenerator=LinkGenerator(), apis=APIS, asyncExtractor=AsyncExtractor())
    m = Main(extractor)
    asyncio.run(m.run())