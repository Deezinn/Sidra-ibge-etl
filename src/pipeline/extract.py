import requests
from src.domain.constants import APISABATE
from datetime import datetime
class Extract():
    def __init__(self) -> None:
        pass
    
    def run(self):
        quarter = 1
        yearBase = 2025
        year_now, month_now = datetime.now().year, (datetime.now().month - 1) // 3 + 1
        year_and_quarter_now = f'{year_now}0{month_now}'
        flag = True
        
        while flag:
            for api in APISABATE:
                link_splited = api.split('/')
                link_splited[11] = f'{yearBase}0{quarter}'
                link_joined = '/'.join(link_splited)
                r = requests.get(link_joined, timeout=30)
                if str(link_splited[11]) != year_and_quarter_now:
                    if quarter > 4:
                        quarter = 0
                        yearBase += 1
                    quarter += 1
                else:
                    flag = False
e = Extract()   
e.run()