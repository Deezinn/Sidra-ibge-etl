
class Orquestrator:
    def __init__(self, extract):
        self.__extract = extract
    
    async def teste(self):
        extract = await self.__extract.run()

        
