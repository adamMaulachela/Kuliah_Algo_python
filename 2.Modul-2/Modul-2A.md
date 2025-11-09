# 🧭 Modul Ajar: Logika Informatika — Dari Logika Proposisional ke Struktur Keputusan (If–Else)

## 1. Identitas Modul Ajar

| Komponen                | Keterangan                                                          |
| ----------------------- | ------------------------------------------------------------------- |
| **Program Studi**       | Pendidikan Teknologi Informasi                                      |
| **Mata Kuliah**         | Algoritma dan Pemrograman                                           |
| **Topik**               | Logika Informatika: Dari Logika Proposisional ke Struktur Keputusan |
| **Dosen Pengampu**      | Adam Bachtiar                                                       |
| **Semester**            | Ganjil                                                              |
| **Bobot**               | 3 SKS (150 menit tatap muka)                                        |
| **Prasyarat**           | Tidak ada                                                           |
| **Metode Pembelajaran** | Ceramah interaktif, diskusi, latihan individu/kelompok              |

---

## 2. Deskripsi Singkat

Logika informatika merupakan dasar berpikir sistematis yang memungkinkan komputer “mengambil keputusan” dengan benar. Dalam kehidupan sehari-hari, manusia sering membuat keputusan seperti *“jika hujan, maka bawa payung.”*  
Dalam dunia algoritma dan pemrograman, keputusan seperti ini diterjemahkan dalam bentuk **logika proposisional** dan **struktur kontrol (if–else)**.

Pada modul ini, mahasiswa akan belajar bagaimana berpikir logis secara formal, memahami nilai benar–salah dari suatu pernyataan, serta mengaplikasikannya ke dalam bentuk **pseudocode** yang merepresentasikan alur pengambilan keputusan dalam program.

---

## 3. Capaian Pembelajaran Mata Kuliah (CPMK) Terkait

1. Mahasiswa mampu memahami konsep dasar algoritma, logika, dan struktur kontrol dalam pemrograman.  
2. Mahasiswa mampu menerapkan logika dan penalaran sistematis dalam penyusunan algoritma.  
3. Mahasiswa mampu menuliskan algoritma dalam bentuk pseudocode yang logis dan terstruktur.

---

## 4. Sub-CPMK (Capaian Pembelajaran Pertemuan)

Setelah mengikuti pembelajaran ini, mahasiswa diharapkan mampu:
1. Menjelaskan konsep **proposisi** dan **operator logika dasar** (NOT, AND, OR, IMPLIKASI, EKUIVALENSI).  
2. Menentukan **nilai kebenaran** dari ekspresi logika sederhana maupun majemuk.  
3. Menghubungkan konsep logika proposisional dengan **struktur keputusan (if–else)** dalam pseudocode.  
4. Menyusun **pseudocode pengambilan keputusan** berdasarkan kombinasi kondisi logika.

---

## 5. Tujuan Pembelajaran

Melalui pembelajaran ini, mahasiswa akan:
- Memahami bagaimana komputer menggunakan logika untuk menentukan jalannya program.  
- Mampu menalar dan menguji kebenaran dari ekspresi logika menggunakan **tabel kebenaran**.  
- Mampu menerjemahkan logika ke dalam **algoritma pengambilan keputusan**.

---

## 6. Materi Pembelajaran

### 6.1 Pengantar Logika dalam Informatika
Logika adalah cara berpikir yang sistematis untuk menentukan apakah suatu pernyataan **benar (True)** atau **salah (False)**.  
Dalam algoritma, logika digunakan untuk membuat keputusan dan mengendalikan alur program.

Contoh:
> Jika nilai ujian ≥ 60, maka mahasiswa **lulus**; jika tidak, **tidak lulus**.

---

### 6.2 Proposisi dan Nilai Kebenaran
- **Proposisi:** Kalimat yang memiliki nilai benar (T) atau salah (F).  
  Contoh:
  - “2 + 2 = 4” → Benar (T)  
  - “5 adalah bilangan ganjil genap” → Salah (F)

---

### 6.3 Operator Logika Dasar

| Operator    | Nama        | Simbol Logika | Makna                                  | Contoh                                           |
| ----------- | ----------- | ------------- | -------------------------------------- | ------------------------------------------------ |
| NOT         | Negasi      | ¬p            | Membalik nilai kebenaran               | Jika p = T, maka ¬p = F                          |
| AND         | Konjungsi   | p ∧ q         | Benar jika **keduanya benar**          | “Saya belajar **dan** saya paham.”               |
| OR          | Disjungsi   | p ∨ q         | Benar jika **salah satu benar**        | “Saya makan **atau** minum.”                     |
| IMPLIKASI   | Kondisional | p → q         | Jika p benar maka q benar              | “Jika hujan, maka jalan basah.”                  |
| EKUIVALENSI | Dua arah    | p ↔ q         | Benar jika p dan q memiliki nilai sama | “Anda lulus **jika dan hanya jika** nilai ≥ 60.” |

---

### 6.4 Tabel Kebenaran

| p   | q   | p ∧ q | p ∨ q | ¬p  |
| --- | --- | ----- | ----- | --- |
| T   | T   | T     | T     | F   |
| T   | F   | F     | T     | F   |
| F   | T   | F     | T     | T   |
| F   | F   | F     | F     | T   |

---

### 6.5 Kombinasi Logika dan Prioritas Operator
Ekspresi logika bisa digabung menggunakan tanda kurung untuk menentukan urutan evaluasi.

Contoh:
> (p ∧ q) ∨ ¬r

Baca: “p dan q harus benar, atau r harus salah agar hasil benar.”

---

### 6.6 Penerapan Logika pada Struktur Keputusan

Komputer menggunakan logika untuk **memilih jalur eksekusi** dalam program.
Struktur umum pengambilan keputusan dalam algoritma adalah sebagai berikut:

#### Bentuk dasar (If)
```pseudocode
IF kondisi THEN
    aksi
END IF
```

#### Bentuk bercabang (If–Else)
```pseudocode
IF kondisi THEN
    aksi_1
ELSE
    aksi_2
END IF
```

#### Bentuk majemuk (If–Else If–Else)
```pseudocode
IF kondisi_1 THEN
    aksi_1
ELSE IF kondisi_2 THEN
    aksi_2
ELSE
    aksi_default
END IF
```

---

### 6.7 Contoh Penerapan Logika Proposisional dalam Pseudocode

**Kasus:**  
Sebuah sistem ingin menentukan apakah seseorang boleh mengemudi.

```pseudocode
IF (umur >= 17) AND (memiliki_SIM = TRUE) THEN
    CETAK "Boleh mengemudi"
ELSE
    CETAK "Tidak boleh mengemudi"
END IF
```

Logika proposisionalnya:
> p: umur ≥ 17  
> q: memiliki SIM  
> hasil: p ∧ q → boleh mengemudi

---

### 6.8 Latihan
1. Tentukan nilai kebenaran dari ekspresi berikut:
   - ¬(p ∨ q) jika p = T dan q = F  
   - (p ∧ q) → r jika p = T, q = F, r = T  
2. Tulis pseudocode untuk kasus berikut:
   > “Jika suhu di atas 37°C maka tampilkan ‘Demam’, jika di bawah 35°C tampilkan ‘Hipotermia’, selain itu tampilkan ‘Normal’.”

---



## 7. Refleksi Mahasiswa

> - Apa hubungan antara logika proposisional dan cara komputer membuat keputusan?  
> - Bagaimana proses berpikir logis membantu kita menulis algoritma yang benar?  
> - Situasi apa dalam kehidupan nyata yang bisa diubah menjadi logika *if–else*?

---

## 11. Lampiran

### Contoh Tabel Kebenaran
| p   | q   | ¬p  | p ∧ q | p ∨ q | p → q | p ↔ q |
| --- | --- | --- | ----- | ----- | ----- | ----- |
| T   | T   | F   | T     | T     | T     | T     |
| T   | F   | F   | F     | T     | F     | F     |
| F   | T   | T   | F     | T     | T     | F     |
| F   | F   | T   | F     | F     | T     | T     |

---

### Contoh Pseudocode Tambahan

```pseudocode
IF (nilai >= 85) THEN
    CETAK "A"
ELSE IF (nilai >= 70) THEN
    CETAK "B"
ELSE IF (nilai >= 60) THEN
    CETAK "C"
ELSE
    CETAK "D"
END IF
```

---

## TUGAS MODUL 2A
### Tugas NIM Genap
**Kasus :**
Sebuah sistem keamanan rumah otomatis memiliki 3 sensor : 
* **Sensor A** : mendeteksi gerakan di dalam rumah
* **Sensor B** : mendeteksi pintu terbuka
* **Sensor C** : mendeteksi jendela terbuka

Alaram akan berbunyi jika **(A aktif DAN B aktif), atau (A aktif DAN C aktif)**

**Pertanyaan :**
1. Nyatakan kondisi alaram berbunyi dalam bentuk ekspresi logika proposisional
2. Buat tabel kebenaran untuk menentukan kapan alaram akan berbunyi (True) dan kapan tidak (False)
3. Jelaskan dengan kalimat biasa bagaimana hubungan sensor dapat diartikan secara logis 
4. Implementasi logika proposisional ke dalam pseudocode dan flowchart


### Tugas NIM Ganjil
**Kasus :**
Dalam seleksi beasiswa, mahasiswa akan **lolos seleksi awal** jika memenuhi kriteria berikut ini : 
* IPK >= 3.25
* Penghasilan orang tua <= Rp. 4.000.000
* **Atau** jika mahasiswa aktif dalam organisasi dan memiliki IPK >= 3.00

**Pertanyaan :**
1. Bentuklah kondisi logika dari kasus ini dalam bentuk ekpresi logika proposisional dengan menggunakan simbol berikut ini : 
   * P = IPK >= 3.25
   * Q = Penghasilan <= 4 juta
   * R = Aktif Organisasi
   * S = IPK >= 3.00
2. Buat Tabel Kebenaran untuk menenutkan kapan mahasiswa lolos beasiswa dan tidak lolos beasiswa
3. Jelaskan dengan kalimat biasa bagaimana logika proposisional dari kasus ini diterjemahkan dalam alur keputusan program
4. Implementasikan logika proposisional ke dalam pseudocode dan flowchart
   
