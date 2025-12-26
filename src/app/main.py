from src.pipeline import Extract

from src.domain.constants.links.ipca import  APISINPC

import pandas as pd 

class Main:
    def __init__(self, extract: Extract):
        self.__extract: Extract = extract
        self.__dispatcher: dict = {
            'monthly': self.__extract.run_monthly,
            'quarterly': self.__extract.run_quarterly
        }
    
    def run(self, apis: list[dict]):
        results:list = []
        
        for api in apis:
            for serie, meta in api.items():
                period = meta['period']
                url = meta['url']
                
                data:dict = self.__dispatcher[period](url)
                results.append({serie: data})
                
if __name__ == '__main__':
    m = Main(Extract())
    m.run([APISINPC])