import requests
from src.domain.constants.links.abate import APISABATE
from src.domain.constants.links.ipca import  APISINPC
from datetime import datetime
import json
import pandas as pd


class SidraExtractor():
    def __init__(self) -> None:
        pass
    
    def run(self) -> list:
    
        results:list = []
        
        #temporário
        apis_list:list = [APISINPC, APISABATE]
        
        for apis in apis_list:
            for serie, api in apis.items():
                results.append(self._orchestrator_extract(api, serie))
                            
        return results
    
    def _orchestrator_extract(self, api, serie) -> dict:
        
        if not api:
            pass
        
        if not isinstance(api, dict):
            pass 
        
        content:dict = {}
        
        match api['period']:
            case 'monthly':
                content[serie] = self._extract_monthly(api['url'])
            case 'quarterly':
                content[serie] = self._extract_quarterly(api['url'])
            case _:
                raise ValueError('periodo errado')
        return content
                
    @staticmethod
    def _extract_quarterly(link: str) -> list:
        
        if not isinstance(link, str):
            pass
        
        if not link:
            ValueError('')
        
        data:list = []
        
        year_base:int = 2025
        quarter_base:int = 1
        
        index_time:int = 0
        
        now:datetime = datetime.now()
        year_quarter_now:str = f'{now.year}0{(now.month - 1)// 3 + 1}'
        
        link_splited:list = link.split('/')
        
        if 'first%201' in link_splited:
            index_time:int = link_splited.index('first%201')
            
        while True:
            year_quarter_base:str = f'{year_base}0{quarter_base}'
            
            if quarter_base > 4:
                quarter_base = 1
                year_base += 1
                
            if year_quarter_base == year_quarter_now:
                break
            
            quarter_base += 1

            link_splited[index_time] = year_quarter_base
            link_joined = '/'.join(link_splited)
            
            response = requests.get(link_joined, timeout=30)
            response.raise_for_status()
            data.extend(response.json())
            
        return data
            
            
    @staticmethod
    def _extract_monthly(link: str) -> str:
        if not link:
            ValueError('')
            
        response = requests.get(link, timeout=30)
        response.raise_for_status()
        
        return response.json()

s = SidraExtractor()
s.run()