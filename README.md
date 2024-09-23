# Snapstore 🛍️

Nama: Belva Ghani Abhinaya

Kelas: PBP A

NPM: 2306203526

Link to the snapstore -> [http://belva-ghani-snapstore.pbp.cs.ui.ac.id/](http://belva-ghani-snapstore.pbp.cs.ui.ac.id/)

<details>
<summary><b>Tugas 2</b></summary>
<br>
  
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

1. Membuat direktori baru yaitu direktori Snapstore untuk dijadikan direktori untuk project django baru
2. Selanjutnya yaitu mengaktifkan virtual environment, instalasi dependencies, dan start project dengan command `python -m django startproject snapstore .`
3. Buatlah aplikasi baru dengan nama main, dengan menjalankan `python manage.py startapp main`
4. Membuat berkas product.html pada direktori baru, yaitu direktori templates pada direktori main, untuk tampilan dasar webnya
5. Product.html berisikan name, price, dan description dengan tipe masing-masing CharField, IntegerField, TextField
6. Mengubah berkas models.py dan melakukan migrations untuk mengupdate model terbaru
7. Mengisi file views.py dengan menambahkan fungsi show_main di views.py untuk menampilkan nama aplikasi serta list dari produk
8. Mengonfigurasi routing URL pada aplikasi main dan dilanjutkan dengan mengonfigurasi routing URL pada direktori proyek
9. Deploy aplikasi ke PWS
10. Selesai.

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Screenshot 2024-09-09 234332.png](https://github.com/Staphlerr/snapstore/blob/e3010cc47524d196a55d809a1c8c6512e9e28b71/Screenshot%202024-09-09%20234332.png)

### Jelaskan fungsi git dalam pengembangan perangkat lunak!

Git adalah version control yang digunakan untuk melacak perubahan kode secara efisien, memungkinkan pekerjaan yang memerlukan kolaborasi tim melalui fitur branching dan merging, serta memungkinkan pengelolaan perubahan kode tanpa mengganggu pengembangan lainnya. Dengan Git, developer dapat kembali ke versi sebelumnya, bekerja secara paralel pada proyek yang sama, dan memanfaatkan cadangan repositori jarak jauh seperti GitHub untuk pemulihan data.

### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django dipilih sebagai permulaan pembelajaran karena menyediakan banyak fitur bawaan, memudahkan pemula untuk fokus pada pengembangan tanpa harus membangun semuanya dari awal, pola MVT (Model-View-Template) yang terstruktur, serta dokumentasi yang lengkap.

### Mengapa model pada Django disebut sebagai ORM?

Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena berfungsi sebagai jembatan antara objek dalam kode Python dan tabel di database relasional. Dengan ORM, pengembang dapat berinteraksi dengan database menggunakan objek Python tanpa perlu menulis query SQL secara langsung.
</details>




<details>
<summary><b>Tugas 3</b></summary>
<br>
  
### Jelaskan mengapa kita memerlukan *data delivery* dalam pengimplementasian sebuah platform?

Data delivery sangat penting dalam pengimplementasian sebuah platform karena memungkinkan platform tersebut untuk berkomunikasi, bertukar data, dan berintegrasi dengan sistem lain secara efisien. Data delivery membantu dalam mengelola data secara dinamis, memperbarui konten, dan memastikan bahwa aplikasi tetap responsif dan relevan bagi pengguna.

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Keduanya merupakan format untuk pertukaran data. XML (eXtensible Markup Language) sudah lama digunakan dalam berbagai aplikasi untuk menyimpan dan mengirimkan informasi yang terstruktur. Namun, JSON (JavaScript Object Notation) lebih baik dan lebih populer karena beberapa alasan:
1. JSON lebih sederhana dan ringkas dibandingkan XML. JSON menggunakan lebih sedikit karakter dan lebih mudah dibaca oleh manusia, yang membuatnya lebih cepat untuk diproses oleh komputer.
2. JSON dirancang untuk menjadi format data yang lebih mudah dipahami dan digunakan oleh pengembang.
3. JSON mudah diintegrasikan dengan JavaScript, yang membuatnya sangat cocok untuk pengembangan web dan penggunaan dalam aplikasi berbasis browser.
4. JSON memiliki waktu parsing yang lebih cepat dibandingkan XML, yang membuatnya lebih efisien dalam penggunaan real-time.

### Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

Fungsi `is_valid()` pada form Django digunakan untuk memvalidasi data yang dikirim oleh pengguna melalui form. Method ini memeriksa apakah data tersebut sesuai dengan kriteria yang didefinisikan dalam form (seperti jenis data, panjang maksimal, dll.) dan memastikan bahwa data yang tidak valid tidak diproses lebih lanjut, sehingga membantu menjaga integritas data dan keamanan aplikasi. Kita membutuhkan method ini untuk mencegah kesalahan data dan serangan yang mungkin terjadi melalui input yang tidak valid.

### Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

`csrf_token` (Cross-Site Request Forgery token) adalah komponen keamanan penting saat membuat form di Django. Ini bertujuan untuk mencegah serangan CSRF, di mana penyerang dapat memanipulasi pengguna yang sah untuk melakukan tindakan tanpa sepengetahuan atau persetujuan mereka pada aplikasi web. Tanpa `csrf_token`, form bisa dimanipulasi oleh penyerang untuk melakukan aksi berbahaya seperti mengubah kata sandi atau transaksi finansial. `csrf_token` membantu memastikan bahwa setiap request yang diterima oleh server benar-benar berasal dari pengguna yang sah dan bukan dimanipulasi oleh pihak ketiga.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Buatlah berkas `forms.py` pada direktori main, yang berisikan kode untuk membuat struktur *form* yang dapat menerima data baru dari pengguna. Isi dari `forms.py` akan berdasar pada models yang telah dibuat sebelumnya.
2. Masuklah ke dalam berkas `views.py`, tambahkan import redirect dan beberapa fungsi dari `forms.py` dan `models.py`, serta HTTPResponse dan serializers.
3. Buatlah fungsi baru untuk menambahkan item baru dengan POST.
4. Buka `urls.py` yang ada pada direktori main dan import fungsi yang sudah dibuat tadi.
5. Tambahkan path URL ke dalam variabel urlpatterns pada `urls.py` di main.
6. Buat berkas HTML baru pada direktori main/templates, yang berisikan penanda block untuk form, token untuk security, template tag, dan tombol submit.
7. Buka `main.html` dan tambahkan beberapa kode untuk menampilkan data form dalam bentuk tabel serta tombol submit yang akan redirect ke halaman form.
8. Buatlah 4 fungsi pada `views.py` untuk melihat data JSON dan XML, contohnya adalah fungsi `show_xml`, `show_json`, `show_json_by_id`, `show_xml_by_id`.
9. Buka `urls.py` yang ada pada direktori main dan import fungsi yang sudah dibuat tadi.
10. Tambahkan path URL ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.

### Screenshot Postman
![show_xml](https://github.com/Staphlerr/snapstore/blob/main/images/Screenshot%202024-09-17%20234937.png)
![show_json](https://github.com/Staphlerr/snapstore/blob/main/images/Screenshot%202024-09-17%20234950.png)
![show_xml_by_id](https://github.com/Staphlerr/snapstore/blob/main/images/Screenshot%202024-09-17%20235024.png)
![show_json_by_id](https://github.com/Staphlerr/snapstore/blob/main/images/Screenshot%202024-09-17%20235007.png)
</details>

<details>
<summary><b>Tugas 4</b></summary>
<br>

### Apa perbedaan antara HttpResponseRedirect() dan redirect()?

### Jelaskan cara kerja penghubungan model Product dengan User!

### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
</details>
