# Deskripsi
Program Python untuk autentikasi pengguna, membaca data pit stop dari CSV, memvalidasi struktur dan nilai, menampilkan tabel, menghitung statistik deskriptif, memfilter data, serta membandingkan statistik antar pembalap.
# Kebutuhan
Python 3. Modul csv dan os merupakan bagian dari pustaka standar Python sehingga tidak memerlukan instalasi tambahan.
# Berkas
Sediakan file program Python, pit_stops_race1054.csv, dan folder kerja yang dapat ditulisi agar program dapat membuat pengguna.csv.
# Kolom CSV
driverId, driver_code, driver_name, stop, lap, milliseconds. Kolom driverId, stop, lap, dan milliseconds harus dapat dikonversi menjadi angka.
# Menjalankan
Simpan kode dengan nama misalnya main.py. Letakkan CSV pada direktori kerja yang sama. Jalankan melalui terminal dengan perintah: python main.py.
# Login awal
Jika pengguna.csv belum ada, program membuatnya dan menambahkan akun admin dengan password 123456. Setelah itu pengguna dapat mendaftar akun baru atau login.
# Pendaftaran
Username minimal empat karakter dan tidak boleh mengandung koma menurut pemeriksaan kode. Password harus tepat enam karakter dan seluruhnya angka. Username yang sudah terdaftar ditolak.
# Login
Login menyediakan maksimal tiga percobaan pada satu sesi pemilihan menu login. Jika ketiganya gagal, program menampilkan pesan percobaan habis.
#Validasi CSV
Program memeriksa keberadaan header dan enam kolom wajib. Baris kosong dilewati. Baris yang gagal mengonversi nilai angka ditolak. Durasi di luar rentang 15.000–60.000 ms juga ditolak.
# Menu utama
1 menampilkan tabel pit stop; 2 menampilkan analisis statistika; 3 membandingkan statistik antar pembalap; 4 keluar.
# Filter
Menu analisis dan perbandingan dapat menggunakan semua data atau data filter. Filter tersedia berdasarkan driverId atau nomor stop. Untuk mode perbandingan, minimal dua driverId berbeda harus ditemukan dalam hasil filter.
