from dapodik_webservice import DapodikWebservice
from dapodik_webservice import Ptk
from dapodik_webservice.models.ptk import RwyKepangkatan, RwyPendFormal


class TestPtk:
    def test_get_ptk(self, dapodik: DapodikWebservice):
        pe = dapodik.ptk
        for p in pe:
            assert isinstance(p, Ptk)
            assert isinstance(p.tahun_ajaran_id, str)
            assert isinstance(p.ptk_terdaftar_id, str)
            assert isinstance(p.ptk_id, str)
            assert isinstance(p.ptk_induk, str)
            assert isinstance(p.tanggal_surat_tugas, str)
            assert isinstance(p.nama, str)
            assert isinstance(p.jenis_kelamin, str)
            assert isinstance(p.tempat_lahir, str)
            assert isinstance(p.tanggal_lahir, str)
            assert isinstance(p.agama_id, int)
            assert isinstance(p.agama_id_str, str)
            assert isinstance(p.nik, str)
            assert isinstance(p.jenis_ptk_id, str)
            assert isinstance(p.jenis_ptk_id_str, str)
            assert isinstance(p.status_kepegawaian_id, int)
            assert isinstance(p.status_kepegawaian_id_str, str)
            assert isinstance(p.pendidikan_terakhir, str)
            assert isinstance(p.bidang_studi_terakhir, str)
            assert isinstance(p.pangkat_golongan_terakhir, str)
            assert not p.nuptk or isinstance(p.nuptk, str)
            assert not p.nip or isinstance(p.nip, str)
            for kepa in p.rwy_kepangkatan:
                self.asrt_rwy_kepangkatan(kepa)
            for pend in p.rwy_pend_formal:
                self.asrt_rwy_pend_formal(pend)

    def asrt_rwy_pend_formal(self, r: RwyPendFormal):
        assert isinstance(r.riwayat_pendidikan_formal_id, str)
        assert isinstance(r.satuan_pendidikan_formal, str)
        assert isinstance(r.fakultas, str)
        assert isinstance(r.kependidikan, str)
        assert isinstance(r.tahun_masuk, str)
        assert isinstance(r.tahun_lulus, str)
        assert isinstance(r.nim, str)
        assert isinstance(r.status_kuliah, str)
        assert isinstance(r.semester, str)
        assert isinstance(r.ipk, str)
        assert isinstance(r.bidang_studi_id_str, str)
        assert isinstance(r.jenjang_pendidikan_id_str, str)
        assert isinstance(r.gelar_akademik_id_str, str)
        assert not r.prodi or isinstance(r.prodi, str)
        assert not r.id_reg_pd or isinstance(r.id_reg_pd, str)

    def asrt_rwy_kepangkatan(self, r: RwyKepangkatan):
        # TODO : implement this
        assert bool(r)
