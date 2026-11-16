from functools import reduce


def alirkan(data, *fungsi):
    """Mengalirkan data melewati beberapa fungsi secara berurutan."""
    return reduce(lambda acc, f: f(acc), fungsi, data)


def komposisi(*fungsi):
    """Menggabungkan beberapa fungsi menjadi satu fungsi baru (kanan ke kiri)."""
    return lambda x: reduce(lambda acc, f: f(acc), reversed(fungsi), x)


def pilih_jika(syarat, data):
    """Menyaring isi data berdasarkan fungsi syarat tanpa mengubah data asli."""
    return tuple(item for item in data if syarat(item))


def transformasi(fn, data):
    """Memetakan fungsi fn ke setiap elemen data."""
    return tuple(fn(item) for item in data)


def reduksi_rekursif(fn, data, awal):
    """Menggabungkan elemen data menjadi satu nilai dengan rekursi."""
    items = tuple(data)
    if not items:
        return awal
    return reduksi_rekursif(fn, items[1:], fn(awal, items[0]))


def partisi_data(syarat, data):
    """Memisahkan data menjadi dua tuple: (lolos_syarat, tidak_lolos)."""
    items = tuple(data)
    cocok = tuple(x for x in items if syarat(x))
    tidak_cocok = tuple(x for x in items if not syarat(x))
    return cocok, tidak_cocok


def kelompokkan_dengan(ambil_kunci, data):
    """Mengelompokkan data ke dictionary berdasarkan kunci tertentu."""
    def masukkan(hasil, item):
        k = ambil_kunci(item)
        grup_lama = hasil.get(k, ())
        return {**hasil, k: grup_lama + (item,)}

    return reduce(masukkan, data, {})


def peringkat_dengan(ambil_kunci, data, menurun=True):
    """Mengurutkan data dan mengembalikan tuple baru."""
    return tuple(sorted(data, key=ambil_kunci, reverse=menurun))


def buat_validator(*aturan):
    """Membuat fungsi validator dari kumpulan pasangan (syarat, pesan_error)."""
    def cek(item):
        error = tuple(pesan for syarat, pesan in aturan if not syarat(item))
        return len(error) == 0, error

    return cek


def format_metrik(angka, awalan="", akhiran="", desimal=0):
    """Memformat angka ke string dengan pemisah ribuan titik."""
    nilai = round(angka, desimal)
    if desimal == 0:
        teks = f"{int(nilai):,}".replace(",", ".")
    else:
        utama, koma = f"{nilai:,.{desimal}f}".split(".")
        teks = f"{utama.replace(',', '.')},{koma}"
    return f"{awalan}{teks}{akhiran}"