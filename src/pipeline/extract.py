import requests
from src.domain.constants import APISABATE
from datetime import datetime
import json
import pandas as pd
class Extract():
    def __init__(self, api: dict) -> None:
        self.__api = api
    
    def extract_quarter_api(self) -> dict:
        yearBase = 2025 # menor valor 1997
        quarter = 1
        
        now = datetime.now()
        year_and_quarter = f'{now.year}0{((now.month - 1) // 3 + 1)}'
        
        content_serie = {}
        content_temp = []
    
        for serie, api in self.__api.items():
            year = yearBase
            quarter = 1
            
            while True:
                year_and_quarter_base = f'{year}0{quarter}'
                
                api_splitted = api.split('/')
                index_to_replace = api_splitted.index('first%201')
                
                api_splitted[index_to_replace] = year_and_quarter_base
                api_joined = '/'.join(api_splitted)
                
                r = requests.get(api_joined, timeout=30)
                
                if r.status_code == 200:
                    content_temp.extend(r.json())
                else:
                    r.raise_for_status()
                    break
                
                if year_and_quarter_base == year_and_quarter:
                    break
                
                quarter += 1
                
                if quarter > 4:
                    quarter =  1
                    year += 1
                
            content_serie[serie] = content_temp
        return content_serie    
    
    def extract_month_api(self):
        pass
    