# Library Pemrograman Fungsional (`fplib.py`)

Proyek Tugas Kelompok — Mata Kuliah Pemrograman Fungsional  
Program Studi Informatika, Universitas Muhammadiyah Malang

**Anggota Kelompok X:**
1. Nama Anggota 1 (NIM)
2. Nama Anggota 2 (NIM)
3. Nama Anggota 3 (NIM)

---

## Deskripsi Proyek

Repositori ini berisi library Python buatan sendiri (`fplib.py`) yang ditulis menggunakan paradigma pemrograman fungsional (*pure functions*, *immutability*, *higher-order functions*, *function composition*, dan rekursi) serta penerapannya pada lima aplikasi terpisah.

### Struktur File
- `fplib.py` — Modul utama berisi 10 fungsi murni bergaya fungsional.
- `test_fplib.py` — Pengujian unit otomatis menggunakan `pytest`.
- `app_apotek.py` — Aplikasi 1: Laporan Stok & Kedaluwarsa Apotek.
- `app_fitness.py` — Aplikasi 2: Catatan Workout & Kalori Mingguan.
- `app_bengkel.py` — Aplikasi 3: Rekap Antrean & Estimasi Servis Bengkel.
- `app_turnamen.py` — Aplikasi 4: Klasemen & Statistik Turnamen Futsal.
- `app_logistik.py` — Aplikasi 5: Rekap Pengiriman & Ongkos Kirim Logistik.
- `requirements.txt` — Daftar dependensi paket yang digunakan.

---

## Daftar Fungsi (`fplib.py`)

1. **`alirkan(data, *fungsi)`**  
   Mengalirkan data melewati serangkaian fungsi transformasi secara berurutan dari kiri ke kanan (*pipelining*).
2. **`komposisi(*fungsi)`**  
   Menggabungkan beberapa fungsi menjadi satu fungsi baru yang dieksekusi dari kanan ke kiri ($f(g(x))$).
3. **`pilih_jika(syarat, data)`**  
   Menyaring elemen koleksi berdasarkan fungsi predikat `syarat` dan mengembalikan `tuple` baru tanpa mengubah data asli.
4. **`transformasi(fn, data)`**  
   Memetakan fungsi `fn` ke setiap elemen koleksi dan mengembalikan `tuple` baru berisi hasil transformasi.
5. **`reduksi_rekursif(fn, data, awal)`**  
   Menggabungkan seluruh elemen koleksi menjadi satu nilai tunggal menggunakan rekursi murni.
6. **`partisi_data(syarat, data)`**  
   Memisahkan koleksi menjadi dua `tuple` sekaligus: `(lolos_syarat, tidak_lolos)`.
7. **`kelompokkan_dengan(ambil_kunci, data)`**  
   Mengelompokkan elemen koleksi ke dalam `dictionary` berdasarkan kunci tertentu dengan anggota berupa `tuple`.
8. **`peringkat_dengan(ambil_kunci, data, menurun=True)`**  
   Mengurutkan elemen koleksi berdasarkan kunci tertentu dan mengembalikan `tuple` baru tanpa mengubah urutan data aslinya.
9. **`buat_validator(*aturan)`**  
   *Higher-Order Function* yang menerima pasangan `(syarat, pesan_error)` dan mengembalikan fungsi validator baru.
10. **`format_metrik(angka, awalan="", akhiran="", desimal=0)`**  
    Memformat nilai angka menjadi string dengan pemisah ribuan titik serta awalan atau akhiran satuan.

---

## Cara Instalasi & Menjalankan Program

### 1. Persiapan Lingkungan (`venv`)
```bash
python -m venv .venv

# Aktivasi di Windows:
.venv\Scripts\activate

# Aktivasi di Linux/macOS:
source .venv/bin/activate

# Pasang dependensi:
pip install -r requirements.txt
```

### 2. Menjalankan Pengujian Otomatis (`pytest`)
```bash
pytest -v
```

### 3. Menjalankan Kelima Aplikasi
```bash
python app_apotek.py
python app_fitness.py
python app_bengkel.py
python app_turnamen.py
python app_logistik.py
```

### 4. Contoh Pemakaian Library
```python
from fplib import alirkan, pilih_jika, transformasi, format_metrik

harga_barang = (10000, 25000, 50000)
hasil = alirkan(
    harga_barang,
    lambda xs: pilih_jika(lambda x: x >= 20000, xs),
    lambda xs: transformasi(lambda x: format_metrik(x, awalan="Rp "), xs),
)
print(hasil)  # ('Rp 25.000', 'Rp 50.000')
```
