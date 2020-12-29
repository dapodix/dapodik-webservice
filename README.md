# dapodik-webservice

[![dapodik-webservice - PyPi](https://img.shields.io/pypi/v/dapodik-webservice)](https://pypi.org/project/dapodik-webservice/)

SDK Python Web Service aplikasi Dapodik

## Install

Pastikan python 3.7 terinstall, kemudian jalankan perintah di bawah dalam Command Prompt atau Powershell (di Windows + X):

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
