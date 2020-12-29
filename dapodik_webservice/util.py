from requests import Response
from dapodik_webservice.exception import (
    BaseDapoWsException,
    TokenSalahException,
    NPSNKosongException,
    SekolahTidakDitemukan,
)
from typing import List, Type

exceptions: List[Type[BaseDapoWsException]] = [
    TokenSalahException,
    NPSNKosongException,
    SekolahTidakDitemukan,
]


def handle_response(res: Response) -> Response:
    for exception in exceptions:
        if exception.text and exception.text in res.text:
            raise exception(exception.message)
    return res
