from __future__ import annotations
from dacite import from_dict
from dataclasses import dataclass, field
from typing import List, Optional

from dapodik_webservice.typing import Rows
from . import RwyKepangkatan
from . import RwyPendFormal


@dataclass
class Ptk:
    tahun_ajaran_id: str
    ptk_terdaftar_id: str
    ptk_id: str
    ptk_induk: str
    tanggal_surat_tugas: str
    nama: str
    jenis_kelamin: str
    tempat_lahir: str
    tanggal_lahir: str
    agama_id: str
    agama_id_str: str
    nuptk: str
    nik: str
    jenis_ptk_id: str
    jenis_ptk_id_str: str
    status_kepegawaian_id: str
    status_kepegawaian_id_str: str
    nip: Optional[str]
    pendidikan_terakhir: str
    bidang_studi_terakhir: str
    pangkat_golongan_terakhir: str
    rwy_pend_formal: List[RwyPendFormal] = field(default_factory=list)
    rwy_kepangkatan: List[RwyKepangkatan] = field(default_factory=list)

    @classmethod
    def from_result(cls, data: dict) -> List[Ptk]:
        rows: Rows = data["rows"]
        return [from_dict(Ptk, row) for row in rows]
