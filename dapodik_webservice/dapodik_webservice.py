from requests import get as requests_get
from typing import Any, AnyStr, List, Union

from dapodik_webservice.models import (
    Pengguna,
    PesertaDidik,
    Ptk,
    RombonganBelajar,
    Sekolah,
)
from dapodik_webservice.result import Result
from dapodik_webservice.util import handle_response


class DapodikWebservice(object):
    """DapodikWebservice

    Args:
        token (Union[AnyStr, int]): Token Web Service Dapodik
        npsn (AnyStr): Nomor NPSN Sekolah
        url (str, optional): Url aplikasi dapodik (tanpa / di belakang). Defaults to "http://localhost:5774".
        user_agent (str, optional): User-Agent yang digunakan. Defaults to "pypi.org/project/dapodik_webservice/".
    """

    def __init__(
        self,
        token: Union[AnyStr, int],
        npsn: AnyStr,
        url: str = "http://localhost:5774",
        user_agent: str = "pypi.org/project/dapodik_webservice/",
    ):
        self.token = str(token)
        self.npsn = str(npsn)
        self.url = url
        self._ua = user_agent

    @property
    def pengguna(self) -> List[Pengguna]:
        """Mendapatkan daftar pengguna Dapodik

        Returns:
            List[Pengguna]: list Pengguna
        """
        res = self._get("getSekolah")
        return Pengguna.from_result(res)

    @property
    def peserta_didik(self) -> List[PesertaDidik]:
        """Mendapatkan daftar peserta didik Dapodik

        Returns:
            List[PesertaDidik]: list PesertaDidik
        """
        res = self._get("getPesertaDidik")
        return PesertaDidik.from_result(res)

    @property
    def ptk(self) -> List[Ptk]:
        """Mendapatkan daftar ptk / gtk Dapodik

        Returns:
            List[Ptk]: list Ptk
        """
        res = self._get("getGtk")
        return Ptk.from_result(res)

    @property
    def rombongan_belajar(self) -> List[RombonganBelajar]:
        """Mendapatkan daftar rombongan belajar Dapodik

        Returns:
            List[RombonganBelajar]: list RombonganBelajar
        """
        res = self._get("getRombonganBelajar")
        return RombonganBelajar.from_result(res)

    @property
    def sekolah(self) -> Sekolah:
        """Mendapatkan data sekolah Dapodik

        Returns:
            Sekolah: list RombonganBelajar
        """
        res = self._get("getSekolah")
        return Sekolah.from_result(res)

    def _get(self, func: str) -> Any:
        params = {"npsn": self.npsn}
        res = requests_get(
            self._url(func),
            params=params,
            headers=self._headers,
        )
        return handle_response(res).json()

    @property
    def _headers(self) -> dict:
        return {
            "Accept": "*/*",
            "Authorization": f"Bearer {self.token}",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "User-Agent": self._ua,
        }

    def _url(self, func: str) -> str:
        return f"{self.url}/WebService/{func}"
