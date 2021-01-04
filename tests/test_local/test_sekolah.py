from dapodik_webservice import DapodikWebservice
from dapodik_webservice import Sekolah


class TestSekolah:
    def test_get_sekolah(self, dapodik: DapodikWebservice):
        s = dapodik.sekolah
        assert isinstance(s, Sekolah)
        assert isinstance(s.sekolah_id, str)
        assert isinstance(s.nama, str)
        assert isinstance(s.nss, str)
        assert isinstance(s.npsn, str)
        assert isinstance(s.bentuk_pendidikan_id, int)
        assert isinstance(s.bentuk_pendidikan_id_str, str)
        assert isinstance(s.status_sekolah, str)
        assert isinstance(s.status_sekolah_str, str)
        assert isinstance(s.alamat_jalan, str)
        assert isinstance(s.rt, str)
        assert isinstance(s.rw, str)
        assert isinstance(s.kode_wilayah, str)
        assert isinstance(s.kode_pos, str)
        assert isinstance(s.is_sks, bool)
        assert isinstance(s.lintang, str)
        assert isinstance(s.desa_kelurahan, str)
        assert isinstance(s.kecamatan, str)
        assert isinstance(s.kabupaten_kota, str)
        assert isinstance(s.provinsi, str)

        assert not s.nomor_telepon or isinstance(s.nomor_telepon, str)
        assert not s.nomor_fax or isinstance(s.nomor_fax, str)
        assert not s.email or isinstance(s.email, str)
        assert not s.website or isinstance(s.website, str)
        assert not s.bujur or isinstance(s.bujur, str)
        assert not s.dusun or isinstance(s.dusun, str)
