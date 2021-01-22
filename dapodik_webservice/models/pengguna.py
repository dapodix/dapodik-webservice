from typing import Optional

from dapodik_webservice.converter import dataclass
from . import BaseModel


@dataclass
class Pengguna(BaseModel):
    pengguna_id: str
    sekolah_id: str
    username: str
    nama: str
    peran_id_str: str
    password: str
    alamat: Optional[str]
    no_telepon: Optional[str]
    no_hp: Optional[str]
    ptk_id: Optional[str]
    peserta_didik_id: Optional[str]
