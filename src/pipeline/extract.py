import asyncio

import aiohttp


class Extract:
    """
    Classe base de extração das apis
    """
    def __init__(self, link_generator, apis, async_extractor, link_validator) -> None:
        self.__dispatcher = {
              'quarterly': link_generator._quarterly,
              'monthly': link_generator._monthly,
              'one-month': link_generator._one_monthly,
              'three-month': link_generator._three_monthly,
              'semester': link_generator._semester,
        }
        self.__apis = apis
        self.__async_extractor = async_extractor
        self.__link_validator = link_validator
        

    @staticmethod
    def __create_context_link_by_date(apis: dict[str, dict], dispatcher: dict, link_validator):
        """
        Método estático que terá a função de gerar os links a partir de uma data default
        até a data atual, com validações inclusas.
        """
        context: dict[str, list] = {}
        
        try:
            for serie, cfg in apis.items():
                url:str = cfg['url']
                period:str = cfg['period']
                
                link_validator._link_is_valid(url, serie)
                link_validator._validate_inputs(url, serie)
                
                context[serie] = dispatcher[period](url,serie)
        except Exception:
                pass
            
        return context

    async def run(self):
        context: dict = self.__create_context_link_by_date(apis=self.__apis,
                                                     dispatcher=self.__dispatcher,
                                                     link_validator= self.__link_validator)

        async with aiohttp.ClientSession() as session:
            tasks = [
                self.__async_extractor.fetch(session=session,serie=serie, url=cfg[0])
                for serie, cfg in context.items()]
            return await asyncio.gather(*tasks, return_exceptions=True)
            
        
