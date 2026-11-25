


import csv
import os
import statistics

NAMA_FILE_DEFAULT = "pit_stops_race1054.csv"
KOLOM_WAJIB = ["driverId", "driver_code", "driver_name", "stop", "lap", "milliseconds"]

BATAS_WAJAR_MIN = 15000
BATAS_WAJAR_MAX = 60000

AMBANG_EFISIEN_DEFAULT = 22000
AMBANG_NORMAL_DEFAULT = 25000

KATEGORI_URUT = ["Sangat Efisien", "Normal", "Perlu Evaluasi"]


def baca_csv(path):
    """
    Membaca berkas CSV dan memisahkan baris valid dan tidak valid.
    Mengembalikan (status, baris_valid, baris_tidak_valid).
    status = "OK" atau pesan kesalahan.
    """
    if not os.path.isfile(path):
        return f"Berkas '{path}' tidak ditemukan.", [], []

    if os.path.getsize(path) == 0:
        return "Berkas kosong (tidak ada isi sama sekali).", [], []

    valid, tidak_valid = [], []
    try:
        with open(path, newline="", encoding="utf-8-sig") as f:
            pembaca = csv.DictReader(f)

            if not pembaca.fieldnames:
                return "Berkas kosong (header tidak ditemukan).", [], []

            kolom_hilang = [k for k in KOLOM_WAJIB if k not in pembaca.fieldnames]
            if kolom_hilang:
                return ("Kolom wajib tidak ada: " + ", ".join(kolom_hilang) + "."), [], []

            for no_baris, baris in enumerate(pembaca, start=2):  
                if not any((v or "").strip() for v in baris.values()):
                    continue
                hasil, alasan = validasi_baris(baris)
                if hasil is None:
                    tidak_valid.append((no_baris, alasan))
                else:
                    valid.append(hasil)
    except (OSError, UnicodeDecodeError, csv.Error) as e:
        return f"Gagal membaca berkas: {e}", [], []

    if not valid and not tidak_valid:
        return "Berkas hanya berisi header, tidak ada data.", [], []

    return "OK", valid, tidak_valid