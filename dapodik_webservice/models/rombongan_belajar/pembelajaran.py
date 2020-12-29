from dataclasses import dataclass
from typing import Optional


@dataclass
class Pembelajaran:
    pembelajaran_id: str
    mata_pelajaran_id: int
    mata_pelajaran_id_str: str
    ptk_terdaftar_id: str
    ptk_id: str
    nama_mata_pelajaran: str
    induk_pembelajaran_id: Optional[int]
    jam_mengajar_per_minggu: str
    status_di_kurikulum: str
    status_di_kurikulum_str: str

    def __str__(self) -> str:
        return self.nama_mata_pelajaran
