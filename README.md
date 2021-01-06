# dapodik-webservice

[![PyPi Package Version](https://img.shields.io/pypi/v/dapodik-webservice)](https://pypi.org/project/dapodik-webservice/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/dapodik-webservice)](https://pypi.org/project/dapodik-webservice/)
[![Tests](https://github.com/dapodix/dapodik-webservice/workflows/Tests/badge.svg)](https://github.com/dapodix/dapodik-webservice/actions)
[![codecov](https://codecov.io/gh/dapodix/dapodik-webservice/branch/main/graph/badge.svg?token=2rX7lP6K0C)](https://codecov.io/gh/dapodix/dapodik-webservice)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Mypy](https://img.shields.io/badge/Mypy-enabled-brightgreen)](https://github.com/python/mypy)

SDK Python Web Service aplikasi Dapodik
_Jangan lupa untuk [donasi](#donasi)_

## Penggunaan

### Aplikasi CLI

Download `dapodik-export` dari [halaman rilis](https://github.com/dapodix/dapodik-webservice/releases) sebaiknya dowload file `.zip` karena lebih cepat.
Exstrak filenya dan masuk folder dapodik-export _(jika menggunakan zip)_.
Buka folder yang berisi `dapodik-export.exe`
Buka / open `cmd / windows powershell` di folder tersebut dengan tahan shift + klik kanan di dalam folder _(jangan klik kanan file apapun)_.

#### Contoh penggunaan Aplikasi CLI

Berikut contoh perintah yang bisa dijalankan melalui `cmd / windows powershell`

_Rubah `token saya` menjadi token webservice dari aplikasi DAPODIK bagian pengaturan!_

Mengeksport semua data ke dalam file bernama `Sekolahku`

```cmd
dapodik-export.exe export semua --token "token saya" --npsn "0123456789" "Sekolahku"
```

Mengeksport data peserta didik ke dalam file bernama `Peserta didik`

```cmd
dapodik-export.exe export peserta-didik --token "token saya" --npsn "0123456789" "Peserta didik"
```

### Dengan Python

Untuk menggunakan modul ini silahkan buat token Web Service Dapodik terlebih dahulu di pengaturan Dapodik.

```python
from dapodik_webservice import DapodikWebservice

token = 'token webservice'
npsn = '12345678'

dw = DapodikWebservice(token, npsn)

sekolah = dw.sekolah

print(sekolah.nama)

```

## Install Dari PIP

_Khusus untuk pengembang python_! Pastikan python 3.6 terinstall, kemudian jalankan perintah di bawah dalam Command Prompt atau Powershell (di Windows + X / klik kanan icon Windows):

```bash
pip install --upgrade dapodik-webservice
```

## Donasi

Jika anda ingin melakukan donasi untuk kami, bisa menghubungi kami melalui [WhatsApp](https://wa.me/6287725780404) ataupun [Telegram](https://t.me/hexatester).

## Legal / Hukum

Kode ini sama sekali tidak berafiliasi dengan, diizinkan, dipelihara, disponsori atau didukung oleh Kemdikbud atau afiliasi atau anak organisasinya. Ini adalah perangkat lunak yang independen dan tidak resmi. Gunakan dengan risiko Anda sendiri.
