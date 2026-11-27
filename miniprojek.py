import csv
import os

NAMA_FILE_DEFAULT = "pit_stops_race1054.csv"
NAMA_FILE_PENGGUNA = "pengguna.csv"
MAKS_PERCOBAAN_LOGIN = 3

KOLOM_WAJIB = [
    "driverId", "driver_code", "driver_name",
    "stop", "lap", "milliseconds"
]

BATAS_WAJAR_MIN = 15000
BATAS_WAJAR_MAX = 60000



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


def siapkan_pengguna():   
    if not os.path.exists(NAMA_FILE_PENGGUNA):
        try:
            with open(NAMA_FILE_PENGGUNA, "w", newline="", encoding="utf-8") as f:
                penulis = csv.writer(f)
                penulis.writerow(["username", "password"])
                penulis.writerow(["admin", "123456"])
        except OSError as e:
            print("Gagal membuat berkas pengguna:", e)

    akun = {}

    try:
        with open(NAMA_FILE_PENGGUNA, "r", newline="", encoding="utf-8-sig") as f:
            for baris in csv.DictReader(f):
                akun[baris["username"]] = baris["password"]
    except (OSError, KeyError, csv.Error) as e:
        print("Gagal membaca berkas pengguna:", e)

    return akun


def menu_login():
    akun = siapkan_pengguna()

    while True:
        print("=" * 65)
        print(" LOGIN - ANALISIS WAKTU PIT STOP FORMULA 1 ")
        print("=" * 65)
        print("1. Daftar akun baru")
        print("2. Login")
        print("3. Keluar")

        pilihan = input("Pilih menu [1-3]: ").strip()

        if pilihan == "3":
            return False

        elif pilihan == "2":
            for percobaan in range(1, MAKS_PERCOBAAN_LOGIN + 1):
                user = input("Username : ").strip()
                sandi = input("Password : ").strip()

                if user in akun and akun[user] == sandi:
                    print("\nLogin berhasil. Selamat datang,", user + "!")
                    input("Tekan Enter untuk melanjutkan...")
                    return True

                sisa = MAKS_PERCOBAAN_LOGIN - percobaan
                print("Username atau password salah. Sisa percobaan:", sisa)

            print("Percobaan login habis.")
            input("Tekan Enter untuk kembali...")

        elif pilihan == "1":
            user = input("Username baru (minimal 4 karakter) : ").strip()
            sandi = input("Password baru (6 digit angka) : ").strip()

            if len(user) < 4:
                print("Username minimal 4 karakter.")
            elif "," in user:
                print("Username hanya mengandung huruf dan angka.")
            elif len(sandi) != 6 or not sandi.isdigit():
                print("Password harus tepat 6 karakter dan berupa angka.")
            elif user in akun:
                print("Username sudah terdaftar.")
            else:
                try:
                    with open(NAMA_FILE_PENGGUNA, "a", newline="", encoding="utf-8") as f:
                        csv.writer(f).writerow([user, sandi])
                    akun[user] = sandi
                    print("Akun berhasil dibuat. Silakan login.")
                except OSError as e:
                    print("Gagal menyimpan akun:", e)

            input("Tekan Enter untuk melanjutkan...")

        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk melanjutkan...")


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

    except (OSError, csv.Error,) as e:
        return "Gagal membaca berkas: " + str(e), [], []

    if not valid and not tidak_valid:
        return "Tidak terdapat data", [], []

    return "OK", valid, tidak_valid


def hitung_statistika(data):

    if len(data) == 0:
        return None

    durasi = []

    for d in data:
        durasi.append(d["ms"] / 1000)

    jumlah = len(durasi)

    rata = sum(durasi) / jumlah

    urut = sorted(durasi)
    tengah = jumlah // 2

    if jumlah % 2 == 1:
        median = urut[tengah]
    else:
        median = (urut[tengah - 1] + urut[tengah]) / 2

    nilai_min = urut[0]
    nilai_max = urut[-1]
    rentang = nilai_max - nilai_min

    if jumlah >= 2:
        total_kuadrat = 0

        for x in durasi:
            total_kuadrat += (x - rata) ** 2

        varians = total_kuadrat / (jumlah - 1)
        sd = varians ** 0.5
    else:
        varians = 0
        sd = 0

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
        f"{'Detik':>9}"
    )

    print("-" * 86)

    for i, d in enumerate(data, start=1):

        detik = d["ms"] / 1000

        print(
            f"{i:>3} {d['driverId']:>10} "
            f"{d['driver_code']:<5} "
            f"{d['driver_name']:<20} "
            f"{d['stop']:>4} {d['lap']:>4} "
            f"{detik:>9}"
        )

    print("-" * 86)
    print("Total:", len(data), "pit stop")


def tampil_statistika(data):

    hasil = hitung_statistika(data)

    if hasil is None:
        print("Data tidak tersedia.")
        return

    print("\n" + "=" * 65)
    print("HASIL ANALISIS STATISTIKA WAKTU PIT STOP")
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

    print("1. Rata-rata waktu pit stop adalah", round(hasil["rata"], 3), "detik.")
    print("2. Nilai median waktu pit stop adalah", round(hasil["median"], 3), "detik.")
    print("3. Rentang waktu pit stop adalah", round(hasil["rentang"], 3), "detik.")
    print("4. Standar deviasi sebesar", round(hasil["sd"], 3), "detik.")

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


def menu_filter(data, banyak=False):   

    print("\nFILTER DATA")
    print("1. Berdasarkan ID pembalap")
    print("2. Berdasarkan nomor pit stop")

    pilihan = input("Pilih [1-2]: ").strip()

    if pilihan not in ("1", "2"):
        print("Pilihan tidak valid.")
        return None

    hasil = data

    if pilihan in ("1"):

        if banyak:
            teks = input("Masukkan driverId (pisahkan dengan koma, minimal 2): ")
        else:
            teks = input("Masukkan driverId: ")

        try:
            daftar = [int(x) for x in teks.split(",")]

        except ValueError:
            print("ID harus berupa angka.")
            return None

        if not banyak:
            daftar = daftar[:1]

        hasil = [d for d in hasil if d["driverId"] in daftar]

        if banyak:
            ada = []

            for d in hasil:
                if d["driverId"] not in ada:
                    ada.append(d["driverId"])

            if len(set(daftar)) < 2 or len(ada) < 2:
                print("Perbandingan membutuhkan minimal 2 driverId berbeda yang ada di data.")
                return None

    if pilihan in ("2"):

        try:
            nilai = int(input("Masukkan nomor stop: "))

        except ValueError:
            print("Nomor stop harus berupa angka.")
            return None

        hasil = [d for d in hasil if d["stop"] == nilai]

    if not hasil:
        print("Data tidak ditemukan.")
        return None

    return hasil


def pilih_data(data, banyak=False):

    print("\nPILIH DATA")
    print("1. Semua data")
    print("2. Data filter")

    pilihan = input("Pilih [1-2]: ").strip()

    if pilihan == "1":
        return data

    elif pilihan == "2":
        return menu_filter(data, banyak)

    print("Pilihan tidak valid.")
    return None


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

    if not menu_login():
        print("Program ditutup.")
        return

    ok, data = muat_data(NAMA_FILE_DEFAULT)

    if not ok:
        print("Program tidak dapat dilanjutkan tanpa data valid.")
        return

    while True:

        print("\n" + "=" * 65)
        print(" ANALISIS WAKTU PIT STOP FORMULA 1 ")
        print(" METODE STATISTIKA")
        print("=" * 65)

        print("1. Tampilkan data pit stop")
        print("2. Analisis statistika")
        print("3. Perbandingan statistika antar pembalap")
        print("4. Keluar")

        pilihan = input("Pilih menu [1-4]: ").strip()

        if pilihan == "4":

            print("Terima kasih. Program selesai.")
            break

        elif pilihan in ("1", "2", "3"):

            hasil = pilih_data(data, pilihan == "3")

            if hasil:

                if pilihan == "1":
                    tampil_tabel(hasil)

                elif pilihan == "2":
                    tampil_statistika(hasil)

                elif pilihan == "3":
                    analisis_pembalap(hasil)

        else:
            print("Pilihan tidak valid, coba lagi.")


if __name__ == "__main__":
    main()