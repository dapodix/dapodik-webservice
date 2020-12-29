from dataclasses import dataclass


@dataclass
class AnggotaRombel:
    anggota_rombel_id: str
    peserta_didik_id: str
    jenis_pendaftaran_id: str
    jenis_pendaftaran_id_str: str
