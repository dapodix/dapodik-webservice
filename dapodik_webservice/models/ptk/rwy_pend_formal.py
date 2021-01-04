from typing import Optional

from dapodik_webservice.converter import dataclass
from .. import BaseModel


@dataclass
class RwyPendFormal(BaseModel):
    riwayat_pendidikan_formal_id: str
    satuan_pendidikan_formal: str
    fakultas: str
    kependidikan: str
    tahun_masuk: str
    tahun_lulus: str
    nim: str
    status_kuliah: str
    semester: str
    ipk: str
    prodi: Optional[str]
    id_reg_pd: Optional[str]
    bidang_studi_id_str: str
    jenjang_pendidikan_id_str: str
    gelar_akademik_id_str: str
