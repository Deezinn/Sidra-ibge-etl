import requests

from datetime import datetime


class Extract():

    def run_quarterly(self, link: str) -> list:
        
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
            
    def run_monthly(self, link: str) -> str:
        
        if not isinstance(list, str):
            pass
        
        if not link:
            ValueError('')
            
        response = requests.get(link, timeout=30)
        response.raise_for_status()
        
        return response.json()

    def run_semester(self, link: str) -> dict:
        
        if not isinstance(list, str):
            pass
        
        if not link:
            ValueError('')
            
        response = requests.get(link, timeout=30)
        response.raise_for_status()
        
        return response.json()
    
    def run_one_monthly(self, link):
        if not isinstance(list, str):
            pass
        
        if not link:
            ValueError('')
            
        response = requests.get(link, timeout=30)
        response.raise_for_status()
        
        return response.json()
    
    def run_three_monthly(self, link):
        if not isinstance(list, str):
            pass
        
        if not link:
            ValueError('')
            
        response = requests.get(link, timeout=30)
        response.raise_for_status()
        
        return response.json()