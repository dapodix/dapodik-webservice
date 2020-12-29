from requests import Response
from dapodik_webservice.exception import (
    TokenSalahException,
    NPSNKosongException,
    SekolahTidakDitemukan,
)
from typing import Optional

exceptions = [TokenSalahException, NPSNKosongException, SekolahTidakDitemukan]


def e_get_text(exception) -> Optional[str]:
    annot = getattr(exception, "__annotations__", {})
    return annot.get('text')



def handle_response(res: Response) -> Response:
    for exception in exceptions:
        text = e_get_text(exception)
        if text and text in res.text:
            raise exception()
    return res
