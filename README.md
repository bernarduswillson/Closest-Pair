# Tugas kecil 2 Strategi Algoritma


## Mencari Pasangan Titik Terdekat dengan Algoritma Divide and Conquer


## Deskripsi Permasalahan

Permainan kartu 24 adalah permainan kartu aritmatika dengan tujuan mencari cara untuk mengubah 4 buah angka random sehingga mendapatkan hasil akhir sejumlah 24 Permainan ini menarik cukup banyak peminat dikarenakan dapat meningkatkan kemampuan berhitung serta mengasah otak agar dapat berpikir dengan cepat dan akurat. Permainan Kartu 24 biasa dimainkan dengan menggunakan kartu remi. Kartu remi terdiri dari 52 kartu yang terbagi menjadi empat suit (sekop, hati, keriting, dan wajik) yang masing-masing terdiri dari 13 kartu (As, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, dan King). Yang perlu diperhatikan hanyalah nilai kartu yang didapat (As, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, dan King). As bernilai 1, Jack bernilai 11, Queen bernilai 12, King bernilai 13, sedangkan kartu bilangan memiliki nilai dari bilangan itu sendiri. Pada awal permainan moderator atau salah satu pemain mengambil 4 kartu dari dek yang sudah dikocok secara random. Permainan berakhir ketika pemain berhasil menemukan solusi untuk membuat kumpulan nilainya menjadi 24. Pengubahan nilai tersebut dapat dilakukan menggunakan operasi dasar matematika penjumlahan (+), pengurangan (-), perkalian (×), divisi (/) dan tanda kurung ( () ). Tiap kartu harus digunakan tepat sekali dan urutan penggunaannya bebas. 
(Paragraf di atas dikutip dari sini: https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2015-2016/Makalah-2016/MakalahStima-2016-038.pdf).


## Bahasa dan Algoritma yang digunakan

Pada projek ini, digunakan suatu algoritma menggunakan Bahasa *C++* dan dengan pendekatan *brute force*, untuk mencari solusi dari permainan kartu 24.


## Struktur Program

```
│ .vscode
├─── bin
│       │ main.exe
│
├─── doc
│       │ Tucil1_K3_13521021_Bernardus Willson.pdf
        | Tucil1-Stima-2023.pdf
│
├─── src
│       │ algorithm
                | numPermutation.cpp
                | operators.cpp
│       │ others
                | inputCard.cpp
                | saveDat.cpp
                | splashScreen.cpp
                | splashScreen.txt
│       │ main.cpp
│
├─── test
        │ file .txt hasil penyimpanan program
```


## Menjalankan Program

Untuk menjalankan program, pada *root directory*, jalankan run.bat (pada *windows*):
```
./run.bat
```
Jika Program tidak dapat dijalankan dengan error message "Permission denied", hapus file main.exe di folder bin. Lalu coba jalankan ulang program.

Untuk teknis penggunaan program saat dijalankan, terdapat Menu HELP yang berisi cara menggunakan Program seperti berikut:
```
<> Contoh masukan untuk Menu nomor 1:
A 2 3 4
10 J Q K

<> Menu nomor 2 hanya mengeluarkan kartu-kartu random.

<> Setelah mendapatkan Solusi dan Jumlah Solusinya, Anda dapat menyimpan data tersebut ke dalam file .txt.
```


## Libraries Used

1. iostream (c++)
2. string (c++)
3. chrono (c++)
4. fstream (c++)
5. cstdlib (c++)
6. ctime (c++)


## Author

Bernardus Willson, 13521021.