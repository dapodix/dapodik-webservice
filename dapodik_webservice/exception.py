class BaseDapoWsException(BaseException):
    pass


class TokenSalahException(BaseDapoWsException):
    message = "Token Salah!"
    text = "Access denied - You are not authorized to access this page. #1"


class NPSNKosongException(BaseDapoWsException):
    message = "NPSN Kosong"
    text = "Parameter NPSN harap diisi"


class SekolahTidakDitemukan(BaseDapoWsException):
    message = "Sekolah tidak ditemukan"
    text = "Sekolah tidak ditemukan"
