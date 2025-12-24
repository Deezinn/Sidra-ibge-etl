import requests
from src.domain.constants import APISABATE
from datetime import datetime
import json
import pandas as pd
class Extract():
    def __init__(self) -> None:
        pass
    
    def run(self):
        quarter = 1
        yearBase = 2024 # menor valor 1997
        year_now, month_now = datetime.now().year, (datetime.now().month - 1) // 3 + 1
        year_and_quarter_now = f'{year_now}0{month_now -1}'
        flag = True
        
        content_api = {}
        
        while flag:
            for serie,api in APISABATE.items():
                
                link_splited = api.split('/')
                link_splited[13] = f'{yearBase}0{quarter}'
                link_joined = '/'.join(link_splited)
                
                r = requests.get(link_joined, timeout=30)
                
                if r.status_code == 200 and link_splited[13] != year_and_quarter_now :
                    if quarter > 3:
                        quarter = 0
                        yearBase += 1
                    quarter += 1
                else:
                    flag = False
                
                content_api[f'abate_{serie}'] = r.json()

        return content_api
    
e = Extract()   
e.run()