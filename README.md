# Program Animasi Terminal Python (ASCII Wave + Text Input)

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8+-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Terminal-lightgrey)

Program ini adalah aplikasi animasi berbasis terminal yang dibuat menggunakan Python.
Pengguna dapat menampilkan animasi gelombang ASCII serta animasi teks berdasarkan input pengguna.
Program mendukung pengaturan kecepatan animasi dan pencatatan log aktivitas.

Program berjalan langsung di terminal dan memanfaatkan library `colorama` untuk efek warna serta sistem logging untuk mencatat aktivitas pengguna.

---

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
2. Buat dan aktifkan virtual environment:

Windows:

3. Install dependency:
pip install colorama

## Cara Menjalankan Program

Jalankan file utama:
python spike.py



## Cara Kerja Program

1. Program meminta teks dari pengguna.
2. Menampilkan teks tersebut secara bertahap.
3. Memulai animasi wave menggunakan karakter "-".
4. Mencatat setiap aktivitas ke dalam file log.
5. Berjalan terus sampai dihentikan secara manual.






## Demo Animasi

Berikut contoh hasil animasi 

<img width="1431" height="492" alt="image" src="https://github.com/user-attachments/assets/2b439dcd-75d9-4069-a5e2-e216897e04af" />



## Lisensi

Proyek ini bebas digunakan, dimodifikasi, dan dikembangkan sesuai kebutuhan.


