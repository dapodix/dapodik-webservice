from dapodik_webservice.converter import dataclass
from .. import BaseModel


@dataclass
class AnggotaRombel(BaseModel):
    anggota_rombel_id: str
    peserta_didik_id: str
    jenis_pendaftaran_id: str
    jenis_pendaftaran_id_str: str
