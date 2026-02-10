class LinkValidator:
    def _validate_inputs(self, link: str, serie: str) -> None:
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

    def _link_is_valid(self, link: str, serie: str) -> None:
        """_summary_

        Args:
            link (str): _description_
            serie (str): _description_

        Raises:
            ValueError: _description_
        """
        
        link_splitted:list = link.split('/')
        serie_splitted:list = serie.split('_')

        for value in serie_splitted:
            if value.isdigit():
                if value in link_splitted:
                    continue
                else:
                    raise ValueError(f'{value} invalido da {serie} serie')
