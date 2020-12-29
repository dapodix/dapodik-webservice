from __future__ import annotations
from dacite import from_dict
from dataclasses import dataclass, field
from typing import List

from dapodik_webservice.typing import Rows
from . import AnggotaRombel
from . import Pembelajaran


@dataclass
class RombonganBelajar:
    rombongan_belajar_id: str
    nama: str
    tingkat_pendidikan_id: str
    semester_id: str
    jenis_rombel: str
    kurikulum_id: str
    kurikulum_id_str: str
    id_ruang: str
    id_ruang_str: str
    moving_class: str
    ptk_id: str
    ptk_id_str: str
    jenis_rombel_str: str
    anggota_rombel: List[AnggotaRombel] = field(default_factory=list)
    pembelajaran: List[Pembelajaran] = field(default_factory=list)

    @classmethod
    def from_result(cls, data: dict) -> List[RombonganBelajar]:
        rows: Rows = data["rows"]
        return [from_dict(RombonganBelajar, row) for row in rows]
