# Analisis Konsistensi dan Kinerja Waktu Pit Stop pada Balapan Formula 1 Menggunakan Metode Statistika

Program berbasis antarmuka teks (*command line*) yang dikembangkan dengan bahasa Python untuk menganalisis konsistensi dan kinerja waktu *pit stop* pada Portuguese Grand Prix 2021. Program membaca data durasi *pit stop* dari berkas CSV, memvalidasi isinya, lalu menghitung ukuran pemusatan dan penyebaran data (rata-rata, median, rentang, varians, standar deviasi, dan koefisien variasi), baik untuk seluruh data, pembalap tertentu, maupun nomor pemberhentian tertentu. Akses ke program dilindungi oleh sistem login sederhana.

Proyek ini disusun sebagai *Mini Project* Programa Komputer, Laboratorium Sistem Informasi dan Keputusan, Departemen Teknik Industri, Fakultas Teknik, Universitas Andalas.

## Daftar Isi

1. [Latar Belakang](#latar-belakang)
2. [Tujuan](#tujuan)
3. [Fitur Utama](#fitur-utama)
4. [Metodologi](#metodologi)
5. [Struktur Repositori](#struktur-repositori)
6. [Persyaratan Sistem](#persyaratan-sistem)
7. [Cara Menjalankan Program](#cara-menjalankan-program)
8. [Panduan Penggunaan](#panduan-penggunaan)
9. [Format Data](#format-data)
10. [Keterbatasan](#keterbatasan)
11. [Tim Pengembang](#tim-pengembang)

---

## Latar Belakang

Dalam Teknik Industri, lamanya suatu pekerjaan diukur dengan Pengukuran Waktu Kerja (*Time Study*), yang dipelajari pada mata kuliah Studi Gerak dan Waktu. Metode ini cocok untuk pekerjaan yang berulang, singkat, dan berpola sama, lalu hasilnya dinilai dari seberapa stabil waktunya. *Pit stop* pada balap Formula 1 memenuhi ciri tersebut: dilakukan berulang kali, hanya memakan puluhan detik, langkah kerjanya sama setiap kali, dan selisih yang kecil saja dapat menggeser posisi pembalap.

Dataset yang dipakai memuat 60 pemberhentian dari 19 pembalap dengan durasi sekitar 21 sampai 29 detik. Durasi itu tidak seragam: sebagian selesai dalam kisaran 21 sampai 22 detik, sedangkan yang lain mencapai 26 sampai 28 detik. Menghitung rata-rata dan simpangan secara manual, apalagi membandingkannya antar pembalap, memakan waktu dan mudah salah. Karena itu dibutuhkan program yang membaca data, memeriksa kelayakannya, dan menghitung ukuran statistika secara otomatis.

Landasan ilmiahnya adalah penelitian Heilmeier dkk. (2020) yang menunjukkan bahwa durasi *pit stop* bervariasi antar tim, sehingga perlu dipandang sebagai data yang bervariasi dan diukur sebarannya, bukan hanya rata-ratanya.

---

## Tujuan

- Membaca berkas CSV *pit stop* dan memeriksa kelengkapan serta kewajaran isinya.
- Menghitung rata-rata, median, nilai minimum, nilai maksimum, rentang, varians, standar deviasi, dan koefisien variasi durasi *pit stop*.
- Menampilkan data *pit stop* secara keseluruhan maupun hasil penyaringan berdasarkan pembalap atau nomor pemberhentian.
- Membandingkan statistika antar pembalap untuk melihat perbedaan kinerja dan konsistensi.
- Memberikan kesimpulan singkat tentang tingkat variasi waktu *pit stop*.
- Membatasi akses program melalui menu login dan pendaftaran akun.

---

## Fitur Utama

| No | Fitur | Keterangan |
| :-: | --- | --- |
| 1 | Halaman sampul | Menampilkan identitas kelompok, asisten pembimbing, dan dosen pengampu saat program dimulai |
| 2 | Login dan pendaftaran akun | Daftar akun baru, login dengan batas 3 kali percobaan, dan keluar. Akun disimpan pada `pengguna.csv` |
| 3 | Pembacaan dan validasi CSV | Mendeteksi header tidak ada, kolom wajib hilang, nilai bukan angka, dan durasi di luar 15.000 sampai 60.000 ms. Baris tidak valid ditampilkan beserta nomor barisnya |
| 4 | Tampilan data *pit stop* | Tabel berisi ID pembalap, kode, nama, nomor stop, putaran, dan durasi dalam detik |
| 5 | Penyaringan data | Berdasarkan ID pembalap atau nomor pemberhentian |
| 6 | Analisis statistika | Jumlah pengamatan, rata-rata, median, minimum, maksimum, rentang, varians, standar deviasi, dan koefisien variasi, disertai kesimpulan otomatis |
| 7 | Perbandingan antar pembalap | Tabel jumlah data, rata-rata, median, dan standar deviasi untuk dua pembalap atau lebih |
| 8 | Penanganan kesalahan | Input tidak valid ditolak dengan pesan, tanpa menghentikan program |

---

## Metodologi

Analisis dilakukan dalam empat langkah sederhana:

1. **Membaca data.** Program membaca berkas CSV dan memeriksa apakah kolom wajib ada, nilainya berupa angka, dan durasinya wajar (15.000 sampai 60.000 ms). Baris yang tidak lolos tidak dipakai.
2. **Memilih data.** Pengguna memilih semua data atau hanya data tertentu (satu pembalap atau satu nomor pemberhentian).
3. **Menghitung statistika.** Durasi diubah ke detik, lalu dihitung ukuran pemusatan dan penyebarannya.
4. **Menilai hasil.** Program menampilkan kesimpulan berdasarkan koefisien variasi (CV): semakin kecil CV, semakin konsisten waktunya.

### Rumus yang dipakai

Misalkan $x_1, x_2, \dots, x_n$ adalah durasi *pit stop* dalam detik.

| Ukuran | Rumus | Arti |
| --- | --- | --- |
| Rata-rata | $\bar{x} = \dfrac{\sum x_i}{n}$ | Nilai tengah hitungan |
| Median | Nilai di tengah data yang sudah diurutkan | Nilai tengah posisi |
| Rentang | $R = x_{\max} - x_{\min}$ | Selisih terlama dan tercepat |
| Varians | $s^2 = \dfrac{\sum (x_i - \bar{x})^2}{n-1}$ | Ukuran sebaran data |
| Standar deviasi | $s = \sqrt{s^2}$ | Sebaran dalam satuan detik |
| Koefisien variasi | $CV = \dfrac{s}{\bar{x}} \times 100\%$ | Sebaran relatif terhadap rata-rata |

Jika data hanya satu, varians dan standar deviasi dianggap 0.

### Kriteria penilaian variasi

| Koefisien variasi | Kesimpulan program |
| --- | --- |
| Kurang dari 10% | Variasi waktu relatif rendah |
| 10% sampai kurang dari 20% | Variasi waktu tergolong sedang |
| 20% atau lebih | Variasi waktu tergolong tinggi |

---

## Struktur Repositori

```text
.
├── mp.py                                     # Program utama
├── pit_stops_race1054.csv                    # Dataset pit stop Portuguese GP 2021
├── pengguna.csv                              # Data akun (dibuat otomatis saat pertama dijalankan)
└── README.md                                 # Dokumentasi proyek
```

### Struktur fungsi pada program

| Kelompok | Fungsi | Keterangan |
| --- | --- | --- |
| Tampilan awal | `cover()` | Menampilkan halaman sampul |
| Akun | `siapkan_pengguna()`, `menu_login()` | Menyiapkan `pengguna.csv`, menampilkan menu login dan pendaftaran |
| Data | `validasi_baris()`, `baca_csv()`, `muat_data()` | Memvalidasi satu baris, membaca seluruh berkas, dan menampilkan status pembacaan |
| Perhitungan | `hitung_statistika()` | Menghitung seluruh ukuran statistika |
| Tampilan hasil | `tampil_tabel()`, `tampil_statistika()`, `analisis_pembalap()` | Menampilkan tabel, hasil analisis, dan perbandingan antar pembalap |
| Pemilihan data | `menu_filter()`, `pilih_data()` | Menyaring data berdasarkan pilihan pengguna |
| Utama | `main()` | Mengatur alur program dan menu utama |

Program hanya memakai modul bawaan Python: `csv` dan `os`.

---

## Persyaratan Sistem

- Python 3.6 atau lebih baru (program memakai *f-string*)
- Sistem operasi Windows, macOS, atau Linux
- Terminal atau *command prompt*
- Tidak ada pustaka tambahan yang perlu dipasang

---

## Cara Menjalankan Program

1. Unduh atau *clone* repositori ini.

   ```bash
   git clone https://github.com/<username>/<nama-repositori>.git
   cd <nama-repositori>
   ```

2. Pastikan `pit_stops_race1054.csv` tersedia, lalu sesuaikan lokasinya pada baris berikut di `mp.py`:

   ```python
   file_csv = r"C:\semester 1\miniproyek7B\pit_stops_race1054.csv"
   ```

   Jika berkas CSV berada di folder yang sama dengan `mp.py`, ubah menjadi:

   ```python
   file_csv = "pit_stops_race1054.csv"
   ```

3. Jalankan program dari folder repositori.

   ```bash
   python mp.py
   ```

   Di sebagian sistem, gunakan `python3 mp.py`.

4. Saat pertama dijalankan, program membuat `pengguna.csv` berisi satu akun bawaan:

   | Username | Password |
   | --- | --- |
   | `admin` | `123456` |

---

## Panduan Penggunaan

### 1. Halaman sampul

Setelah program dijalankan, halaman sampul tampil. Tekan **Enter** untuk melanjutkan.

### 2. Menu login

| Menu | Fungsi |
| :-: | --- |
| 1 | Daftar akun baru |
| 2 | Login |
| 3 | Keluar |

**Aturan pendaftaran akun**

- Username minimal 4 karakter dan tidak boleh mengandung koma.
- Password harus tepat 6 karakter dan berupa angka.
- Username tidak boleh sama dengan akun yang sudah ada.

**Aturan login:** tersedia 3 kali percobaan. Jika habis, pengguna kembali ke menu login.

### 3. Pembacaan data

Setelah login berhasil, program membaca CSV dan menampilkan status pembacaan. Bila data tidak valid secara keseluruhan (misalnya kolom wajib hilang), program berhenti.

### 4. Menu utama

| Menu | Fungsi |
| :-: | --- |
| 1 | Tampilkan data *pit stop* |
| 2 | Analisis statistika |
| 3 | Perbandingan statistika antar pembalap |
| 4 | Keluar |

Untuk menu 1 sampai 3, program menanyakan data yang dipakai:

| Pilihan | Keterangan |
| :-: | --- |
| 1 | Semua data |
| 2 | Data filter (berdasarkan ID pembalap atau nomor *pit stop*) |

Pada menu 3 (perbandingan), filter ID pembalap menerima beberapa ID yang dipisahkan koma dan minimal dua pembalap berbeda.

**Contoh ID pembalap:** 1 = Hamilton, 830 = Verstappen, 822 = Bottas, 846 = Norris, 844 = Leclerc.

### 5. Contoh alur

- Melihat seluruh statistika: menu `2`, lalu `1`.
- Statistika pemberhentian ke-3 saja: menu `2`, lalu `2`, pilih `2`, masukkan `3`.
- Membandingkan Hamilton, Verstappen, dan Bottas: menu `3`, lalu `2`, pilih `1`, masukkan `1,830,822`.

### 6. Contoh output

Contoh berikut dihasilkan dari `pit_stops_race1054.csv` (60 baris valid, 0 tidak valid).

**Status pembacaan berkas**

```text
=================================================================
STATUS PEMBACAAN BERKAS
=================================================================
Status : OK
Jumlah data valid : 60
Jumlah data tidak valid : 0
```

**Tampilan data (menu 1, cuplikan tiga baris pertama)**

```text
--------------------------------------------------------------------------------------
 No  Driver ID Kode  Pembalap             Stop  Lap     Detik
--------------------------------------------------------------------------------------
  1        822 BOT   Valtteri Bottas         1    2    21.377
  2          1 HAM   Lewis Hamilton          1    2    22.426
  3        830 VER   Max Verstappen          1    2    22.718
--------------------------------------------------------------------------------------
```

**Analisis statistika (menu 2, semua data)**

```text
=================================================================
HASIL ANALISIS STATISTIKA WAKTU PIT STOP
=================================================================
Jumlah pengamatan : 60
Rata-rata (Mean) : 23.768 detik
Median : 22.456 detik
Nilai minimum : 21.275 detik
Nilai maksimum : 28.639 detik
Rentang (Range) : 7.364 detik
Varians : 5.552
Standar deviasi : 2.356 detik
Koefisien variasi : 9.91 %
=================================================================
KESIMPULAN
1. Rata-rata waktu pit stop adalah 23.768 detik.
2. Nilai median waktu pit stop adalah 22.456 detik.
3. Rentang waktu pit stop adalah 7.364 detik.
4. Standar deviasi sebesar 2.356 detik.
5. Variasi waktu relatif rendah.
=================================================================
```

**Perbandingan antar pembalap (menu 3, ID 1, 830, 822)**

```text
==============================================================================
PERBANDINGAN STATISTIKA ANTAR PEMBALAP
==============================================================================
Kode    Nama Pembalap           Jumlah       Mean     Median         SD
------------------------------------------------------------------------------
BOT     Valtteri Bottas              4     24.240     24.322      2.922
HAM     Lewis Hamilton               3     23.832     22.426      2.666
VER     Max Verstappen               4     24.471     24.518      2.398
------------------------------------------------------------------------------
```

**Catatan membaca hasil.** Rata-rata (23,768 detik) berada jauh di atas median (22,456 detik), yang menandakan sebaran data condong ke durasi yang lebih lama. Pola ini sejalan dengan data: semua pemberhentian ke-1 dan ke-2 berada pada 21,275 sampai 23,532 detik, sedangkan pemberhentian ke-3 dan ke-4 berada pada 25,892 sampai 28,639 detik. Jika dianalisis per nomor pemberhentian, variasinya jauh lebih kecil (pemberhentian ke-3: rata-rata 26,782 detik, CV 2,21%). Nilai CV keseluruhan sebesar 9,91% lebih mencerminkan perbedaan antar nomor pemberhentian daripada ketidakstabilan kerja dalam satu pemberhentian. Data tidak memuat penyebab perbedaan tersebut.

---

## Format Data

Berkas CSV harus memiliki header dan memuat kolom berikut.

| Kolom | Tipe | Wajib | Keterangan |
| --- | --- | :-: | --- |
| `raceId` | Bilangan bulat | Tidak | ID balapan (1054) |
| `year` | Bilangan bulat | Tidak | Tahun balapan (2021) |
| `race_name` | Teks | Tidak | Nama balapan |
| `driverId` | Bilangan bulat | Ya | ID pembalap |
| `driver_code` | Teks | Ya | Kode tiga huruf pembalap |
| `driver_name` | Teks | Ya | Nama pembalap |
| `stop` | Bilangan bulat | Ya | Nomor pemberhentian |
| `lap` | Bilangan bulat | Ya | Putaran saat masuk *pit* |
| `time` | Teks | Tidak | Waktu jam saat pemberhentian |
| `duration` | Desimal | Tidak | Durasi dalam detik |
| `milliseconds` | Bilangan bulat | Ya | Durasi dalam milidetik, dipakai untuk semua perhitungan |

**Contoh isi berkas**

```csv
raceId,year,race_name,driverId,driver_code,driver_name,stop,lap,time,duration,milliseconds
1054,2021,Portuguese Grand Prix,822,BOT,Valtteri Bottas,1,2,15:06:11,21.377,21377
1054,2021,Portuguese Grand Prix,1,HAM,Lewis Hamilton,1,2,15:06:13,22.426,22426
```

**Aturan validasi**

- Kolom wajib harus ada; jika tidak, pembacaan dihentikan dengan pesan kolom yang hilang.
- `driverId`, `stop`, `lap`, dan `milliseconds` harus berupa angka.
- `milliseconds` harus berada pada rentang 15.000 sampai 60.000.
- Baris kosong dilewati; baris yang gagal validasi dicatat beserta nomor barisnya dan tidak ikut dihitung.

**Berkas akun (`pengguna.csv`)**

```csv
username,password
admin,123456
```

**Sumber data:** dataset *Formula 1 World Championship* di Kaggle, disaring untuk Portuguese Grand Prix 2021 (`raceId` 1054).

---

## Keterbatasan

1. Data hanya berasal dari **satu balapan** (60 baris), sehingga hasil tidak dapat digeneralisasi ke balapan atau musim lain.
2. Analisis hanya memakai **total durasi pelayanan di jalur *pit***, tanpa membedakan tahap kerja mekanik, jenis ban, maupun tim.
3. Program memakai **statistika deskriptif**. Tidak ada uji hipotesis, standar waktu, atau penghitungan waktu baku seperti pada *Time Study* lengkap.
4. Penilaian variasi memakai batas CV tetap (10% dan 20%) yang tidak diturunkan dari standar resmi.
5. Nilai CV untuk seluruh data **mencampur** pemberhentian ke-1, 2, 3, dan 4, sehingga perbedaan antar nomor pemberhentian ikut terhitung sebagai variasi.
6. Lokasi berkas CSV tertulis **langsung di dalam kode** (`file_csv`) dan harus disesuaikan di setiap komputer.
7. Sistem login bersifat **sederhana**: password disimpan sebagai teks biasa pada `pengguna.csv`, dan akun bawaan `admin` / `123456` dapat diketahui siapa saja yang membaca repositori. Sistem ini ditujukan untuk keperluan tugas, bukan keamanan sungguhan.
8. Validasi username hanya menolak koma; karakter lain tidak diperiksa.
9. Perbandingan antar pembalap hanya menampilkan jumlah data, rata-rata, median, dan standar deviasi, dan pembalap dengan data sedikit (3 sampai 4 *pit stop*) memberi estimasi yang kurang stabil.
10. Program berjalan melalui **antarmuka teks**, tanpa grafik atau visualisasi.

---

## Tim Pengembang

**Kelompok 7B**

| Nama | NIM |
| --- | --- |
| Stefan Virgo Zalukhu | 2610932037 |
| Muhammad Rifat Naufal | 2610933007 |
| Rafa Amalia Yurinov | 2610932005 |
| M. Dafa Al Saban | 2610932001 |

**Asisten Pembimbing:** Faiza Mumtaz & Intan Permata Mustika

**Dosen Pengampu:** Dr. Eng. Ardhian Agung Yulianto

Laboratorium Sistem Informasi dan Keputusan, Departemen Teknik Industri, Fakultas Teknik, Universitas Andalas, 2026.

## Referensi

Heilmeier, A., Graf, M., Betz, J., & Lienkamp, M. (2020). Application of Monte Carlo Methods to Consider Probabilistic Effects in a Race Simulation for Circuit Motorsport. *Applied Sciences*, 10(12), 4229. https://doi.org/10.3390/app10124229
