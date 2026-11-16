from fplib import (
    alirkan,
    pilih_jika,
    transformasi,
    reduksi_rekursif,
    partisi_data,
    kelompokkan_dengan,
    peringkat_dengan,
    format_metrik,
)

catatan_olahraga = (
    {"hari": "Senin", "tipe": "Kardio", "latihan": "Jogging", "menit": 40, "kal_menit": 11},
    {"hari": "Selasa", "tipe": "Beban", "latihan": "Dumbell & Bench", "menit": 50, "kal_menit": 8},
    {"hari": "Rabu", "tipe": "Stretching", "latihan": "Yoga", "menit": 30, "kal_menit": 4},
    {"hari": "Kamis", "tipe": "Kardio", "latihan": "Sepeda Statis", "menit": 45, "kal_menit": 10},
    {"hari": "Sabtu", "tipe": "Beban", "latihan": "Pull Up & Squat", "menit": 35, "kal_menit": 7},
)


def tambah_total_kalori(sesi):
    return {**sesi, "kalori": sesi["menit"] * sesi["kal_menit"]}


def main():
    semua_sesi = transformasi(tambah_total_kalori, catatan_olahraga)
    berat, ringan = partisi_data(lambda s: s["kalori"] >= 350, semua_sesi)

    urutan_tertinggi = alirkan(
        semua_sesi,
        lambda xs: pilih_jika(lambda s: s["menit"] >= 35, xs),
        lambda xs: peringkat_dengan(lambda s: s["kalori"], xs),
    )

    per_tipe = kelompokkan_dengan(lambda s: s["tipe"], semua_sesi)
    total_kalori = reduksi_rekursif(lambda acc, s: acc + s["kalori"], semua_sesi, 0)
    total_waktu = reduksi_rekursif(lambda acc, s: acc + s["menit"], semua_sesi, 0)

    print("CATATAN WORKOUT MINGGUAN")
    print(f"Durasi total  : {format_metrik(total_waktu, akhiran=' menit')}")
    print(f"Kalori keluar : {format_metrik(total_kalori, akhiran=' kkal')}")
    print(f"Sesi berat (>=350 kkal): {len(berat)}x | Sesi ringan: {len(ringan)}x\n")

    print("Urutan latihan >= 35 menit:")
    for s in urutan_tertinggi:
        kal = format_metrik(s["kalori"], akhiran=" kkal")
        print(f"  {s['hari']}: {s['latihan']} ({s['menit']} mnt) -> {kal}")

    print("\nJumlah sesi per tipe:")
    for tipe, daftar in per_tipe.items():
        print(f"  {tipe}: {len(daftar)} sesi")


if __name__ == "__main__":
    main()