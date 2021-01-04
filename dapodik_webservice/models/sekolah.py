from typing import Optional

from dapodik_webservice.converter import dataclass
from . import BaseModel


@dataclass
class Sekolah(BaseModel):
    sekolah_id: str
    nama: str
    nss: str
    npsn: str
    bentuk_pendidikan_id: int
    bentuk_pendidikan_id_str: str
    status_sekolah: str
    status_sekolah_str: str
    alamat_jalan: str
    rt: str
    rw: str
    kode_wilayah: str
    kode_pos: str
    nomor_telepon: Optional[str]
    nomor_fax: Optional[str]
    email: Optional[str]
    website: Optional[str]
    is_sks: bool
    lintang: str
    bujur: Optional[str]
    dusun: Optional[str]
    desa_kelurahan: str
    kecamatan: str
    kabupaten_kota: str
    provinsi: str
