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

daftar_paket = (
    {"resi": "JTM-01", "tujuan": "Surabaya", "berat": 2.5, "tarif": 12000, "lama": 1, "target": 2},
    {"resi": "JTM-02", "tujuan": "Jakarta", "berat": 6.2, "tarif": 18000, "lama": 4, "target": 3},
    {"resi": "JTM-03", "tujuan": "Surabaya", "berat": 1.4, "tarif": 12000, "lama": 2, "target": 2},
    {"resi": "JTM-04", "tujuan": "Bandung", "berat": 8.0, "tarif": 16000, "lama": 3, "target": 3},
    {"resi": "JTM-05", "tujuan": "Jakarta", "berat": 3.5, "tarif": 18000, "lama": 5, "target": 3},
    {"resi": "JTM-06", "tujuan": "Malang", "berat": 0.0, "tarif": 10000, "lama": 1, "target": 1},
)


def main():
    cek_paket = buat_validator(
        (lambda p: p["berat"] > 0, "Berat nol/negatif"),
        (lambda p: p["tarif"] > 0, "Tarif tidak valid"),
    )

    hitung_ongkir = komposisi(
        lambda nominal: round(nominal, -2),
        lambda p: p["berat"] * p["tarif"],
    )

    paket_sah = alirkan(
        daftar_paket,
        lambda xs: pilih_jika(lambda p: cek_paket(p)[0], xs),
        lambda xs: transformasi(lambda p: {**p, "ongkir": hitung_ongkir(p)}, xs),
        lambda xs: peringkat_dengan(lambda p: p["ongkir"], xs),
    )

    tepat_waktu, telat = partisi_data(lambda p: p["lama"] <= p["target"], paket_sah)
    paket_besar = pilih_jika(lambda p: p["berat"] >= 5.0, paket_sah)
    per_kota = kelompokkan_dengan(lambda p: p["tujuan"], paket_sah)

    total_kg = reduksi_rekursif(lambda acc, p: acc + p["berat"], paket_sah, 0.0)
    total_biaya = reduksi_rekursif(lambda acc, p: acc + p["ongkir"], paket_sah, 0)

    print("REKAP PENGIRIMAN LOGISTIK")
    print(f"Total muatan : {format_metrik(total_kg, akhiran=' kg', desimal=1)}")
    print(f"Total ongkir : {format_metrik(total_biaya, awalan='Rp ')}")
    print(f"Ketepatan    : {len(tepat_waktu)} tepat waktu, {len(telat)} terlambat")
    print(f"Kargo >= 5kg : {len(paket_besar)} paket\n")

    for p in paket_sah:
        berat_str = format_metrik(p["berat"], akhiran=" kg", desimal=1)
        ongkir_str = format_metrik(p["ongkir"], awalan="Rp ")
        print(f"- {p['resi']} ke {p['tujuan']} ({berat_str}) -> {ongkir_str}")

    print("\nSebaran kota tujuan:")
    for kota, list_pkt in per_kota.items():
        print(f"- {kota}: {len(list_pkt)} paket")


if __name__ == "__main__":
    main()