# Program Animasi Terminal Python (ASCII Wave + Text Input)

Program ini adalah aplikasi animasi berbasis terminal yang dibuat menggunakan Python.  
Pengguna dapat menampilkan animasi gelombang ASCII serta animasi teks berdasarkan input pengguna.  
Program mendukung pengaturan kecepatan animasi dan pencatatan log aktivitas.

Program berjalan langsung di terminal dan memanfaatkan library `colorama` untuk efek warna serta sistem logging untuk mencatat aktivitas pengguna.

## Fitur Utama

### 1. Input Teks dari Pengguna
- Pengguna dapat memasukkan teks bebas.
- Program menampilkan teks secara bertahap huruf demi huruf.
- Setiap huruf akan dianimasikan menggunakan karakter "-".

### 2. Animasi ASCII Wave
- Menampilkan efek barisan garis yang memanjang dan memendek.
- Polanya bergerak naik dan turun seperti gelombang.

### 3. Pengaturan Kecepatan Animasi
Pengguna dapat memilih tiga level kecepatan:
- 1 = Lambat  
- 2 = Normal  
- 3 = Cepat  

Kecepatan memengaruhi nilai `time.sleep()` dalam setiap frame animasi.

### 4. Logging Aktivitas
Program otomatis membuat file `log.txt` yang mencatat:
- Input teks dari pengguna
- Kecepatan animasi yang dipilih
- Waktu program digunakan

### 5. Penanganan Interrupt
Program dapat dihentikan dengan aman menggunakan `Ctrl + C` tanpa menampilkan error.

## Instalasi

Pastikan Python versi 3.8 atau lebih baru telah terpasang.

1. Clone repository:
