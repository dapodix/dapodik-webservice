# dapodik-webservice

[![dapodik-webservice - PyPi](https://img.shields.io/pypi/v/dapodik-webservice)](https://pypi.org/project/dapodik-webservice/)
[![Tests](https://github.com/dapodix/dapodik-webservice/workflows/Tests/badge.svg)](https://github.com/dapodix/dapodik-webservice/actions)
[![codecov](https://codecov.io/gh/dapodix/dapodik-webservice/branch/main/graph/badge.svg?token=2rX7lP6K0C)](https://codecov.io/gh/dapodix/dapodik-webservice)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

SDK Python Web Service aplikasi Dapodik

## Install

Pastikan python 3.7 terinstall, kemudian jalankan perintah di bawah dalam Command Prompt atau Powershell (di Windows + X / klik kanan icon Windows):

```bash
pip install --upgrade dapodik-webservice
```

## Penggunaan

Untuk menggunakan modul ini silahkan buat token Web Service Dapodik terlebih dahulu di pengaturan Dapodik.

```python
from dapodik_webservice import DapodikWebservice

token = 'token webservice'
npsn = '12345678'

dw = DapodikWebservice(token, npsn)

sekolah = dw.sekolah

print(sekolah.nama)

```

## Donasi

Jika anda ingin melakukan donasi untuk kami, bisa menghubungi kami melalui [WhatsApp](https://wa.me/6287725780404) ataupun [Telegram](https://t.me/hexatester).

## Legal / Hukum

Kode ini sama sekali tidak berafiliasi dengan, diizinkan, dipelihara, disponsori atau didukung oleh Kemdikbud atau afiliasi atau anak organisasinya. Ini adalah perangkat lunak yang independen dan tidak resmi. Gunakan dengan risiko Anda sendiri.
