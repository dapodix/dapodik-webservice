from dapodik_webservice import DapodikWebservice
from dapodik_webservice import RombonganBelajar
from dapodik_webservice.models.rombongan_belajar import AnggotaRombel, Pembelajaran


class TestRombonganBelajar:
    def test_get_rombongan_belajar(self, dapodik: DapodikWebservice):
        rb = dapodik.rombongan_belajar
        for r in rb:
            assert isinstance(r, RombonganBelajar)
            assert isinstance(r.rombongan_belajar_id, str)
            assert isinstance(r.nama, str)
            assert isinstance(r.tingkat_pendidikan_id, str)
            assert isinstance(r.semester_id, str)
            assert isinstance(r.jenis_rombel, str)
            assert isinstance(r.kurikulum_id, int)
            assert isinstance(r.kurikulum_id_str, str)
            assert isinstance(r.id_ruang, str)
            assert isinstance(r.id_ruang_str, str)
            assert isinstance(r.moving_class, str)
            assert isinstance(r.ptk_id, str)
            assert isinstance(r.ptk_id_str, str)
            assert isinstance(r.jenis_rombel_str, str)
            for a in r.anggota_rombel:
                self.asrt_anggota_rombel(a)
            for p in r.pembelajaran:
                self.asrt_pembelajaran(p)

    def asrt_anggota_rombel(self, a: AnggotaRombel):
        assert isinstance(a.anggota_rombel_id, str)
        assert isinstance(a.peserta_didik_id, str)
        assert isinstance(a.jenis_pendaftaran_id, str)
        assert isinstance(a.jenis_pendaftaran_id_str, str)

    def asrt_pembelajaran(self, p: Pembelajaran):
        assert isinstance(p.pembelajaran_id, str)
        assert isinstance(p.mata_pelajaran_id, int)
        assert isinstance(p.mata_pelajaran_id_str, str)
        assert isinstance(p.ptk_terdaftar_id, str)
        assert isinstance(p.ptk_id, str)
        assert isinstance(p.nama_mata_pelajaran, str)
        assert not p.induk_pembelajaran_id or isinstance(p.induk_pembelajaran_id, int)
        assert isinstance(p.jam_mengajar_per_minggu, str)
        assert isinstance(p.status_di_kurikulum, str)
        assert isinstance(p.status_di_kurikulum_str, str)
