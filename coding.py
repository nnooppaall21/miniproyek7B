import csv
import statistics

NAMA_FILE_DEFAULT = "pit_stops_race1054.csv"

KOLOM_WAJIB = [
    "driverId", "driver_code", "driver_name",
    "stop", "lap", "milliseconds"
]

BATAS_WAJAR_MIN = 15000
BATAS_WAJAR_MAX = 60000

DATA_CONTOH = [
    (1, "HAM", "Lewis Hamilton", 1, 12, 23120),
    (1, "HAM", "Lewis Hamilton", 2, 25, 22840),
    (1, "HAM", "Lewis Hamilton", 3, 38, 24310),
    (1, "HAM", "Lewis Hamilton", 4, 50, 22690),

    (830, "VER", "Max Verstappen", 1, 11, 22310),
    (830, "VER", "Max Verstappen", 2, 24, 22580),
    (830, "VER", "Max Verstappen", 3, 37, 22190),
    (830, "VER", "Max Verstappen", 4, 49, 41250),

    (822, "BOT", "Valtteri Bottas", 1, 13, 24870),
    (822, "BOT", "Valtteri Bottas", 2, 26, 25210),
    (822, "BOT", "Valtteri Bottas", 3, 39, 24560),
    (822, "BOT", "Valtteri Bottas", 4, 51, 25030),

    (846, "NOR", "Lando Norris", 1, 12, 23640),
    (846, "NOR", "Lando Norris", 2, 25, 23290),
    (846, "NOR", "Lando Norris", 3, 38, 23880),
    (846, "NOR", "Lando Norris", 4, 50, 23510),

    (817, "RIC", "Daniel Ricciardo", 1, 14, 25420),
    (817, "RIC", "Daniel Ricciardo", 2, 27, 24980),
    (817, "RIC", "Daniel Ricciardo", 3, 40, 25760),
    (817, "RIC", "Daniel Ricciardo", 4, 52, 25110),

    (4, "ALO", "Fernando Alonso", 1, 13, 24150),
    (4, "ALO", "Fernando Alonso", 2, 26, 23920),
    (4, "ALO", "Fernando Alonso", 3, 39, 24470),
    (4, "ALO", "Fernando Alonso", 4, 51, 24060),
]


def cover():
    def baris(teks=""):
        print("|" + teks.center(85) + "|")

    print("+" + "-" * 85 + "+")
    baris()
    baris()
    baris("MINI PROJECT")
    baris("PROGRAMA KOMPUTER")
    baris()
    baris("(Analisis Konsistensi dan Kinerja Waktu Pit Stop")
    baris("pada Balapan Formula 1)")
    baris()
    baris()
    baris("Oleh :")
    baris("Kelompok 7B")
    baris()
    baris("Anggota Kelompok :")
    baris("Stefan Virgo Zalukhu (2610932037)")
    baris("Muhammad Rifat Naufal (2610933007)")
    baris("Rafa Amalia Yurinov (2610932005)")
    baris("M. Dafa Al Saban (2610932001)")
    baris()
    baris()
    baris("Asisten Pembimbing :")
    baris("Faiza Mumtaz & Intan Permata Mustika")
    baris()
    baris()
    baris("Dosen Pengampu :")
    baris("Dr. Eng. Ardhian Agung Yulianto")
    baris()
    baris()
    baris("LABORATORIUM SISTEM INFORMASI DAN KEPUTUSAN")
    baris("DEPARTEMEN TEKNIK INDUSTRI")
    baris("FAKULTAS TEKNIK")
    baris("UNIVERSITAS ANDALAS")
    baris("2026")
    baris()
    baris()
    print("+" + "-" * 85 + "+")

    input("\nTekan Enter untuk melanjutkan...")

def buat_csv_contoh(path):
    try:
        with open(path, "w", newline="", encoding="utf-8") as f:
            penulis = csv.writer(f)
            penulis.writerow(KOLOM_WAJIB)
            penulis.writerows(DATA_CONTOH)

    except OSError as e:
        print("Gagal membuat berkas contoh:", e)
        return False

    print("Berkas contoh berhasil dibuat.")
    return True


def validasi_baris(baris):
    try:
        driver_id = int(baris["driverId"])
        stop = int(baris["stop"])
        lap = int(baris["lap"])
        ms = int(float(baris["milliseconds"]))

    except (ValueError, TypeError, KeyError):
        return None, "Data angka tidak valid"

    if ms < BATAS_WAJAR_MIN or ms > BATAS_WAJAR_MAX:
        return None, "Durasi di luar batas wajar"

    return {
        "driverId": driver_id,
        "driver_code": baris["driver_code"].strip(),
        "driver_name": baris["driver_name"].strip(),
        "stop": stop,
        "lap": lap,
        "ms": ms
    }, None


def baca_csv(path):
    valid = []
    tidak_valid = []

    try:
        with open(path, "r", newline="", encoding="utf-8-sig") as f:

            pembaca = csv.DictReader(f)

            if not pembaca.fieldnames:
                return "Header tidak ditemukan", [], []

            kolom_hilang = []

            for k in KOLOM_WAJIB:
                if k not in pembaca.fieldnames:
                    kolom_hilang.append(k)

            if kolom_hilang:
                return "Kolom tidak lengkap: " + str(kolom_hilang), [], []

            for no_baris, baris in enumerate(pembaca, start=2):

                if not any(baris.values()):
                    continue

                hasil, alasan = validasi_baris(baris)

                if hasil is None:
                    tidak_valid.append((no_baris, alasan))
                else:
                    valid.append(hasil)

    except FileNotFoundError:
        return "Berkas tidak ditemukan", [], []

    except (OSError, csv.Error, UnicodeDecodeError) as e:
        return "Gagal membaca berkas: " + str(e), [], []

    if not valid and not tidak_valid:
        return "Tidak terdapat data", [], []

    return "OK", valid, tidak_valid


def hitung_statistika(data):

    if len(data) == 0:
        return None

    # Mengubah milliseconds menjadi detik
    durasi = []

    for d in data:
        durasi.append(d["ms"] / 1000)

    jumlah = len(durasi)

    # Perhitungan statistika deskriptif
    rata = statistics.mean(durasi)
    median = statistics.median(durasi)

    nilai_min = min(durasi)
    nilai_max = max(durasi)

    rentang = nilai_max - nilai_min

    if jumlah >= 2:
        varians = statistics.variance(durasi)
        sd = statistics.stdev(durasi)
    else:
        varians = 0
        sd = 0

    # Koefisien variasi
    if rata != 0:
        kv = (sd / rata) * 100
    else:
        kv = 0

    return {
        "jumlah": jumlah,
        "rata": rata,
        "median": median,
        "min": nilai_min,
        "max": nilai_max,
        "rentang": rentang,
        "varians": varians,
        "sd": sd,
        "kv": kv
    }


def tampil_tabel(data):

    if not data:
        print("Tidak ada data yang cocok.")
        return

    print("-" * 86)
    print(
        f"{'No':>3} {'Driver ID':>10} {'Kode':<5} "
        f"{'Pembalap':<20} {'Stop':>4} {'Lap':>4} "
        f"{'Durasi(ms)':>12} {'Detik':>9}"
    )   
    
    print("-" * 86)

    for i, d in enumerate(data, start=1):

        detik = d["ms"] / 1000

        print(
            f"{i:>3} {d['driverId']:>10} "
            f"{d['driver_code']:<5} "
            f"{d['driver_name']:<20} "
            f"{d['stop']:>4} {d['lap']:>4} "
            f"{d['ms']:>12,} {detik:>9.3f}"
        )

    print("-" * 86)
    print("Total:", len(data), "pit stop")


def tampil_statistika(data):

    hasil = hitung_statistika(data)

    if hasil is None:
        print("Data tidak tersedia.")
        return

    print("\n" + "=" * 65)
    print("HASIL ANALISIS STATISTIKA DESKRIPTIF")
    print("=" * 65)

    print("Jumlah pengamatan :", hasil["jumlah"])
    print("Rata-rata (Mean) :", round(hasil["rata"], 3), "detik")
    print("Median :", round(hasil["median"], 3), "detik")
    print("Nilai minimum :", round(hasil["min"], 3), "detik")
    print("Nilai maksimum :", round(hasil["max"], 3), "detik")
    print("Rentang (Range) :", round(hasil["rentang"], 3), "detik")
    print("Varians :", round(hasil["varians"], 3))
    print("Standar deviasi :", round(hasil["sd"], 3), "detik")
    print("Koefisien variasi :", round(hasil["kv"], 2), "%")

    print("=" * 65)
    print("KESIMPULAN")

    print(
        "1. Rata-rata waktu pit stop adalah",
        round(hasil["rata"], 3), "detik."
    )

    print(
        "2. Nilai median waktu pit stop adalah",
        round(hasil["median"], 3), "detik."
    )

    print(
        "3. Rentang waktu pit stop adalah",
        round(hasil["rentang"], 3), "detik."
    )

    print(
        "4. Standar deviasi sebesar",
        round(hasil["sd"], 3), "detik."
    )

    if hasil["kv"] < 10:
        print("5. Variasi waktu relatif rendah.")
    elif hasil["kv"] < 20:
        print("5. Variasi waktu tergolong sedang.")
    else:
        print("5. Variasi waktu tergolong tinggi.")

    print("=" * 65)


def analisis_pembalap(data):

    if not data:
        print("Data tidak tersedia.")
        return

    daftar_id = []

    for d in data:
        if d["driverId"] not in daftar_id:
            daftar_id.append(d["driverId"])

    print("\n" + "=" * 78)
    print("PERBANDINGAN STATISTIKA ANTAR PEMBALAP")
    print("=" * 78)

    print(
        f"{'Kode':<7} {'Nama Pembalap':<22} "
        f"{'Jumlah':>7} {'Mean':>10} {'Median':>10} {'SD':>10}"
    )

    print("-" * 78)

    for id_pembalap in daftar_id:

        data_pembalap = []

        for d in data:
            if d["driverId"] == id_pembalap:
                data_pembalap.append(d)

        hasil = hitung_statistika(data_pembalap)

        print(
            f"{data_pembalap[0]['driver_code']:<7} "
            f"{data_pembalap[0]['driver_name']:<22} "
            f"{hasil['jumlah']:>7} "
            f"{hasil['rata']:>10.3f} "
            f"{hasil['median']:>10.3f} "
            f"{hasil['sd']:>10.3f}"
        )

    print("-" * 78)


def menu_filter(data):

    print("\nFILTER DATA")
    print("1. Berdasarkan ID pembalap")
    print("2. Berdasarkan nomor pit stop")
    print("3. Berdasarkan keduanya")

    pilihan = input("Pilih [1-3]: ").strip()

    if pilihan not in ("1", "2", "3"):
        print("Pilihan tidak valid.")
        return None

    hasil = data

    if pilihan in ("1", "3"):

        try:
            nilai = int(input("Masukkan driverId: "))

        except ValueError:
            print("ID harus berupa angka.")
            return None

        hasil = [
            d for d in hasil
            if d["driverId"] == nilai
        ]

    if pilihan in ("2", "3"):

        try:
            nilai = int(input("Masukkan nomor stop: "))

        except ValueError:
            print("Nomor stop harus berupa angka.")
            return None

        hasil = [
            d for d in hasil
            if d["stop"] == nilai
        ]

    if not hasil:
        print("Data tidak ditemukan.")
        return None

    return hasil


def muat_data(path):

    status, valid, tidak_valid = baca_csv(path)

    print("\n" + "=" * 65)
    print("STATUS PEMBACAAN BERKAS")
    print("=" * 65)

    print("Status :", status)
    print("Jumlah data valid :", len(valid))
    print("Jumlah data tidak valid :", len(tidak_valid))

    for no, alasan in tidak_valid:
        print("Baris", no, ":", alasan)

    return status == "OK", valid


def main():

    cover()

    path_default = NAMA_FILE_DEFAULT

    try:
        with open(path_default, "r", encoding="utf-8"):
            pass

    except FileNotFoundError:
        buat_csv_contoh(path_default)

    ok, data = muat_data(path_default)

    while True:

        print("\n" + "=" * 65)
        print(" ANALISIS WAKTU PIT STOP FORMULA 1 ")
        print(" METODE STATISTIKA")
        print("=" * 65)

        print("1. Muat ulang / ganti berkas CSV")
        print("2. Tampilkan semua data pit stop")
        print("3. Tampilkan data dengan filter")
        print("4. Analisis statistika seluruh data")
        print("5. Analisis statistika hasil filter")
        print("6. Perbandingan statistika antar pembalap")
        print("0. Keluar")

        pilihan = input("Pilih menu [0-6]: ").strip()

        if pilihan == "0":

            print("Terima kasih. Program selesai.")
            break

        elif pilihan == "1":

            masukan = input(
                "Nama/path berkas CSV [Enter = default]: "
            ).strip()

            path = masukan if masukan else path_default

            ok, data = muat_data(path)

        elif pilihan in ("2", "3", "4", "5", "6"):

            if not ok or not data:
                print("Belum ada data valid. Muat berkas terlebih dahulu.")
                continue

            if pilihan == "2":
                tampil_tabel(data)

            elif pilihan == "3":
                hasil = menu_filter(data)

                if hasil:
                    tampil_tabel(hasil)

            elif pilihan == "4":
                tampil_statistika(data)

            elif pilihan == "5":
                hasil = menu_filter(data)

                if hasil:
                    tampil_statistika(hasil)

            elif pilihan == "6":
                analisis_pembalap(data)

        else:
            print("Pilihan tidak valid, coba lagi.")


if __name__ == "__main__":
    main()