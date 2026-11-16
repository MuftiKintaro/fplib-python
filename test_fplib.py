from fplib import (
    alirkan,
    komposisi,
    pilih_jika,
    transformasi,
    reduksi_rekursif,
    partisi_data,
    kelompokkan_dengan,
    peringkat_dengan,
    buat_validator,
    format_metrik,
)


def test_alirkan():
    hasil = alirkan(
        [1, 2, 3, 4, 5],
        lambda xs: pilih_jika(lambda x: x % 2 == 1, xs),
        lambda xs: transformasi(lambda x: x * 10, xs),
        lambda xs: reduksi_rekursif(lambda acc, x: acc + x, xs, 0),
    )
    assert hasil == 90


def test_komposisi():
    f = komposisi(lambda x: x + 2, lambda x: x * 3)
    assert f(4) == 14


def test_pilih_jika_immutable():
    asal = [10, 25, 30, 45, 50]
    hasil = pilih_jika(lambda x: x >= 30, asal)
    assert hasil == (30, 45, 50)
    assert asal == [10, 25, 30, 45, 50]


def test_transformasi():
    barang = [{"nama": "Buku", "harga": 5000}, {"nama": "Pena", "harga": 2000}]
    assert transformasi(lambda b: b["harga"] * 2, barang) == (10000, 4000)


def test_reduksi_rekursif():
    assert reduksi_rekursif(lambda a, b: a + b, [10, 20, 30], 0) == 60
    assert reduksi_rekursif(lambda a, b: a + b, [], 50) == 50


def test_partisi_data():
    genap, ganjil = partisi_data(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
    assert genap == (2, 4, 6)
    assert ganjil == (1, 3, 5)


def test_kelompokkan_dengan():
    data = (
        {"jenis": "Minuman", "nama": "Kopi"},
        {"jenis": "Makanan", "nama": "Roti"},
        {"jenis": "Minuman", "nama": "Teh"},
    )
    grup = kelompokkan_dengan(lambda x: x["jenis"], data)
    assert len(grup["Minuman"]) == 2
    assert len(grup["Makanan"]) == 1


def test_peringkat_dengan():
    nilai = [{"nama": "Rina", "skor": 78}, {"nama": "Dimas", "skor": 91}, {"nama": "Sari", "skor": 85}]
    urut = peringkat_dengan(lambda x: x["skor"], nilai)
    assert urut[0]["nama"] == "Dimas"
    assert nilai[0]["nama"] == "Rina"


def test_buat_validator():
    cek = buat_validator(
        (lambda x: x["nama"] != "", "Nama wajib diisi"),
        (lambda x: x["stok"] >= 0, "Stok minus"),
    )
    assert cek({"nama": "Bodrex", "stok": 12}) == (True, ())
    assert cek({"nama": "", "stok": -1}) == (False, ("Nama wajib diisi", "Stok minus"))


def test_format_metrik():
    assert format_metrik(150000, awalan="Rp ") == "Rp 150.000"
    assert format_metrik(12.34, akhiran=" kg", desimal=1) == "12,3 kg"