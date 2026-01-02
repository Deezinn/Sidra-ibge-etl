from datetime import datetime

import requests
from requests.exceptions import InvalidJSONError

class Extract():

    @staticmethod
    def _link_is_valid(link: str, serie: str):
        """
        Verifica se o link está batendo com a série
        
        :param link: recebe o link da constante
        :type link: str
        :param serie: recebe a serie da constante
        :type serie: str
        """
        
        link_splitted:list = link.split('/')
        serie_splitted:list = serie.split('_')
        
        for value in serie_splitted:
            if value.isdigit():
                if value in link_splitted:
                    continue
                else:
                    raise ValueError(f'{value} invalido da {serie} serie')

    def run_quarterly(self, link: str, serie: str) -> list:
        self._link_is_valid(link=link, serie=serie)
        
        if not isinstance(link, str):
            raise TypeError('')
        
        if not link:
            raise ValueError('')
        
        data:list = []
        
        year_init:int = 2025
        quarter_init:int = 1
                
        now:datetime = datetime.now()
        
        current_quarter:int = (now.month - 1)// 3 + 1
        current_year:int = now.year
                
        link_splitted:list = link.split('/')
        
        if 'first%201' not in link_splitted:
            raise ValueError(f'link não contém o placeholder "first%201" {serie}')  
        
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
                raise InvalidJSONError('')
            
            data.extend(payload)
                    
            quarter_init += 1
        return data
                
    def run_monthly(self, link: str, serie: str) -> list:
        self._link_is_valid(link=link, serie=serie)
        
        if not isinstance(link, str):
            raise TypeError('')
        
        if not link:
            raise ValueError('')
        
        data:list = []
        
        year_init:int = 2020
        month_init:int = 1
        
        now:datetime = datetime.now()
        current_year:int = now.year
        current_month:int = now.month
              
        link_splitted:list = link.split('/')
        
        if 'first%201' not in link_splitted:
            raise ValueError(f'link não contém o placeholder "first%201" {serie}')  
        
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
                raise InvalidJSONError('')
            
            data.extend(payload)
            
            month_init += 1
        return data

    def run_semester(self, link: str, serie: str) -> list:
        self._link_is_valid(link=link, serie=serie)
        
        if not isinstance(link, str):
            pass
        
        if not link:
            ValueError('')
        
        data:list = []
        
        year_init:int = 2020
        semester_init:int = 1
        
        now:datetime = datetime.now()
        current_semester:int = (now.month - 1) // 6 + 1
        current_year:int = now.year

        link_splitted = link.split('/') 
        
        if 'first%201' not in link_splitted:
            raise ValueError(f'link não contém o placeholder "first%201" {serie}')  
            
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
                raise InvalidJSONError('')
            
            data.extend(payload)
            
            semester_init += 1
        return data
    
    def run_one_monthly(self, link, serie: str):
        self._link_is_valid(link=link, serie=serie)
        
        if not isinstance(link, str):
            pass
        
        if not link:
            ValueError('')
            
        response = requests.get(link)
        response.raise_for_status()
        payload = response.json()
        
        if not payload:
            raise InvalidJSONError('')

        return payload 
    
    def run_three_monthly(self, link, serie):
        self._link_is_valid(link=link, serie=serie)
        
        if not isinstance(link, str):
            ValueError('')
        
        if not link:
            ValueError('')
        
        data:list = []
        
        link_splitted:list = link.split('/')
        index_to_replace:int = link_splitted.index('first%201')
        
        link_splitted[index_to_replace] = 'all'
        link_joined = '/'.join(link_splitted)
        
        response = requests.get(link_joined)
        payload = response.json()
            
        if not payload:
            raise InvalidJSONError('')
   
        data.extend(payload)
            
        return data
    