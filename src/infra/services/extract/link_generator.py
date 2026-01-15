from datetime import datetime


class LinkGenerator():
    PLACEHOLDER = 'first%201'

    @staticmethod
    def _validate_inputs(link: str, serie: str) -> None:
        """_summary_

        Args:
            link (str): _description_
            serie (str): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
            TypeError: _description_
            TypeError: _description_
        """

        if not link:
            raise ValueError('')
        
        if not serie :
            raise ValueError('')
        
        if not isinstance(link, str):
            raise TypeError('')

        if not isinstance(serie, str):
            raise TypeError('')


    @staticmethod
    def _link_is_valid(link: str, serie: str) -> None:
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

    def quarterly(self, link: str, serie: str) -> list:
        self._validate_inputs(link=link, serie=serie)
        self._link_is_valid(link=link, serie=serie)

        data:list = []

        year_init:int = 2025
        quarter_init:int = 1

        now:datetime = datetime.now()

        current_quarter:int = (now.month - 1)// 3 + 1
        current_year:int = now.year

        link_splitted:list = link.split('/')

        if self.PLACEHOLDER not in link_splitted:
            raise ValueError(f'link não contém o placeholder "first%201" {serie}')

        index_to_replace:int = link_splitted.index(self.PLACEHOLDER)

        while (year_init,quarter_init) <= (current_year,current_quarter):

            if quarter_init > 4:
                quarter_init = 1
                year_init += 1
               
            link_splitted[index_to_replace] = f'{year_init}{quarter_init:02d}'
            link_joined:str = '/'.join(link_splitted)
            data.append(link_joined)
            quarter_init += 1
        return data

    def monthly(self, link: str, serie: str) -> list:
        self._validate_inputs(link=link, serie=serie)
        self._link_is_valid(link=link, serie=serie)

        data:list = []

        year_init:int = 2025
        month_init:int = 10

        now:datetime = datetime.now()
        current_year:int = now.year
        current_month:int = now.month

        link_splitted:list = link.split('/')

        if self.PLACEHOLDER not in link_splitted:
            raise ValueError(f'link não contém o placeholder "first%201" {serie}')

        index_to_replace:int = link_splitted.index(self.PLACEHOLDER)

        while (year_init, month_init) <= (current_year, current_month):

            if month_init > 12:
                month_init = 1
                year_init += 1

            link_splitted[index_to_replace] = f'{year_init}{month_init:02d}'
            link_joined = '/'.join(link_splitted)
            data.append(link_joined)
                
            month_init += 1
        return data

    def semester(self, link: str, serie: str) -> list:
        self._validate_inputs(link=link, serie=serie)
        self._link_is_valid(link=link, serie=serie)

        data:list = []

        year_init:int = 2025
        semester_init:int = 1

        now:datetime = datetime.now()
        current_semester:int = (now.month - 1) // 6 + 1
        current_year:int = now.year

        link_splitted = link.split('/')

        if self.PLACEHOLDER not in link_splitted:
            raise ValueError(f'link não contém o placeholder "first%201" {serie}')

        index_to_replace = link_splitted.index(self.PLACEHOLDER)

        while (year_init, semester_init) <= (current_year, current_semester):

            if semester_init > 2:
                semester_init = 1
                year_init += 1

            link_splitted[index_to_replace] = f'{year_init}{semester_init:02d}'
            link_joined = '/'.join(link_splitted)
            data.append(link_joined)
            semester_init += 1

        return data

    def one_monthly(self, link, serie: str) -> list:
        self._validate_inputs(link=link, serie=serie)
        self._link_is_valid(link=link, serie=serie)

        data:list = []
        data.append(link)
        return data

    def three_monthly(self, link, serie) -> list:
        self._validate_inputs(link=link, serie=serie)
        self._link_is_valid(link=link, serie=serie)

        data:list = []

        link_splitted:list = link.split('/')
        index_to_replace:int = link_splitted.index(self.PLACEHOLDER)

        link_splitted[index_to_replace] = 'all'
        link_joined = '/'.join(link_splitted)
        data.append(link_joined)
        return data
