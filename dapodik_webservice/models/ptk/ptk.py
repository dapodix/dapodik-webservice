import attr
from typing import List, Optional

from dapodik_webservice.converter import dataclass
from .. import BaseModel
from . import RwyKepangkatan
from . import RwyPendFormal


@dataclass
class Ptk(BaseModel):
    tahun_ajaran_id: str
    ptk_terdaftar_id: str
    ptk_id: str
    ptk_induk: str
    tanggal_surat_tugas: str
    nama: str
    jenis_kelamin: str
    tempat_lahir: str
    tanggal_lahir: str
    agama_id: Optional[int]
    agama_id_str: str
    nuptk: Optional[str]
    nik: str
    jenis_ptk_id: str
    jenis_ptk_id_str: str
    status_kepegawaian_id: int
    status_kepegawaian_id_str: str
    nip: Optional[str]
    pendidikan_terakhir: str
    bidang_studi_terakhir: str
    pangkat_golongan_terakhir: str
    rwy_pend_formal: List[RwyPendFormal] = attr.ib(
        converter=RwyPendFormal.from_list, factory=list
    )
    rwy_kepangkatan: List[RwyKepangkatan] = attr.ib(
        converter=RwyKepangkatan.from_list, factory=list
    )
