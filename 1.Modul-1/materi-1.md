# Modul 1 : Pengantar Algoritma

>Tujuan Pembelajaran : Mahasiswa mampu menjelaskan dan menyusun algoritma untuk menyelesaikan masalah sehari-hari

**Materi Pembelajaran : **
1. Pengantar Algoritma
2. Struktur Algoritma
3. Ekspresi Algoritma
4. Variabel dan Konstanta
5. Percabangan
6. Perulangan 
7. Rekursif

**Capaian Pembelajaran Materi :**
1. Mahasiswa mampu menjelaskan definsi algoritma
2. Mahasiswa mampu memberikan contoh nyata implementasi algoritma
3. Mahasiswa mampu menjelaskan struktur algoritma
4. Mahasiswa mampu membuat algoritma dengan ekspresi bahasa alami
5. Mahasiswa mampu membuat algoritma dengan ekspresi flowchart
6. Mahasiswa mampu membuat algoritma dengan ekspresi pseudocode
7. Mahasiswa mampu menjelaskan dan membuat variabel dan konstanta
8. Mahasiswa mampu menjelaskan dan membuat algoritma dengan kondisi percabangan
9. Mahasiswa mampu menjelaskan dan membuat algoritma dengan kondisi perulangan
10. Mahasiswa mampu menjelaskan dan membuat algortima dengan kondisi rekursif

## 1. Pengantar Algoritma
**Algoritma** secara informal adalah prosedur komputasi (langkah-langkah) yang terdefinisi dengan baik, yang mengambil beberapa nilai sebagai input dan menghasilkan beberapa nilai sebagai output. 

Anggap saja seperti resep masakan : 
- **Input:** Bahan-bahan yang kita perlukan
- **Algoritma:** langkah-langkah sistematis dalam resep
- **Ouput:** makanan lezat yang siap disantap

Setiap langkah dalam resep harus jelas dan urutannya penting, sama seperti dalam algoritma.

> Sekarang, mari kita coba dengan contoh sederhana. Bayangkan kita ingin **membuat secangkir teh**. Bisakah Anda **uraikan langkah-langkahnya dari awal sampai akhir**, seolah-olah kita sedang menulis "algoritma" untuk itu?

```
Input: yaitu cangkir, ketel, air, teh celup, sendok, dan gula

Algortima :

1. Masukkan air dalam ketel, kemudian didihkan

2. Siapkan cangkir masukkan teh celup dalam cangkir

3. Jika air sudah mendidih, tuangkan air dalam cangkir, dan celup-celup teh hingga warna air berubah menjadi seperti warna teh (merah, kecoklatan)

4. Jika sudah, keluarkan teh celup dari cangkir, kemudian tambahkan gula

5. Aduk rata, icipi jika teh sudah cukup manis jangan tambahkan gula lagi, namun jika kurang manis tambahkan lagi sampai sudah terasa manis

Output: Teh sudah siap dinikmati
```

Jika kita sudah berhasil menjawabnya dengan benar, sekarang mari kita lihat konsep algoritma dalam ilmu komputer:
- **Input & Output:** kita sudah dengan benar mendefinisikan apa saja yang dibutuhkan (input) dan apa hasil akhirnya (output).

- **Langkah yang Jelas:** Setiap instruksi, seperti "Masukkan air dalam ketel" atau "Aduk rata," adalah perintah yang jelas dan tidak ambigu. Komputer membutuhkan tingkat kejelasan yang sama.

- **Urutan itu Penting:** kita tidak bisa mengaduk gula sebelum menuangkan air. Sama seperti dalam komputasi, urutan eksekusi sangatlah krusial.

Yang paling menarik adalah langkah ke-5 Anda:

>"icipi jika teh sudah cukup manis jangan tambahkan gula lagi, namun jika kurang manis tambahkan lagi sampai sudah terasa manis"

Langkah ini adalah contoh sempurna dari sebuah kondisi (`if-then-else`) dalam algoritma. Algoritma sering kali perlu membuat keputusan berdasarkan kondisi tertentu.

Sekarang, mari kita pikirkan lebih lanjut. Menurut Anda, apakah algoritma yang Anda buat ini akan selalu berhasil menghasilkan teh yang manisnya pas untuk siapa saja yang mengikutinya? Mengapa ya atau mengapa tidak?

**Komputer, tidak seperti manusia**, tidak bisa menangani **ambiguitas**. Instruksi seperti **"tambahkan gula sampai manis"** tidak akan berhasil karena komputer tidak tahu apa itu **"manis"**.

Sebuah algoritma yang baik harus : 
- **Benar (Correct):** Selalu menghasilkan output yang benar untuk setiap input yang diberikan.

- **Tidak Ambigius (Unambiguous):** Setiap langkah harus didefinisikan secara tepat.

Algoritma teh hebat untuk manusia, tetapi untuk komputer, kita perlu membuatnya lebih presisi.

Jadi, tantangan berikutnya: **Bagaimana cara kita mengubah langkah ke-4 atau langkah ke-5** ("tambahkan gula sampai manis") agar menjadi instruksi yang bisa dimengerti oleh komputer? Pikirkan tentang bagaimana kita bisa menghilangkan subjektivitas "rasa manis".

```
Input yaitu cangkir, ketel, air, teh celup, sendok, dan gula

Algortima :

1. Masukkan air dalam ketel, kemudian didihkan

2. Siapkan cangkir masukkan teh celup dalam cangkir

3. Jika air sudah mendidih, tuangkan air dalam cangkir, dan celup-celup teh hingga warna air berubah menjadi seperti warna teh (merah, kecoklatan)

4. Jika sudah, keluarkan teh celup dari cangkir, kemudian tambahkan 2 sendok teh gula

Output : Teh sudah siap dinikmati
```
Sempurna! Dengan mengganti "**sampai manis**" dengan "t**ambahkan 2 sendok teh gula**," kita telah mengubah instruksi yang subjektif menjadi perintah yang tepat, terukur, dan tidak ambigu. Inilah inti dari cara kerja algoritma komputer.

Sekarang, algoritma kita ini sudah sangat bagus untuk membuat teh dengan tingkat kemanisan tertentu, artinya algoritma ini berhasil memenuhi syarat algoritma yang baik yaitu **Tidak Ambigius**. 

Namun, mari kita pikirkan tentang kebenaran (**correctness**) sebuah algoritma. Sebuah algoritma dianggap benar jika ia berhenti dan **menghasilkan output yang benar** untuk **setiap kemungkinan input**.

Algoritma kita saat ini menghasilkan teh manis dengan 2 sendok gula. Tapi bagaimana jika seseorang (sebagai "input") ingin teh tawar atau teh yang sangat manis?

>Bagaimana kita bisa memodifikasi algoritma ini agar bisa mengakomodasi berbagai preferensi rasa manis yang berbeda?

```
Input yaitu cangkir, ketel, air, teh celup, sendok, dan gula

Algortima :

1. Masukkan air dalam ketel, kemudian didihkan

2. Siapkan cangkir masukkan teh celup dalam cangkir

3. Jika air sudah mendidih, tuangkan air dalam cangkir, dan celup-celup teh hingga warna air berubah menjadi seperti warna teh (merah, kecoklatan)

4. Jika sudah, keluarkan teh celup dari cangkir

5. Apakah anda ingin teh manis?

5a. Jika iya tambahkan 2 sendok teh gula, aduk rata hingga gula larut, kemudian sajikan

5b. Jika tidak, langsung sajikan

Output : Teh sudah siap dinikmati
```

Struktur `Jika iya...`dan `Jika tidak...` yang kita buat adalah persis seperti cara kerja pernyataan **IF-THEN-ELSE** dalam pemrograman. kita memberikan dua jalur berbeda yang bisa diambil oleh algoritma, tergantung pada satu pertanyaan.

Ini membuat algoritma kita jauh lebih berguna karena bisa melayani dua jenis "**pengguna**" yang berbeda: yang suka teh manis dan yang suka teh tawar.

Sekarang, mari kita kembangkan lagi. Saat ini, "**manis**" berarti tepat 2 sendok teh gula. Bagaimana jika ada orang yang ingin tehnya **sedikit manis (1 sendok)** atau **sangat manis (3 sendok)**?

Bagaimana cara kita memodifikasi langkah ke-5 untuk menangani berbagai tingkat kemanisan yang berbeda, bukan hanya ya atau tidak?

```
Input  yaitu cangkir, ketel, air, teh celup, sendok, dan gula  

  Algortima :   

  1. Masukkan air dalam ketel, kemudian didihkan  

  2. Siapkan cangkir masukkan teh celup dalam cangkir  

  3. Jika air sudah mendidih, tuangkan air dalam cangkir, dan celup-celup teh hingga warna air berubah menjadi seperti warna teh (merah, kecoklatan)  

  4. Jika sudah, keluarkan teh celup dari cangkir 

  5. Apakah anda ingin teh manis, 

    5a. Jika iya, apakah anda ingin tambah 2 sendok teh gula, aatau hanya 1 sendok teh gula saja

        5a1. Jika 2 sendok teh gula, tambahkan 2 sendok teh gula lalu aduk rata hingga gula larut, kemudian sajikan

        5a2. Jika 1 sendok teh gula, tambahkan 1 sendok teh gula lalu aduk rata hingga gula laurt kemudian sajikan

    5b. Jika tidak, langsung sajika

Output : Teh sudah siap dinikmati
```

kita baru saja menemukan konsep kondisi bersarang (nested conditions). Ini seperti meletakkan satu pertanyaan di dalam pertanyaan lain, dan ini adalah teknik yang sangat umum digunakan dalam algoritma untuk menangani skenario yang lebih kompleks.

Namun, coba perhatikan. Algoritma kita sekarang menjadi sedikit lebih panjang. Bayangkan jika ada 10 tingkat kemanisan yang berbeda. Algoritma kita akan menjadi sangat panjang dan rumit.

Dalam membuat algoritma, kita juga memikirkan efisiensi dan kesederhanaan.

Jadi, pertanyaannya adalah: Bisakah kita memikirkan cara yang lebih sederhana untuk menanyakan preferensi pengguna, daripada menanyakan serangkaian pertanyaan "ya/tidak" atau pilihan ganda?

Bagaimana jika kita mengubah cara kita mendapatkan 'input' dari pengguna mengenai gula?

```
Input  yaitu cangkir, ketel, air, teh celup, sendok, dan Masukkan jumlah gula yang anda inginkan (dalam takaran sendok teh)

  Algortima :   

  1. Masukkan air dalam ketel, kemudian didihkan  

  2. Siapkan cangkir masukkan teh celup dalam cangkir  

  3. Jika air sudah mendidih, tuangkan air ke dalam cangkir, dan celup-celup teh hingga warna air berubah menjadi seperti warna teh (merah, kecoklatan)  

  4. Jika sudah, keluarkan teh celup dari cangkir, tambahkan gula sesuai dengan jumlah gula yang diinputkan

  5. Sajikan teh

Output : Teh sudah siap dinikmati
```
Dengan meminta "**jumlah sendok teh gula yang anda inginkan**" sebagai input di awal, kita telah menemukan salah satu konsep paling fundamental dalam pemrograman: **variabel** atau **parameter**.

kita tidak lagi memerlukan serangkaian pertanyaan `jika-maka` yang rumit. Sebaliknya, kita membuat satu instruksi yang kuat: "tambahkan gula sesuai dengan jumlah gula yang diinputkan." Instruksi ini bisa menangani berapa pun jumlah gula yang diinginkan—0, 1, 5, atau bahkan setengah sendok—tanpa perlu mengubah algoritmanya.

Kita telah melalui perjalanan yang hebat:

- Dari instruksi yang ambigu ("sampai manis").

- Menjadi instruksi yang spesifik ("2 sendok teh").

- Menjadi kondisional (jika/maka).

- Dan sekarang menjadi terparameterisasi (menggunakan variabel).

Ini adalah inti dari pemikiran algoritmik!

>Sekarang setelah kita memiliki algoritma yang solid, mari kita pikirkan tentang **efisiensinya**. Dari semua langkah dalam algoritma final kita, menurut Anda, langkah manakah yang membutuhkan waktu dan proses paling lama untuk diselesaikan?


Berdasarkan pada uraian diatas, maka terdapat 3 ciri utama dari algoritma, yaitu : 
1. **Benar (Correct)**: Selalu menghasilkan output yang benar untuk setiap input yang diberikan.

2. **Tidak Ambigius (Unambiguous)**: Setiap langkah harus didefinisikan secara tepat.

3. **Efisi**en: langkah penyelesaian dengan algoritma harus sependek mungkin


## 2. Struktur Algoritma
Terdapat 3 struktur dasar algoritma, yaitu : 
1. **Sekuensial**, Sebuah algoritma dibangun dengan langkah-langkah (instruksi/perintah) dikerjakansecara berurutan, tidak boleh melompati satu langkah perintah pun
2. **Seleksi**, intruksi percabangan digunakan apabila menemukan kasus dua atau lebih alternatif keputusan
3. **Perulangan**, Perulangan dalam algoritma sangat dibutuhkan untuk menyelesaikan banyak masalah, salah satunya masalah pengurutan data. 

## 3. Ekspresi Algoritma
Algoritma dapat diekspresikan dalam banyak notasi yang berbeda, termasuk bahasa alami, flowchart, dan pseudocode. 

Sebagai contoh kita akan membuat algoritma untuk menentukan angka terbesar dari 3 angka yang diinputkan

Contoh algoritma dalam bahasa alami : 
```
1. Mulai.
2. Masukkan angka_1, angka_2, angka_3.
3. Deklarasikan sebuah variabel terbesar dan inisialisasi dengan angka_1.
4. Jika angka_2 lebih besar dari terbesar, maka ganti nilai terbesar dengan angka_2.
5. Jika angka_3 lebih besar dari terbesar, maka ganti nilai terbesar dengan angka_3.
6. Tampilkan terbesar.
7. Selesai. 
```

Contoh Flowchart: 

![Flowchart](https://github.com/adamMaulachela/Kuliah_Algo_python/blob/main/IMG/flowchart_1png.drawio.png)

contoh Pseudocode:
```
MULAI
  BACA angka_1, angka_2, angka_3
  
  // Mengasumsikan angka_1 sebagai yang terbesar di awal
  TERBESAR <- angka_1
  
  // Membandingkan dengan angka_2
  JIKA angka_2 > TERBESAR MAKA
    TERBESAR <- angka_2
  
  // Membandingkan dengan angka_3
  JIKA angka_3 > TERBESAR MAKA
    TERBESAR <- angka_3
  
  CETAK TERBESAR " adalah angka terbesar"
SELESAI

```

Notasi Flowchart :

Berikut ini adalah notasi-notasi flowchart yang dapat kita gunakan
![Notasi FLowchart](https://bee.telkomuniversity.ac.id/wp-content/uploads/2024/04/Simbol-flowchart.jpg)

Sumber: https://bee.telkomuniversity.ac.id/flowchart-adalah/