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
                
        now:datetime = datetime.now()
        year_quarter_now:str = f'{now.year}0{(now.month - 1)// 3 + 1}'
        
        link_splitted:list = link.split('/')
        
        if 'first%201' not in link_splitted:
            raise ValueError('link não contém o placeholder "first%201" ')  
        
        index_to_replace:int = link_splitted.index('first%201')
            
        while True:
            year_quarter_base:str = f'{year_base}0{quarter_base}'
            
            if quarter_base > 4:
                quarter_base = 1
                year_base += 1
                
            link_splitted[index_to_replace] = year_quarter_base
            link_joined = '/'.join(link_splitted)
            
            response = requests.get(link_joined, timeout=60)
            response.raise_for_status()
            
            data.extend(response.json())
            
            if year_quarter_base == year_quarter_now:
                break
            
            quarter_base += 1

            
        return data
            
    def run_monthly(self, link: str) -> list:
        
        if not isinstance(link, str):
            ValueError('')
        
        if not link:
            ValueError('')
        
        data:list = []
        
        year_base:int = 2025
        month_base:int = 1
        
        now:datetime = datetime.now()
        year_month_now:str = f'{now.year}{now.month}'
        
        link_splitted:list = link.split('/')
        
        if 'first%201' not in link_splitted:
            raise ValueError('link não contém o placeholder "first%201" ')  
        
        index_to_replace:int = link_splitted.index('first%201')
        
        while True:
            year_month_base:str = f'{year_base}{month_base:02d}'
            
            if month_base > 12:
                month_base = 1
                year_base += 1
            
            link_splitted[index_to_replace] = year_month_base
            link_joined = '/'.join(link_splitted)
            
            response = requests.get(link_joined, timeout=60)
            response.raise_for_status()
            
            data.extend(response.json())
            
            if year_month_base == year_month_now:
                break
            
            month_base += 1
        
        return data

    def run_semester(self, link: str) -> list:
        
        if not isinstance(link, str):
            pass
        
        if not link:
            ValueError('')
        
        data:list = []
        
        year_base:int = 2023
        semester_base:int = 1
        
        now:datetime = datetime.now()
        semester_now:int = (now.month - 1) // 6 + 1
        year_semester_now:str = f'{now.year}0{semester_now}'

        link_splitted = link.split('/') 
        
        if 'first%201' not in link_splitted:
            raise ValueError('link não contém o placeholder "first%201" ')  
            
        index_to_replace = link_splitted.index('first%201')
        
        while True:
            if semester_base > 2:
                semester_base = 1
                year_base += 1    
            
            year_semester_base = f'{year_base}0{semester_base}'
            
            link_splitted[index_to_replace] = year_semester_base
            link_joined = '/'.join(link_splitted)
            
            response = requests.get(link_joined, timeout=60)
            response.raise_for_status()
            payload = response.json()
            
            if not payload:
                break
            
            data.extend(payload)
            
            if year_semester_base == year_semester_now :
                break
            
            semester_base += 1
                        
        return data
    
    def run_one_monthly(self, link):
        if not isinstance(link, str):
            pass
        
        if not link:
            ValueError('')
            
        response = requests.get(link, timeout=60)
        response.raise_for_status()
        
        return response.json()
    
    def run_three_monthly(self, link):
        
        if not isinstance(link, str):
            ValueError('')
        
        if not link:
            ValueError('')
        
        data:list = []
        
        year_base:int = 2023
        month_base:int = 1
        
        now:datetime = datetime.now()
        year_month_now:str = f'{now.year}{now.month}'
        
        link_splitted:list = link.split('/')
        index_to_replace:int = link_splitted.index('first%201')
        
        while True:
            year_month_base:str = f'{year_base}{month_base:02d}'
            
            if month_base >= 12:
                month_base = 1
                year_base += 1
            
            link_splitted[index_to_replace] = year_month_base
            link_joined = '/'.join(link_splitted)
            
            response = requests.get(link_joined, timeout=60)
            response.raise_for_status()
            
            data.extend(response.json())
            
            if year_month_base == year_month_now:
                break
            
            month_base += 1
        
        return data