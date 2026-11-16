from fplib import (
    alirkan,
    pilih_jika,
    transformasi,
    partisi_data,
    peringkat_dengan,
    format_metrik,
)

hasil_pertandingan = (
    {"tim": "Garuda Muda", "m": 4, "s": 1, "k": 0, "gm": 14, "gk": 4},
    {"tim": "Elang Utara", "m": 3, "s": 1, "k": 1, "gm": 11, "gk": 6},
    {"tim": "Rajawali FC", "m": 3, "s": 0, "k": 2, "gm": 9, "gk": 8},
    {"tim": "Banteng Selatan", "m": 1, "s": 2, "k": 2, "gm": 6, "gk": 9},
    {"tim": "Harimau Timur", "m": 0, "s": 0, "k": 5, "gm": 3, "gk": 16},
)


def hitung_statistik(tim):
    return {
        **tim,
        "poin": (tim["m"] * 3) + tim["s"],
        "selisih": tim["gm"] - tim["gk"],
    }


def main():
    klasemen = alirkan(
        hasil_pertandingan,
        lambda xs: transformasi(hitung_statistik, xs),
        lambda xs: peringkat_dengan(lambda t: (t["poin"], t["selisih"]), xs),
    )

    lolos, gugur = partisi_data(lambda t: t["poin"] >= 9, klasemen)
    agresif = pilih_jika(lambda t: t["gm"] >= 10, klasemen)

    print("KLASEMEN AKHIR TURNAMEN FUTSAL")
    for pos, t in enumerate(klasemen, start=1):
        pts = format_metrik(t["poin"], akhiran=" poin")
        print(f"{pos}. {t['tim']:<16} | {pts:<8} | SG: {t['selisih']:+d}")

    print("\nLolos fase gugur :", ", ".join(t["tim"] for t in lolos))
    print("Tidak lolos      :", ", ".join(t["tim"] for t in gugur))
    print("Tim produktif    :", ", ".join(t["tim"] for t in agresif))


if __name__ == "__main__":
    main()