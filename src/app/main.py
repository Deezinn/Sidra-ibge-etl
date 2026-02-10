from infra.http import AsyncExtractor
from infra.services.extract import LinkGenerator
from infra.services.extract import LinkValidator

from pipeline.extract import Extract

from domain.constants.links import APIS

from pipeline import Orquestrator

if __name__ == "__main__":
    extract = Extract(
        apis=APIS,
        async_extractor=AsyncExtractor(),
        link_generator=LinkGenerator(),
        link_validator=LinkValidator(),
    )
    orq = Orquestrator(extract=extract)
    orq.teste()
