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
            if p.alamat:
                assert isinstance(p.alamat, str)
            if p.no_telepon:
                assert isinstance(p.no_telepon, str)
            if p.no_hp:
                assert isinstance(p.no_hp, str)
            if p.ptk_id:
                assert isinstance(p.ptk_id, str)
            if p.peserta_didik_id:
                assert isinstance(p.peserta_didik_id, str)
