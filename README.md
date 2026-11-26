# Latar Belakang

  Dalam Teknik Industri, lamanya suatu pekerjaan diukur dengan Pengukuran Waktu Kerja (Time Study), yang dipelajari pada mata kuliah Studi Gerak dan Waktu. Metode ini cocok untuk pekerjaan yang berulang, singkat, dan berpola sama, lalu hasilnya dinilai dari seberapa stabil waktunya. Pit stop pada balap Formula 1 memenuhi ciri tersebut: dilakukan berulang kali, hanya memakan puluhan detik, langkah kerjanya sama setiap kali, dan selisih yang kecil saja dapat menggeser posisi pembalap.

Pada teori aslinya, Time Study berlanjut sampai penghitungan waktu normal dan waktu baku dengan tambahan kelonggaran. Pada proyek ini, metodenya disederhanakan menjadi lima tahap:

Tahap	Kegiatan	Implementasi pada program
1	Menentukan pekerjaan yang diukur	Pit stop pada satu balapan
2	Mencatat waktu	Data durasi sudah tersedia pada berkas CSV
3	Menghitung statistik waktu	Rata-rata, minimum, maksimum, standar deviasi
4	Membandingkan dengan standar	Klasifikasi berdasarkan nilai ambang batas
5	Mengevaluasi hasil	Rekapitulasi kategori dan rekomendasi konsistensi proses

Secara keseluruhan, struktur dan penanganan error-nya sudah rapi. Jika Anda mau, kirim sisa kodenya dan saya bisa bantu melengkapi validasi_baris atau bagian klasifikasi dan laporannya.

# Tujuan Program

Membaca berkas CSV pit stop dan memeriksa kelengkapan serta kewajaran isinya.
Menghitung rata-rata, nilai terkecil, nilai terbesar, dan standar deviasi durasi pit stop.
Menggolongkan setiap pit stop ke dalam kategori Sangat Efisien, Normal, atau Perlu Evaluasi berdasarkan nilai ambang.
Menampilkan rekapitulasi jumlah dan persentase tiap kategori, baik untuk seluruh data maupun untuk pembalap atau nomor pemberhentian tertentu.
Memberikan rekomendasi sederhana untuk mengevaluasi konsistensi proses pit stop.

Pengguna yang dituju: mahasiswa Teknik Industri yang mempelajari analisis waktu kerja, pengamat atau analis data olahraga otomotif, dan asisten praktikum yang menilai pengolahan data pada program.

# Dataset

Keterangan	Isi
Berkas	pit_stops_race1054.csv
Sumber	Dataset Formula 1 World Championship di Kaggle, disaring untuk satu balapan
Balapan	Portuguese Grand Prix 2021 (raceId = 1054)
Jumlah data	60 pit stop dari 19 pembalap
Rentang durasi	21.275 ms sampai 28.639 ms (sekitar 21 sampai 29 detik)
Jumlah pemberhentian	Stop 1: 19, Stop 2: 19, Stop 3: 19, Stop 4: 3

Kolom pada berkas:

Kolom	Keterangan	Wajib oleh program
raceId	ID balapan	-
year	Tahun balapan	-
race_name	Nama balapan	-
driverId	ID pembalap (mis. 1 = Hamilton, 830 = Verstappen, 822 = Bottas)	Ya
driver_code	Kode tiga huruf pembalap (mis. HAM)	Ya
driver_name	Nama pembalap	Ya
stop	Nomor pemberhentian pembalap pada balapan tersebut	Ya
lap	Putaran saat pembalap masuk pit	Ya
time	Waktu jam saat pemberhentian	-
duration	Durasi dalam detik	-
milliseconds	Durasi dalam milidetik (dipakai untuk semua perhitungan)	Ya

# Fitur Program

Pembacaan berkas CSV: memuat data dari pit_stops_race1054.csv (default) atau berkas lain yang dipilih pengguna.
Validasi data:
berkas tidak ditemukan, berkas kosong, atau hanya berisi header;
kolom wajib tidak ada;
driverId, stop, lap, atau milliseconds bukan angka;
durasi di luar batas wajar 15.000 sampai 60.000 ms.
Baris valid dan tidak valid dipisahkan, dan alasan setiap baris yang ditolak ditampilkan beserta nomor barisnya.
Penyaringan data: berdasarkan driverId, nomor stop, atau keduanya.
Perhitungan statistik: jumlah data, rata-rata, minimum, maksimum, dan standar deviasi.
Klasifikasi efisiensi: setiap pit stop digolongkan ke tiga kategori berdasarkan nilai ambang.
Rekapitulasi dan rekomendasi: jumlah dan persentase tiap kategori beserta saran evaluasi otomatis.
Pengaturan ambang: nilai ambang dapat diubah lewat menu, dengan validasi (harus angka positif dan ambang "Sangat Efisien" lebih kecil dari ambang "Normal").
Tahan kesalahan: program tetap berjalan bila berkas gagal dimuat, sehingga pengguna dapat memuat ulang lewat menu 1.

Menu program:
Menu Fungsi
1, Muat ulang / ganti berkas CSV
2, Tampilkan semua data pit stop
3, Tampilkan data dengan filter (pembalap / stop)
4, Statistik durasi (seluruh data)
5, Rekapitulasi kategori dan rekomendasi (seluruh data)
6, Rekapitulasi kategori dan rekomendasi (hasil filter)
7, Atur nilai ambang klasifikasi
0, Keluar
