import requests

from datetime import datetime


class Extract():

    def run_quarterly(self, link: str) -> list:
        
        if not isinstance(link, str):
            raise TypeError('')
        
        if not link:
            raise ValueError('')
        
        data:list = []
        
        year_init:int = 2020
        quarter_init:int = 1
                
        now:datetime = datetime.now()
        
        current_quarter:int = (now.month - 1)// 3 + 1
        current_year:int = now.year
                
        link_splitted:list = link.split('/')
        
        if 'first%201' not in link_splitted:
            raise ValueError('link não contém o placeholder "first%201" ')  
        
        index_to_replace:int = link_splitted.index('first%201')
        
        while (year_init,quarter_init) <= (current_year,current_quarter):
            
            if quarter_init > 4:
                quarter_init = 1
                
            if quarter_init == 4:
                year_init += 1
            
            link_splitted[index_to_replace] = f'{year_init}{quarter_init:02d}'
            link_joined:str = '/'.join(link_splitted)
            
            response = requests.get(link_joined)
            response.raise_for_status()
            
            payload = response.json()
            
            if not payload:
                break
            
            data.extend(payload)
                    
            quarter_init += 1
        return data
                
    def run_monthly(self, link: str) -> list:
        
        if not isinstance(link, str):
            raise TypeError('')
        
        if not link:
            raise ValueError('')
        
        data:list = []
        
        year_init:int = 2025
        month_init:int = 1
        
        now:datetime = datetime.now()
        current_year:int = now.year
        current_month:int = now.month
              
        link_splitted:list = link.split('/')
        
        if 'first%201' not in link_splitted:
            raise ValueError('link não contém o placeholder "first%201" ')  
        
        index_to_replace:int = link_splitted.index('first%201')
        
        while (year_init, month_init) <= (current_year, current_month):
            
            if month_init > 12:
                month_init = 1
                year_init += 1
            
            link_splitted[index_to_replace] = f'{year_init}{month_init:02d}'
            link_joined:str = '/'.join(link_splitted)
            
            response = requests.get(link_joined)
            response.raise_for_status()
            
            payload = response.json()
            
            if not payload:
                break
            
            data.extend(payload)
            
            month_init += 1
        return data

    def run_semester(self, link: str) -> list:
        
        if not isinstance(link, str):
            pass
        
        if not link:
            ValueError('')
        
        data:list = []
        
        year_init:int = 2024
        semester_init:int = 1
        
        now:datetime = datetime.now()
        current_semester:int = (now.month - 1) // 6 + 1
        current_year:int = now.year

        link_splitted = link.split('/') 
        
        if 'first%201' not in link_splitted:
            raise ValueError('link não contém o placeholder "first%201" ')  
            
        index_to_replace = link_splitted.index('first%201')
        
        while (year_init, semester_init) <= (current_year, current_semester):
            
            if semester_init > 2:
                semester_init = 1
                year_init += 1 
                
            link_splitted[index_to_replace] = f'{year_init}{semester_init:02d}'
            link_joined = '/'.join(link_splitted)
            
            response = requests.get(link_joined)
            response.raise_for_status()
            
            payload = response.json()
            
            if not payload:
                break
            
            data.extend(payload)
            
            semester_init += 1
        return data
    
    def run_one_monthly(self, link):
        if not isinstance(link, str):
            pass
        
        if not link:
            ValueError('')
            
        response = requests.get(link)
        response.raise_for_status()
        
        return response.json()
    
    def run_three_monthly(self, link):
        
        if not isinstance(link, str):
            ValueError('')
        
        if not link:
            ValueError('')
        
        data:list = []
        
        year_init:int = 2025
        month_init:int = 1
        
        now:datetime = datetime.now()
        current_year = now.year
        current_month = now.month
        
        link_splitted:list = link.split('/')
        index_to_replace:int = link_splitted.index('first%201')
        
        while (year_init, month_init) <= (current_year, current_month):
            if month_init > 12:
                month_init = 1
                year_init += 1
                
            link_splitted[index_to_replace] = f'{year_init}{month_init:02d}'
            link_joined = '/'.join(link_splitted)
            response = requests.get(link_joined)
            payload = response.json()
            
            if not payload:
                break
            
            data.extend(payload)
            
            month_init += 1
        return data