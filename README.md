# Latar Belakang

  Program Python ini membaca data pit stop dari berkas CSV, memeriksa struktur dan isi data, menampilkan catatan pit stop, melakukan penyaringan, menghitung statistik deskriptif, serta membandingkan statistik antar pembalap.
# Tujuan penggunaan
membantu pengguna menelusuri data pit stop Grand Prix Portugal 2021 (raceId 1054) dan memperoleh ringkasan numerik dari durasi pit stop. Program bersifat deskriptif; hasilnya hanya menggambarkan data yang dimasukkan dan bukan prediksi atau generalisasi untuk balapan lain.
# Kebutuhan 
Python 3. Pustaka csv dan statistics sudah termasuk dalam pustaka standar Python sehingga tidak perlu instalasi tambahan.
# Berkas yang diperlukan
file program Python dan pit_stops_race1054.csv. Jika CSV tidak ditemukan pada lokasi kerja, program mencoba membuat berkas contoh berisi 24 baris demonstrasi. Data contoh bukan pengganti dataset asli 60 baris.
# Kolom wajib CSV
driverId, driver_code, driver_name, stop, lap, dan milliseconds. Kolom milliseconds berisi durasi dalam milidetik. Program mengubahnya menjadi detik dengan membagi nilai milidetik dengan 1000.

# Menu program
## 1 = memuat ulang atau mengganti file CSV
## 2 = menampilkan seluruh data pit stop
## 3 = menampilkan data berdasarkan filter 
## 4 = menganalisis statistik seluruh data 
## 5 = menganalisis statistik dari hasil filter
## 6 = membandingkan statistik antar pembalap
## 0 = keluar dari program.
# Pilihan filter


pengguna dapat menyaring berdasarkan driverId, nomor pit stop (stop), atau gabungan keduanya. Nilai ID dan nomor pit stop harus berupa angka. Jika format masukan salah atau tidak ada data yang cocok, program menampilkan pesan dan tidak melanjutkan analisis filter tersebut.
# Validasi data
program memeriksa keberadaan header, kelengkapan enam kolom wajib, serta kemampuan mengonversi driverId, stop, lap, dan milliseconds menjadi angka. Program juga menerapkan rentang pemeriksaan durasi 15.000–60.000 milidetik melalui konstanta BATAS_WAJAR_MIN dan BATAS_WAJAR_MAX. Rentang ini adalah aturan teknis yang tertanam pada kode; jangan menyebutnya sebagai standar universal Formula 1 tanpa sumber akademik atau regulasi yang secara langsung mendukungnya.
# Hasil perhitungan
program menampilkan jumlah pengamatan, mean, median, nilai minimum, maksimum, rentang, varians, standar deviasi, dan koefisien variasi. Durasi ditampilkan dalam detik. Pada kode saat ini, varians dan standar deviasi dihitung sebagai statistik sampel menggunakan statistics.variance() dan statistics.stdev() jika jumlah pengamatan minimal dua; jika hanya satu pengamatan, keduanya diatur menjadi nol.
# Interpretasi keluaran
mean dan median menggambarkan pemusatan data; minimum, maksimum, dan rentang menunjukkan batas serta selisih durasi; standar deviasi dan koefisien variasi menggambarkan penyebaran relatif terhadap rata-rata. Keluaran statistik tidak dengan sendirinya membuktikan penyebab cepat atau lambatnya pit stop.
# Catatan akademik
kode saat ini memberi label variasi relatif rendah jika koefisien variasi <10%, sedang jika <20%, dan tinggi jika ≥20%. Ambang tersebut merupakan aturan klasifikasi dalam implementasi program. Gunakan label itu sebagai kategori ilmiah hanya jika kelompok dapat mencantumkan rujukan yang secara eksplisit mendukung batas tersebut. Jika jurnal yang digunakan tidak menetapkan ambang itu, laporkan nilai koefisien variasinya secara numerik tanpa menyimpulkan kategori baku.
# Batasan
program tidak melakukan uji hipotesis, pemodelan prediktif, atau penilaian sebab-akibat. Ketepatan hasil bergantung pada kelengkapan, konsistensi, dan kebenaran data CSV yang digunakan. Dataset yang dijelaskan dalam laporan merupakan 60 catatan pit stop dari 19 pembalap pada Grand Prix Portugal 2021.
