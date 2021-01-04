from typing import Optional

from dapodik_webservice.converter import dataclass
from . import BaseModel


@dataclass
class PesertaDidik(BaseModel):
    registrasi_id: str
    jenis_pendaftaran_id: str
    jenis_pendaftaran_id_str: str
    nipd: str
    tanggal_masuk_sekolah: str
    sekolah_asal: Optional[str]
    peserta_didik_id: str
    nama: str
    nisn: Optional[str]
    jenis_kelamin: str
    nik: str
    tempat_lahir: str
    tanggal_lahir: str
    agama_id: int
    agama_id_str: str
    alamat_jalan: Optional[str]
    nomor_telepon_rumah: Optional[str]
    nomor_telepon_seluler: Optional[str]
    nama_ayah: str
    pekerjaan_ayah_id: int
    pekerjaan_ayah_id_str: str
    nama_ibu: str
    pekerjaan_ibu_id: int
    pekerjaan_ibu_id_str: str
    nama_wali: Optional[str]
    pekerjaan_wali_id: int
    pekerjaan_wali_id_str: str
    tinggi_badan: str
    berat_badan: str
    semester_id: str
    anggota_rombel_id: str
    rombongan_belajar_id: str
    tingkat_pendidikan_id: str
    nama_rombel: str
    kurikulum_id: int
    kurikulum_id_str: str

    def __str__(self) -> str:
        return self.nama
