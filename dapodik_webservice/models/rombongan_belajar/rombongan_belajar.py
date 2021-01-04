import attr
from typing import List

from dapodik_webservice.converter import dataclass
from .. import BaseModel
from . import AnggotaRombel
from . import Pembelajaran


@dataclass
class RombonganBelajar(BaseModel):
    rombongan_belajar_id: str
    nama: str
    tingkat_pendidikan_id: str
    semester_id: str
    jenis_rombel: str
    kurikulum_id: int
    kurikulum_id_str: str
    id_ruang: str
    id_ruang_str: str
    moving_class: str
    ptk_id: str
    ptk_id_str: str
    jenis_rombel_str: str
    anggota_rombel: List[AnggotaRombel] = attr.ib(
        factory=list, converter=AnggotaRombel.from_list
    )
    pembelajaran: List[Pembelajaran] = attr.ib(
        factory=list, converter=Pembelajaran.from_list
    )
