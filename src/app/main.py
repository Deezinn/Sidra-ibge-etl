from pipeline import Extract

from domain.constants.links import APIS

import pandas as pd

class Main:
    def __init__(self, extract: Extract):
        self.__extract: Extract = extract
        
        self.__dispatcher: dict = {
            'quarterly': self.__extract.run_quarterly,
            'monthly': self.__extract.run_monthly,
            'one-month': self.__extract.run_one_monthly,
            'three-month': self.__extract.run_three_monthly,
            'semester': self.__extract.run_semester,
        }
    
    def run(self, apis: dict):
        
        if not apis and not isinstance(apis,dict):
            raise ValueError(f'')
            
        results:list = []
        
        for serie, meta in apis.items():
            
            if not meta['url'] :
                raise ValueError(f'{serie} url empty.')
            elif not meta['period']:
                raise ValueError(f'{serie} period empty.')
        
            period = meta['period']
            url = meta['url']
            
            data:dict = self.__dispatcher[period](url, serie)
            print(f'Série {serie} inicializada a etl')
            results.append({serie: data})
        
        # temp
        for result in results:
            key = next(iter(result.keys()))
            dataframe = pd.DataFrame(result[key])
            dataframe.to_csv(f'../csv/{key}.csv')
            
            
if __name__ == '__main__':
    m = Main(Extract())
    m.run(apis=APIS)