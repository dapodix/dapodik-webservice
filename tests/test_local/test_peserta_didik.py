from dapodik_webservice import DapodikWebservice
from dapodik_webservice import PesertaDidik


class TestPesertaDidik:
    def test_get_peserta_didik(self, dapodik: DapodikWebservice):
        pe = dapodik.peserta_didik
        for p in pe:
            assert isinstance(p, PesertaDidik)
            assert isinstance(p.registrasi_id, str)
            assert isinstance(p.jenis_pendaftaran_id, str)
            assert isinstance(p.jenis_pendaftaran_id_str, str)
            assert isinstance(p.nipd, str)
            assert isinstance(p.tanggal_masuk_sekolah, str)
            assert isinstance(p.peserta_didik_id, str)
            assert isinstance(p.nama, str)
            assert isinstance(p.jenis_kelamin, str)
            assert isinstance(p.nik, str)
            assert isinstance(p.tempat_lahir, str)
            assert isinstance(p.tanggal_lahir, str)
            assert isinstance(p.agama_id, int)
            assert isinstance(p.agama_id_str, str)
            assert isinstance(p.nama_ayah, str)
            assert isinstance(p.pekerjaan_ayah_id, int)
            assert isinstance(p.pekerjaan_ayah_id_str, str)
            assert isinstance(p.nama_ibu, str)
            assert isinstance(p.pekerjaan_ibu_id, int)
            assert isinstance(p.pekerjaan_ibu_id_str, str)
            assert isinstance(p.pekerjaan_wali_id, int)
            assert isinstance(p.pekerjaan_wali_id_str, str)
            assert isinstance(p.tinggi_badan, str)
            assert isinstance(p.berat_badan, str)
            assert isinstance(p.semester_id, str)
            assert isinstance(p.anggota_rombel_id, str)
            assert isinstance(p.rombongan_belajar_id, str)
            assert isinstance(p.tingkat_pendidikan_id, str)
            assert isinstance(p.nama_rombel, str)
            assert isinstance(p.kurikulum_id, int)
            assert isinstance(p.kurikulum_id_str, str)

            assert not p.nisn or isinstance(p.nisn, str)
            assert not p.sekolah_asal or isinstance(p.sekolah_asal, str)
            assert not p.alamat_jalan or isinstance(p.alamat_jalan, str)
            assert not p.nomor_telepon_rumah or isinstance(p.nomor_telepon_rumah, str)
            assert not p.nomor_telepon_seluler or isinstance(
                p.nomor_telepon_seluler, str
            )
            assert not p.nama_wali or isinstance(p.nama_wali, str)
