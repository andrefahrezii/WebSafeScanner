# Dokumentasi Menjalankan Aplikasi Python Secara Lokal

Panduan ini akan membantu Anda menjalankan aplikasi Python di lingkungan lokal Anda.

## Prasyarat

- **Python 3.x**: Pastikan Anda telah menginstal Python 3 di sistem Anda. Anda dapat memeriksa versi Python dengan perintah:

  ```bash
  python --version
  ```

````
## pip: Pastikan pip (package manager untuk Python) terinstal. Anda dapat memeriksa dengan perintah:

 ```bash
 pip --version
````

# Instalasi

Ikuti langkah-langkah berikut untuk menjalankan aplikasi secara lokal.

# 1. Clone Repository

Clone repositori aplikasi ke mesin lokal Anda. Gantilah URL dengan URL repositori Anda.

```bash
git clone https://github.com/username/repository.git
cd repository
```

# 2. Buat Virtual Environment (Opsional)

Disarankan untuk menggunakan virtual environment untuk mengelola dependensi.

```bash
python -m venv venv
```

# 3. Aktifkan Virtual Environment

Aktifkan virtual environment yang baru saja dibuat:

Di Windows:

```bash
venv\Scripts\activate
```

Di macOS/Linux:

```bash
source venv/bin/activate
```

# 4. Instal Dependensi

Instal dependensi yang diperlukan menggunakan requirements.txt:

```bash
pip install -r requirements.txt
```

# 5. Jalankan Aplikasi

Setelah semua dependensi terinstal, Anda dapat menjalankan aplikasi. Jika aplikasi Anda adalah skrip Python biasa, jalankan dengan:

```bash
python nama_file.py
```

Jika Anda menggunakan framework web seperti Flask atau Django, Anda dapat menjalankannya dengan:

# Flask:

```bash
export FLASK_APP=nama_file.py
flask run
```

# Django:

```bash
python manage.py runserver
```

# 6. Akses Aplikasi

Setelah aplikasi berjalan, Anda dapat mengaksesnya melalui browser dengan URL:

```bash
http://127.0.0.1:5000  # Untuk Flask
http://127.0.0.1:8000  # Untuk Django
```

## Catatan Tambahan

Pastikan untuk memeriksa file konfigurasi jika aplikasi memerlukan pengaturan khusus seperti variabel lingkungan.
Jika Anda mengalami masalah saat menjalankan aplikasi, periksa pesan kesalahan yang ditampilkan di terminal

```bash
Anda dapat mengganti `https://github.com/username/repository.git` dengan URL repositori Anda dan `nama_file.py` dengan nama file utama aplikasi Anda. Selamat mencoba!
```

## Example Response

```JSON
{
  "target": "http://192.168.1.230/payment/va",
  "scan_report": {
    "host": {
      "ip": "192.168.1.230",
      "status": "up",
      "latency": "0.0010s"
    },
    "ports": [
      {
        "port": 80,
        "state": "open",
        "service": "http",
        "version": "Apache httpd 2.4.41",
        "http_title": "Sample Title",
        "http_server_header": "Apache/2.4.41 (Ubuntu)"
      },
      {
        "port": 443,
        "state": "open",
        "service": "ssl/http",
        "version": "Nginx 1.18.0",
        "http_title": "Sample Title",
        "ssl_cert": {
          "subject": "commonName=example.com"
        },
        "ssl_date": "TLS randomness does not represent time",
        "vulnerabilities": [
          {
            "cve": "cve-2019-11043",
            "description": "Detail tentang kerentanan"
          }
        ],
        "http_server_header": "nginx/1.18.0"
      }
    ],
    "closed_ports": 995
  }
}
```
