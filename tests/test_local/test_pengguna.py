from dapodik_webservice import DapodikWebservice
from dapodik_webservice import Pengguna


class TestPengguna:
    def test_get_pengguna(self, dapodik: DapodikWebservice):
        pe = dapodik.pengguna
        for p in pe:
            assert isinstance(p, Pengguna)
            assert isinstance(p.pengguna_id, str)
            assert isinstance(p.sekolah_id, str)
            assert isinstance(p.username, str)
            assert isinstance(p.nama, str)
            assert isinstance(p.peran_id_str, str)
            assert isinstance(p.password, str)
            assert isinstance(p.alamat, str)
            assert not p.no_telepon or isinstance(p.no_telepon, str)
            assert not p.no_hp or isinstance(p.no_hp, str)
            assert not p.ptk_id or isinstance(p.ptk_id, str)
            assert not p.peserta_didik_id or isinstance(p.peserta_didik_id, str)
