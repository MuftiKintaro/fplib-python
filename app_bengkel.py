from fplib import (
    alirkan,
    komposisi,
    pilih_jika,
    transformasi,
    reduksi_rekursif,
    kelompokkan_dengan,
    buat_validator,
    format_metrik,
)

data_servis = (
    {"no": "B-101", "nama": "Rizky", "mekanik": "Pak Budi", "status": "Dikerjakan", "jasa": 150000, "part": 320000},
    {"no": "B-102", "nama": "Nadia", "mekanik": "Mas Dani", "status": "Selesai", "jasa": 95000, "part": 0},
    {"no": "B-103", "nama": "Fajar", "mekanik": "Pak Budi", "status": "Dikerjakan", "jasa": 210000, "part": 450000},
    {"no": "B-104", "nama": "Tari", "mekanik": "Mas Dani", "status": "Dikerjakan", "jasa": 120000, "part": 175000},
    {"no": "B-105", "nama": "", "mekanik": "Pak Budi", "status": "Dikerjakan", "jasa": -20000, "part": 50000},
)


def main():
    cek_data = buat_validator(
        (lambda x: len(x["nama"].strip()) > 0, "Nama kosong"),
        (lambda x: x["jasa"] >= 0 and x["part"] >= 0, "Nominal minus"),
    )

    # Hitung jasa + sparepart lalu tambah pajak 11%
    hitung_total_pajak = komposisi(
        lambda sub: round(sub * 1.11),
        lambda item: item["jasa"] + item["part"],
    )

    servis_valid = alirkan(
        data_servis,
        lambda xs: pilih_jika(lambda x: cek_data(x)[0], xs),
        lambda xs: transformasi(lambda x: {**x, "total_bayar": hitung_total_pajak(x)}, xs),
    )

    masih_proses = pilih_jika(lambda x: x["status"] == "Dikerjakan", servis_valid)
    bagi_mekanik = kelompokkan_dengan(lambda x: x["mekanik"], servis_valid)
    pendapatan = reduksi_rekursif(lambda acc, x: acc + x["total_bayar"], servis_valid, 0)

    print("REKAP ANTREAN SERVIS BENGKEL")
    print(f"Estimasi pemasukan (+PPN) : {format_metrik(pendapatan, awalan='Rp ')}")
    print(f"Unit masih dikerjakan     : {len(masih_proses)} motor\n")

    for item in servis_valid:
        biaya = format_metrik(item["total_bayar"], awalan="Rp ")
        print(f"[{item['no']}] {item['nama']} - {item['status']} ({biaya})")

    print("\nPembagian kerja mekanik:")
    for mekanik, tugas in bagi_mekanik.items():
        print(f"- {mekanik}: {len(tugas)} antrean")


if __name__ == "__main__":
    main()