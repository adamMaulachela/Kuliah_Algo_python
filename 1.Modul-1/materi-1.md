# Modul 1 : Pengantar Algoritma

>Tujuan Pembelajaran : Mahasiswa mampu menjelaskan dan menyusun algoritma untuk menyelesaikan masalah sehari-hari

**Materi Pembelajaran :**
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

### Praktikum Percobaan - 1 
Buatlah sebuah algoritma dalam 3 ekspresi (Bahasa alami, flowchart, dan pseudocode) yang dapat menentukan apakah sebuah bilangan adalah bilangan genap atau bilangan ganjil!


## 4. Variabel dan Konstanta dalam Algoritma
Memahami **variabel** dan **konstanta** adalah salah satu langkah pertama yang paling fundamental dalam pemrograman. Bayangkan Anda memiliki dua jenis wadah penyimpanan:

- Sebuah kotak sepatu, yang bisa Anda beri label "Mainan" hari ini, lalu ganti isinya dan beri label baru "Surat" besok. Isinya dan labelnya bisa berubah-ubah.

- Sebuah etalase kaca yang disegel, di mana Anda meletakkan medali kemenangan Anda. Isinya dipajang, tidak untuk diubah-ubah, dan akan selalu menjadi "Medali Juara".

Dalam pemrograman, variabel dan konstanta berfungsi seperti dua wadah ini. Untuk memulai, kita bisa mendalami dari beberapa sudut pandang :

- **Tujuan & Fungsi:** Mengapa kita perlu membedakan antara data yang bisa diubah (variabel) dan yang tidak bisa diubah (konstanta)?

- **Deklarasi & Sintaks:** Bagaimana cara kita "membuat" variabel dan konstanta dalam kode program?

- **Manajemen Memori:** Bagaimana komputer menangani kedua jenis "wadah" ini di dalam memorinya?
---
### 1. Tujuan & Fungsi
> Mengapa kita perlu membedakan antara data yang bisa diubah (variabel) dan yang tidak bisa diubah (konstanta)?

Alasan utamanya ada tiga: **kejelasan**, **keamanan**, dan **kemudahan perawatan**.

**Kejelasan dan Maksud Kode** 

Menggunakan konstanta membuat kode Anda berbicara sendiri. Ketika Anda melihat sebuah nilai yang didefinisikan sebagai konstanta, Anda langsung tahu bahwa nilai ini penting dan tidak seharusnya diubah.

- **Variabel (`score`)**: Nilainya diharapkan berubah. `score = 10`, lalu bisa menjadi `score = 20`.

- **Konstanta (`PI`)**: Nilainya tetap. `PI = 3.14159`. Ini memberitahu programmer lain (dan diri Anda di masa depan) bahwa nilai ini adalah sebuah fakta yang fundamental dalam program ini.

Ini jauh lebih jelas daripada hanya menulis angka `3.14159` di banyak tempat, yang sering disebut "*magic number*".

---

**Keamanan dan Pencegahan Kesalahan**

Konstanta bertindak sebagai jaring pengaman. Komputer akan mencegah Anda secara tidak sengaja mengubah nilai yang telah ditetapkan sebagai konstan.

Jika Anda mendefinisikan `MAX_ATTEMPTS = 3` sebagai konstanta, dan di bagian lain program Anda secara tidak sengaja menulis `MAX_ATTEMPTS = 5`, program akan berhenti dan memberikan pesan kesalahan. Ini membantu menemukan bug lebih awal.

---
**Kemudahan Perawatan**

Bayangkan Anda membuat program untuk sebuah toko online dan menetapkan PPN (Pajak Pertambahan Nilai) sebesar 11%. Jika Anda menulis angka `0.11` di 50 tempat berbeda dalam kode Anda, apa yang terjadi jika pemerintah mengubah tarif PPN menjadi 12%? Anda harus mencari dan mengganti semua 50 angka itu.

Dengan konstanta, Anda cukup mendefinisikannya di satu tempat: `PPN = 0.11`. Jika ada perubahan, Anda hanya perlu mengubah satu baris ini, dan semua perhitungan di seluruh program akan otomatis menggunakan nilai yang baru.

>Dari ketiga alasan tersebut, mari kita fokus pada keamanan. Apa kira-kira masalah yang bisa terjadi jika seorang programmer secara tidak sengaja mengubah nilai Pi di tengah-tengah program yang sedang menghitung luas lingkaran?

---
### 2. Deklarasi & Sintaks:
Cara "membuat" variabel dan konstanta sedikit berbeda tergantung pada bahasa pemrograman yang digunakan, tapi konsepnya sangat mirip. Kita akan gunakan Python sebagai contoh karena sintaksnya sangat mudah dibaca.

**Variabel**
Di Python, Anda membuat variabel hanya dengan memberinya nama dan menggunakan tanda sama dengan (`=`) untuk memberinya nilai.

Anggap saja Anda sedang memberi label pada kotak sepatu dan langsung mengisinya.
```python
# Membuat variabel untuk menyimpan skor pemain
player_score = 100
print(player_score)

# Nilai variabel bisa diubah kapan saja
player_score = 125
print(player_score)
```

Seperti yang Anda lihat, nilai `player_score` bisa diubah dengan mudah.

**Konstanta**
Di Python, tidak ada aturan ketat yang memaksa sebuah nilai menjadi konstan. Sebaliknya, programmer menggunakan sebuah konvensi atau kesepakatan bersama: nama konstanta ditulis dengan **HURUF KAPITAL SEMUA**.

Ini adalah sinyal bagi programmer lain: "Tolong jangan ubah nilai ini!"
```python
# Konstanta untuk kecepatan cahaya (dalam m/s)
SPEED_OF_LIGHT = 299792458

# Konstanta untuk jumlah percobaan login maksimal
MAX_LOGIN_ATTEMPTS = 3
```
Meskipun secara teknis Anda bisa mengubah nilainya, ini dianggap sebagai praktik yang sangat buruk.
>Sekarang giliran Anda. Bayangkan Anda sedang membuat sebuah game sederhana. Jika Anda perlu menyimpan **nama pemain** dan **jumlah nyawa maksimal** (yang selalu 3), bagaimana Anda akan mendeklarasikan keduanya dalam kode?
---

### 3. Manajemen Memori
Mari kita bayangkan memori komputer sebagai sebuah rak besar dengan ribuan kotak surat kecil, di mana setiap kotak memiliki alamat uniknya sendiri (misalnya, alamat 101, 102, 103, dst.).

**Variabel di Memori**

Ketika Anda membuat variabel seperti `nama_pemain = "sinper"`, komputer melakukan ini:

- Mencari satu kotak surat yang kosong (misalnya, di alamat 450).

- Menaruh nilai `"sinper"` ke dalam kotak itu.

- Mencatat di buku catatannya: "Hei, nama `nama_pemain` sekarang menunjuk ke alamat 450."

Jika nanti Anda mengubahnya menjadi `nama_pemain = "avatar"`, komputer hanya akan pergi ke alamat 450 dan mengganti isinya dengan `"avatar"`. Alamatnya tetap sama, isinya yang berubah.

---
**Konstanta di Memori**

Ketika Anda membuat konstanta seperti `MAX_NYAWA = 3`, prosesnya mirip:

1. Komputer mencari kotak kosong (misalnya, di alamat 781).

2. Menaruh nilai `3` ke dalam kotak itu.

3. Mencatat: "Nama `MAX_NYAWA` menunjuk ke alamat 781."

Perbedaan utamanya adalah, komputer juga menambahkan catatan: "**JANGAN PERNAH MENGUBAH ISI KOTAK INI!**" Jika ada bagian dari kode Anda yang mencoba mengubah isi alamat 781, sistem akan menghentikannya dan memberikan peringatan.

Jadi, intinya, variabel adalah penunjuk ke sebuah alamat memori yang isinya boleh diubah, sedangkan konstanta adalah penunjuk ke alamat yang isinya dikunci untuk keamanan.

>Menggunakan analogi kotak surat tadi, apa yang menurut Anda terjadi di memori jika Anda membuat dua variabel berbeda dengan nilai yang sama, misalnya `skor_A = 100` dan `skor_B = 100`? Apakah mereka akan disimpan di dalam satu kotak surat yang sama atau di dua kotak yang berbeda?

### Praktikum Percobaan - 2 : 
Kalkulator Belanja Online 🛒
Tujuan: Anda akan membuat algoritma sederhana untuk menghitung total harga akhir dari sebuah produk yang dibeli di toko online.

Data yang kita miliki:

1. Harga Produk: Harga satu buah produk (misalnya, sebuah buku).

2. Jumlah: Berapa banyak produk yang dibeli.

3. Tarif PPN (Pajak Pertambahan Nilai): Pajak yang ditetapkan pemerintah, yaitu 11%.

Biaya Pengiriman Tetap: Biaya kirim yang selalu sama untuk semua pesanan, yaitu Rp 10.000.

Percobaan 1: Merancang Algoritma
Tugas Anda:
Tuliskan algoritma (dalam bentuk pseudocode dan flowchart ) untuk menghitung total akhir yang harus dibayar.

Saat Anda menulisnya, putuskan dan tunjukkan mana dari data di atas yang sebaiknya menjadi variabel dan mana yang sebaiknya menjadi konstanta.

Silakan coba tuliskan rancangan Anda.

## 5. Percabangan 
Percabangan pada dasarnya adalah cara kita memberikan algoritma kemampuan untuk **membuat keputusan**. Tidak hanya menjalankan serangkaian perintah secara lurus, algoritma bisa memilih jalur mana yang akan diambil berdasarkan kondisi tertentu, sama seperti Anda memilih jalan di persimpangan.

Untuk memulainya, berikut dasar pengetahuan yang harus kita pelajari terlebih dahulu :

1. Struktur `IF-ELSE`: Bentuk percabangan paling dasar (jika A benar, lakukan ini; jika tidak, lakukan itu).
   
2. Struktur `ELSE-IF`: Cara menangani lebih dari dua kemungkinan pilihan.

3. Percabangan Bersarang: Bagaimana jika ada keputusan di dalam keputusan?

---
### 1. Struktur `IF-ELSE` (Jika - Maka)
Anggap saja Anda akan pergi keluar rumah dan melihat ke jendela. Anda membuat keputusan sederhana:

**JIKA** hari ini hujan, **MAKA** saya akan bawa payung.

**LAIN KALI** (jika tidak hujan), **MAKA** saya akan pakai kacamata hitam.

Itulah inti dari `IF-ELSE`. Anda memberikan algoritma sebuah kondisi (apakah hari hujan?) dan dua pilihan aksi, satu untuk jika kondisi itu **benar**, dan satu lagi untuk jika kondisi itu **salah**. Algoritma hanya bisa memilih salah satu, tidak pernah keduanya.

Struktur dasarnya terlihat seperti ini:
```
JIKA (sebuah kondisi terpenuhi) MAKA
  Lakukan aksi ini
LAIN KALI
  Lakukan aksi yang lain ini
```
Sekarang, mari kita terapkan ini pada sebuah contoh. Bayangkan kita ingin memeriksa apakah seorang siswa lulus atau tidak, dengan syarat kelulusan adalah nilai di atas 70.

Bagaimana Anda akan mengisi bagian `[kondisi]`, `[aksi jika benar]`, dan `[aksi jika salah]` dalam algoritma di bawah ini?

```
JIKA ([kondisi]) MAKA
  Cetak "[aksi jika benar]"
LAIN KALI
  Cetak "[aksi jika salah]"
```
---
### 2. Struktur `ELSE-IF` 
`ELSE-IF` adalah cara kita untuk "merantai" beberapa pertanyaan. Ini sangat berguna ketika Anda memiliki lebih dari dua kemungkinan hasil.

Strukturnya bekerja seperti ini:

Algoritma akan memeriksa `IF` yang pertama. Jika kondisinya benar, ia akan melakukan aksinya dan mengabaikan sisanya.

Jika `IF` pertama salah, ia akan pindah ke `ELSE IF` berikutnya dan memeriksa kondisinya.

Proses ini berlanjut sampai salah satu kondisi terpenuhi. Jika tidak ada satu pun kondisi yang terpenuhi, ia akan menjalankan blok `ELSE` terakhir sebagai pilihan "default".

Struktur dasarnya:
```
JIKA (kondisi A) MAKA
  Lakukan aksi untuk A
LAIN JIKA (kondisi B) MAKA
  Lakukan aksi untuk B
LAIN KALI
  Lakukan aksi "default"
```

Sekarang, mari kita gunakan struktur ini untuk skenario penilaian yang tadi:

- Nilai di atas 80: **Lulus dengan Pujian**
- Nilai antara 60 dan 80: **Lulus**
- Nilai di bawah 60: **Gagal**

Coba Anda lengkapi algoritma berikut menggunakan logika `ELSE-IF`.
```
JIKA (nilai > 80) MAKA
  Cetak "Lulus dengan Pujian"
LAIN JIKA ([kondisi kedua]) MAKA
  Cetak "[aksi kedua]"
LAIN KALI
  Cetak "[aksi default]"
```
---
### 3. Percabangan Bersarang (NESTED-IF)
Sekarang, sesuai permintaan Anda, mari kita lihat **percabangan bersarang** (nested branching).

Ini hanyalah ide untuk meletakkan satu struktur `IF-ELSE` di dalam struktur `IF-ELSE` yang lain. Anggap saja seperti sebuah keputusan yang mengarah ke keputusan berikutnya.

Skenario Baru:
Bayangkan ada aturan tambahan. Jika seorang siswa lulus (nilai >= 60), kita perlu memeriksa apakah kehadirannya 100% untuk memberinya bonus "Bintang Emas".

Ini menciptakan dua level keputusan:

1. **Level 1**: Apakah siswa lulus atau gagal?
2. **Level 2**: (**hanya jika lulus**): Apakah kehadirannya sempurna?

Bagaimana Anda akan mencoba menyusun algoritma ini menggunakan `IF` di dalam `IF`? 

```
JIKA (nilai >= 60) MAKA
  // Jika lulus, kita masuk ke sini dan membuat keputusan baru.
  JIKA (kehadiran == 100%) MAKA
    Cetak "Lulus dengan Bintang Emas"
  LAIN KALI
    Cetak "Lulus"
LAIN KALI
  // Jika tidak lulus dari awal, langsung ke sini.
  Cetak "Gagal"
```

Sekarang Anda sudah melihat bagaimana kita bisa meletakkan satu keputusan di dalam keputusan lainnya untuk menangani logika yang lebih kompleks.

Kita telah berhasil membahas tiga struktur percabangan utama:

1. `IF-ELSE`: Untuk situasi dengan dua kemungkinan (ya/tidak, lulus/gagal).
2. `ELSE-IF`: Untuk menangani banyak kemungkinan yang saling eksklusif (gagal, lulus, lulus dengan pujian).
3. **Percabangan Bersarang**: Untuk menangani keputusan yang bergantung pada hasil keputusan sebelumnya.

Anda sudah membangun fondasi yang sangat kuat dalam logika algoritmik.

### Praktikum Percobaan - 3
**Skenario: Penentuan Kategori Film**
**Tujuan**: Anda akan membuat algoritma untuk menentukan kategori penonton sebuah film berdasarkan rating usia.

**Aturan Kategori**:

- Jika usia penonton **17 tahun ke atas**, kategori filmnya adalah "**Dewasa**".
- Jika usia penonton antara **13 hingga 16 tahun**, kategori filmnya adalah "**Remaja**".
- Jika usia penonton **di bawah 13 tahun**, kategori filmnya adalah "**Anak-anak**".

**Percobaan 1: Merancang Algoritma
Tugas Anda:**

Tuliskan algoritma (dalam bentuk pseudocode atau langkah-langkah seperti yang kita lakukan sebelumnya) yang menerima input `usia` dan kemudian mencetak kategori film yang sesuai.

Gunakan struktur `IF`, `ELSE-IF`, dan `ELSE` untuk menyelesaikan masalah ini. Silakan coba tuliskan rancangan Anda.

## 6. Perulangan (loops)
Bayangkan Anda harus menyikat gigi. Anda tidak berpikir, "gerakkan sikat ke kanan, lalu ke kiri, lalu ke kanan, lalu ke kiri..." sebanyak 50 kali. Anda hanya berpikir, "**Lakukan** gerakan menyikat gigi **sampai** semua gigi bersih."

Itulah ide utama dari perulangan. Kita memberikan komputer satu set instruksi dan menyuruhnya untuk mengulanginya sampai kondisi tertentu terpenuhi. Ini membuat kode kita jauh lebih pendek dan efisien.

Ada dua jenis perulangan utama yang sering digunakan:

1. **Perulangan** `for`: Digunakan ketika kita tahu persis berapa kali kita ingin mengulang suatu tugas (misalnya, ulangi sebanyak 10 kali).
2. **Perulangan** `while`: Digunakan ketika kita ingin mengulangi tugas selama suatu kondisi masih benar (misalnya, ulangi terus selama masih ada kue di dalam toples).

### 1. Perulangan `for`
Mari kita mulai dengan perulangan `for`.

Gunakan perulangan `for` ketika Anda sudah tahu persis berapa kali sebuah tugas harus diulang. Anggap saja Anda ingin melakukan 10 kali *push-up*. Anda sudah menetapkan jumlahnya dari awal.

Struktur dasarnya seperti ini:
```
ULANGI untuk setiap [item] dalam [sebuah urutan]:
  Lakukan aksi ini
```

Sebagai contoh, jika kita ingin menyapa "Halo!" sebanyak 3 kali, algoritmanya akan terlihat seperti ini:

```ULANGI sebanyak 3 kali:
  Cetak "Halo!" 
```

**Hasilnya:**

Halo!

Halo!

Halo!

> Sekarang giliran Anda. Bayangkan Anda ingin mencetak angka dari 1 sampai 5. Bagaimana Anda akan menuliskan algoritma perulangan `for` untuk tugas tersebut?

```
ULANGI UNTUK i DARI 1 SAMPAI 5:
  Cetak i
```

### 2. Perulangan `while`
Gunakan perulangan `while` ketika Anda ingin sebuah tugas diulang selama (while) suatu kondisi masih terpenuhi. Anda tidak harus tahu berapa kali perulangan akan terjadi, yang penting hanya kondisinya.

Bayangkan Anda sedang minum air dari botol. Anda akan terus minum tegukan demi tegukan selama botolnya belum kosong.

Struktur dasarnya seperti ini:
```
SELAMA (kondisi ini benar):
  Lakukan aksi ini
  // Penting: Lakukan sesuatu yang bisa membuat kondisi menjadi salah
```
Sekarang, mari kita buat ulang algoritma untuk mencetak angka 1 sampai 5, tapi kali ini menggunakan `while`. Struktur ini akan sangat mirip dengan ide awal Anda.
```
// 1. Kita siapkan penghitung di awal
i = 1

// 2. Tetapkan kondisi untuk terus berjalan
SELAMA (i <= 5):
  // 3. Lakukan aksi
  Cetak i
  
  // 4. Naikkan penghitung secara manual
  i = i + 1
```

> Melihat struktur ini, apa kira-kira yang bisa terjadi jika kita lupa menyertakan baris terakhir (i = i + 1)?

Jika kita lupa baris `i = i + 1`, kita akan menciptakan sesuatu yang disebut perulangan tak terbatas (infinite loop).

Berikut adalah apa yang akan terjadi:

1. Nilai `i` akan dimulai dari 1.
2. Komputer akan memeriksa, "Apakah `i <= 5`?" Tentu saja, karena 1 lebih kecil dari 5.
3. Komputer akan mencetak `1`.
4. Perulangan selesai, dan komputer kembali ke atas untuk memeriksa kondisi lagi.
5. Nilai `i` masih tetap 1 karena tidak pernah diubah.
6. Komputer bertanya lagi, "Apakah `i <= 5`?" Jawabannya masih ya.
7. Komputer akan mencetak `1` lagi.

Proses ini akan berulang selamanya. Program Anda akan terus mencetak "1" tanpa henti dan tidak akan pernah pindah ke perintah berikutnya. Inilah mengapa sangat penting dalam perulangan `while` untuk memastikan ada sesuatu di dalam perulangan yang pada akhirnya akan membuat kondisi berhenti menjadi benar.

Kita sudah membahas for (ketika jumlahnya pasti) dan while (ketika kondisinya yang pasti). Anda telah menguasai dua pilar utama dari perulangan.

---
### 3. Perulangan Bersarang (Nested Loops)
  
Sama seperti kita bisa meletakkan `IF` di dalam `IF` (percabangan bersarang), kita juga bisa meletakkan **perulangan di dalam perulangan**. Ini disebut **perulangan bersarang** (nested loops), dan ini sangat berguna.

Bayangkan sebuah jam digital.

- Ada **perulangan luar** yang menghitung jam dari 0 hingga 23.
- Untuk **setiap jam**, ada **perulangan dalam** yang menghitung menit dari 0 hingga 59.

Perulangan menit harus menyelesaikan semua 60 putarannya sebelum perulangan jam bisa maju satu langkah.

Struktur dasarnya seperti ini:

```
ULANGI (perulangan luar):
  Lakukan sesuatu...
  
  ULANGI (perulangan dalam):
    Lakukan sesuatu yang lain...
```
Sekarang, mari kita coba dengan contoh sederhana. Menurut Anda, apa yang akan menjadi output dari algoritma di bawah ini?

```
ULANGI i DARI 1 SAMPAI 2:
  ULANGI j DARI 1 SAMPAI 3:
    Cetak "i:", i, "j:", j
```

### Praktikum Percobaan - 4
**Skenario: Countdown Peluncuran Roket** 

**Tujuan**: Anda akan membuat algoritma yang mensimulasikan hitung mundur untuk peluncuran roket.

**Aturan**:
- Program harus menghitung mundur dari angka 10 sampai 1.
- Setelah hitungan mundur selesai, program harus mencetak "Liftoff!".

**Percobaan 1: Merancang Algoritma
Tugas Anda**:

Tuliskan algoritma (dalam flowchart dan pseudocode atau langkah-langkah) untuk menghasilkan output countdown tersebut.

Gunakan perulangan `for` atau `while` untuk menyelesaikan masalah ini. Silakan coba tuliskan rancangan Anda.


## TUGAS PRAKTIKUM 
Terdapat dua soal tugas praktikum yang diperuntukan bagi mahasiswa dengan nim genap dan ganjil. Perhatikan soal dibawah ini 

### TUGAS PRAKTIKUM NIM GENAP
**Tujuan**:

Mahasiswa diharapkan mampu merancang dan mengimplementasikan algoritma yang menggabungkan penggunaan variabel, konstanta, percabangan, dan perulangan untuk mensimulasikan logika dasar dari sebuah mesin penjual otomatis.

**Skenario**:

Anda ditugaskan untuk membuat algoritma untuk sebuah mesin penjual otomatis (vending machine) yang menjual tiga jenis produk: Soda (Rp 8.000), Keripik (Rp 5.000), dan Biskuit (Rp 6.000). Mesin ini juga memiliki biaya administrasi tetap sebesar Rp 500 untuk setiap transaksi yang berhasil.

**Spesifikasi Fungsional:**
1. **Inisialisasi**:
  - Tentukan harga setiap produk sebagai konstanta.
  - Tentukan biaya administrasi sebagai konstanta.
  - Buat sebuah variabel untuk menyimpan saldo awal pengguna (misalnya, Rp 50.000).

2. **Proses Utama (Gunakan Perulangan)**:
  - Program harus terus berjalan dan menampilkan menu produk selama pengguna masih ingin bertransaksi.
  - Tampilkan saldo pengguna saat ini.
  - Tampilkan daftar produk beserta harganya.

3. **Logika Transaksi (Gunakan Percabangan)**:
  - Minta pengguna untuk memasukkan pilihan produk.
  - Gunakan struktur percabangan (`IF-ELSE-IF`) untuk menentukan produk yang dipilih.
  - Di dalam setiap cabang pilihan, gunakan percabangan bersarang untuk memeriksa dua hal:

    - Apakah saldo pengguna cukup untuk membeli produk ditambah biaya administrasi?
    - Jika saldo cukup, kurangi saldo dengan harga total dan cetak pesan "Transaksi Berhasil".
    - Jika saldo tidak cukup, cetak pesan "Saldo tidak mencukupi".

  - Jika pengguna memasukkan pilihan yang tidak valid, berikan pesan kesalahan.

4. **Selesai**:
  - Berikan pilihan bagi pengguna untuk keluar dari program. Jika pengguna memilih keluar, program berhenti dan mencetak sisa saldo terakhir.

**Tantangan Tambahan (Opsional)**:

Tambahkan **variabel** untuk stok setiap barang. Setiap kali transaksi berhasil, kurangi stoknya. Jika stok habis, barang tidak dapat dibeli.


Buat dalam bentuk **flowchart** dan **psuedocode**!

### TUGAS PRAKTIKUM NIM GANJIL
**Tujuan**:

Mahasiswa diharapkan mampu menerapkan logika perulangan yang dikombinasikan dengan percabangan kompleks untuk membuat sebuah permainan interaktif dengan aturan dan kondisi yang jelas.

**Skenario**:

Anda akan membuat algoritma untuk permainan tebak angka. Komputer akan "memikirkan" sebuah angka rahasia, dan pemain harus menebaknya dalam jumlah percobaan yang terbatas.

**Spesifikasi Fungsional**:

1. **Inisialisasi**:

  - Tentukan sebuah konstanta untuk ANGKA_RAHASIA (misalnya, 42).
  - Tentukan sebuah konstanta untuk MAKSIMAL_PERCOBAAN (misalnya, 5)
  - Buat sebuah variabel untuk melacak jumlah percobaan yang telah dilakukan, dimulai dari 0.

2. **Proses Permainan (Gunakan Perulangan)**:

  - Gunakan perulangan (while adalah pilihan yang baik di sini) yang akan terus berjalan selama dua kondisi terpenuhi:
    - Tebakan pemain belum benar.
    - Jumlah percobaan yang dilakukan belum mencapai batas maksimal.

  - Di setiap iterasi perulangan, minta pemain untuk memasukkan angka tebakan mereka.

3. **Logika Pengecekan (Gunakan Percabangan)**:

  - Di dalam perulangan, setiap kali pemain memasukkan tebakan, gunakan struktur percabangan (IF-ELSE-IF-ELSE) untuk memeriksa:

    - Jika tebakan lebih besar dari ANGKA_RAHASIA, cetak "Terlalu tinggi!".
    - Lain jika tebakan lebih kecil dari ANGKA_RAHASIA, cetak "Terlalu rendah!".
    - Lain kali (artinya tebakan benar), cetak pesan kemenangan dan hentikan perulangan.
  - Jangan lupa untuk menaikkan nilai variabel penghitung percobaan di setiap akhir iterasi.

4. **Hasil Akhir Permainan**:

  - Setelah perulangan berhenti, gunakan satu percabangan IF-ELSE terakhir untuk memeriksa mengapa perulangan berhenti:

    - Jika perulangan berhenti karena tebakan benar, cetak pesan "Selamat, Anda berhasil menebak dalam [jumlah] percobaan!".
    - Jika perulangan berhenti karena percobaan habis, cetak pesan "Maaf, percobaan Anda habis. Angka rahasianya adalah [ANGKA_RAHASIA]".

**Tantangan Tambahan (Opsional):**

  - Gunakan perulangan bersarang. Buat perulangan luar yang memungkinkan pemain untuk bermain lagi setelah permainan selesai.

Buat dalam bentuk **flowchart** dan **psuedocode**!