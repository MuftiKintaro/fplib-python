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

stok_obat = (
    {"nama": "Sanmol Tablet", "jenis": "Analgesik", "stok": 42, "harga": 8500, "sisa_hari": 140},
    {"nama": "Amoxsan 500mg", "jenis": "Antibiotik", "stok": 7, "harga": 16000, "sisa_hari": 15},
    {"nama": "Enervon-C", "jenis": "Vitamin", "stok": 28, "harga": 24000, "sisa_hari": 95},
    {"nama": "Proris Forte", "jenis": "Analgesik", "stok": 5, "harga": 13500, "sisa_hari": 22},
    {"nama": "Cefat 500mg", "jenis": "Antibiotik", "stok": 14, "harga": 21000, "sisa_hari": 12},
    {"nama": "Input Salah", "jenis": "Vitamin", "stok": -2, "harga": 10000, "sisa_hari": 60},
)


def periksa_kritis(obat):
    return obat["sisa_hari"] <= 30 or obat["stok"] <= 10


def main():
    validasi_obat = buat_validator(
        (lambda o: o["stok"] >= 0, "Stok negatif"),
        (lambda o: o["harga"] > 0, "Harga tidak valid"),
    )

    valid, ditolak = partisi_data(lambda o: validasi_obat(o)[0], stok_obat)

    teks_aset = komposisi(
        lambda nominal: format_metrik(nominal, awalan="Rp "),
        lambda item: item["stok"] * item["harga"],
    )

    daftar_peringatan = alirkan(
        valid,
        lambda xs: pilih_jika(periksa_kritis, xs),
        lambda xs: peringkat_dengan(lambda o: o["sisa_hari"], xs, menurun=False),
        lambda xs: transformasi(
            lambda o: f"* {o['nama']} -> sisa {o['stok']} box (exp {o['sisa_hari']} hari) | aset {teks_aset(o)}",
            xs,
        ),
    )

    per_jenis = kelompokkan_dengan(lambda o: o["jenis"], valid)
    total_aset = reduksi_rekursif(lambda total, o: total + (o["stok"] * o["harga"]), valid, 0)

    print("LAPORAN STOK & KEDALUWARSA APOTEK")
    print("-" * 40)
    print(f"Data valid : {len(valid)} item (ditolak: {len(ditolak)})")
    print(f"Total aset : {format_metrik(total_aset, awalan='Rp ')}\n")

    print("Perlu restock / hampir expired:")
    for baris in daftar_peringatan:
        print(baris)

    print("\nRekap per kategori:")
    for jenis, isi in per_jenis.items():
        print(f"- {jenis}: {len(isi)} merek")


if __name__ == "__main__":
    main()