
class Orquestrator:
    def __init__(self, extract):
        self.__extract = extract
    
    async def teste(self):
        await self.__extract.run()
        
        
