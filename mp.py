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
def validasi_baris(baris):
    """Memeriksa satu baris. Mengembalikan (dict_bersih, None) atau (None, alasan)."""
    try:
        driver_id = int(baris["driverId"].strip())
        stop = int(baris["stop"].strip())
        lap = int(baris["lap"].strip())
    except (ValueError, AttributeError):
        return None, "driverId/stop/lap bukan angka"

    try:
        ms = int(float(baris["milliseconds"].strip()))
    except (ValueError, AttributeError):
        return None, "durasi (milliseconds) bukan angka"

    if ms < BATAS_WAJAR_MIN or ms > BATAS_WAJAR_MAX:
        return None, f"durasi {ms} ms di luar batas wajar ({BATAS_WAJAR_MIN}-{BATAS_WAJAR_MAX} ms)"

    return {
        "driverId": driver_id,
        "driver_code": baris["driver_code"].strip(),
        "driver_name": baris["driver_name"].strip(),
        "stop": stop,
        "lap": lap,
        "ms": ms,
    }, None


def validasi_ambang(efisien, normal):
    """Ambang harus angka positif dan efisien < normal. Mengembalikan pesan error atau None."""
    try:
        e = float(efisien)
        n = float(normal)
    except (ValueError, TypeError):
        return "Ambang harus berupa angka."
    if e <= 0 or n <= 0:
        return "Ambang harus bernilai positif."
    if e >= n:
        return "Ambang 'Sangat Efisien' harus lebih kecil dari ambang 'Normal'."
    return None


def saring_data(data, driver_id=None, stop=None):
    """Memilih baris berdasarkan ID pembalap dan/atau nomor pemberhentian."""
    hasil = data
    if driver_id is not None:
        hasil = [d for d in hasil if d["driverId"] == driver_id]
    if stop is not None:
        hasil = [d for d in hasil if d["stop"] == stop]
    return hasil