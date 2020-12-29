from __future__ import annotations
from dacite import from_dict
from dataclasses import dataclass
from typing import List, Optional

from dapodik_webservice.typing import Rows


@dataclass
class Pengguna:
    pengguna_id: str
    sekolah_id: str
    username: str
    nama: str
    peran_id_str: str
    password: str
    alamat: str
    no_telepon: str
    no_hp: str
    ptk_id: Optional[str]
    peserta_didik_id: Optional[str]

    @classmethod
    def from_result(cls, data: dict) -> List[Pengguna]:
        rows: Rows = data["rows"]
        return [from_dict(Pengguna, row) for row in rows]
