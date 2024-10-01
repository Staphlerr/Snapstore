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

`HttpResponseRedirect()` adalah kelas bawaan Django yang digunakan untuk membuat respons pengalihan (status 302) dengan URL tujuan yang harus ditentukan secara eksplisit, sementara `redirect()` adalah fungsi utilitas yang lebih fleksibel dan mudah digunakan, memungkinkan pengalihan dengan berbagai argumen seperti URL, nama *URL pattern*, atau objek model. `redirect()` menyederhanakan penggunaan `HttpResponseRedirect()` dengan menyediakan abstraksi yang lebih praktis dalam kebanyakan kasus.

### Jelaskan cara kerja penghubungan model Product dengan User!

Untuk menghubungkan model `Product` dengan `User` di Django, biasanya digunakan *ForeignKey* yang menautkan setiap produk ke pengguna tertentu. Dalam model `Product`, tambahkan field `owner` atau `user` yang mengacu ke model `User` dengan `ForeignKey(User, on_delete=CASCADE)`, sehingga setiap produk terkait dengan satu pengguna. `on_delete=CASCADE` memastikan jika pengguna dihapus, produk terkait juga ikut dihapus. Ini memungkinkan setiap produk dimiliki oleh pengguna yang berbeda.

### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

Authentication adalah proses memverifikasi identitas pengguna (misalnya, dengan username dan password), sementara authorization adalah pemberian izin untuk mengakses sumber daya atau fitur setelah pengguna terautentikasi. Saat pengguna login, **authentication** dilakukan dengan memeriksa kredensialnya. Django mengimplementasikan authentication melalui sistem login bawaan, memeriksa username dan password dengan model `User`. Setelah itu, **authorization** dilakukan dengan memastikan pengguna memiliki izin untuk mengakses halaman atau aksi tertentu menggunakan fitur seperti `permissions` atau `is_authenticated`.

### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Django mengingat pengguna yang telah login dengan menyimpan *session ID* dalam cookie di browser pengguna. Setiap kali pengguna mengirim permintaan, Django memeriksa cookie ini untuk mengidentifikasi sesi dan pengguna terkait. Selain untuk sesi, cookies juga digunakan untuk menyimpan preferensi pengguna atau data pelacakan. Namun, tidak semua cookies aman; misalnya, cookies yang tidak dienkripsi (*non-secure*) rentan terhadap pencurian melalui serangan *man-in-the-middle*. Django melindungi cookies penting dengan fitur seperti *HttpOnly* dan *Secure* untuk mencegah akses yang tidak sah.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Implementasi fungsi register, fungsi login_user, dan fungsi logout_user pada `views.py`, lalu tambahkan path URL ketiga fungsi tadi ke `urls.py`.
   - Fungsi register digunakan untuk membuat laman untuk mendaftarkan akun pengguna
   - Fungsi login_user digunakan untuk mengautentikasi pengguna yang ingin masuk ke dalam websitenya. Fungsi login_user diimplementasi menggunakan fungsi `authenticate` dan `login` yang merupakan fungsi bawaan Django.
   - Fungsi logout_user digunakan untuk melakukan mekanisme keluar dari akun. Fungsi logout_user diimplementasi menggunakan fungsi `logout` yang merupakan fungsi bawaan Django.
   - Buat juga `register.html` dan `login.html` untuk interface laman register dan laman login (logout tidak perlu interface karena ketika pengguna melakukan logout, akan kembali ke login.html).
2. Membuat 2 akun dengan meregistrasi di bagian url register. Kemudian, login dengan akun pertama yang telah dibuat. Setelah login, kemudian mengakses create_item_entry untuk menambahkan 3 dummy data. Setelah itu, logout dari akun pertama dan login dengan akun yang lain (akun kedua) dan lanjut mengakses create_item_entry untuk menambahkan 3 dummy data yang berbeda dengan akun pertama. Setelah itu lakukan logout dari akun kedua.
3. Buka `models.py` dan import User, lalu tambahkan potongan kode `user = models.ForeignKey(User, on_delete=models.CASCADE)` pada fungsi Product untuk menghubungkan satu item entry dengan satu user, sehingga untuk sebuah item entry pasti terasosiasikan dengan seorang user.
4. Selanjutnya yaitu buka `views.py` lalu tambahkan potongan kode `mood_entry = form.save(commit=False)` pada fungsi create_item_entry. Parameter (commit=False) disini berguna untuk mencegah Django agar tidak langsung menyimpan objek yang telah dibuat dari form langsung ke database, sehingga user dapat memodifikasi objek terlebih dahulu sebelum disimpan ke database.
5. Ubah value 'name' pada item_entries menjadi `reguest.user.username` sehingga menampilkan username pengguna yang login pada halaman main.
6. Jangan lupa untuk melakukan makemigrations dan migrate, karena mengubah model.
7. Selanjutnya persiapkan web untuk _environtment production_ dengan import os pada settings.py dan ganti variabel DEBUG menjadi:
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
8. Selanjutnya, buka `views.py` lalu import HttpResponseRedirect, reverse, dan datetime yang kemudian kita akan menggunakannya pada fungsi login_user, sehingga dapat menambahkan _cookie_ yang bernama `last_login` untuk melihat kapan terakhir kali pengguna melakukan login.
9. Tambahkan informasi _cookie_ `last_login` pada response yang akan ditampilkan di halaman web dengan menambahkan `'last_login': request.COOKIES['last_login']` pada fungsi show_main
10. Jangan lupa untuk menambahkan implementasi kode untuk menghapus cookie last_login saat pengguna melakukan logout.
11. Terakhir, buka berkas `main.html` dan tambahkan kode `<h5>Sesi terakhir login: {{ last_login }}</h5>` untuk menampilkan last_login pengguna
</details>

<details open>
<summary><b>Tugas 5</b></summary>
<br>

### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Urutan prioritas CSS Selector dimulai dari yang paling prioritas yaitu Inline styles > ID selector (`#id`) > Class/Attribute/Pseudo-class selector (`.class`, `[type="text"]`, `:hover`) > Type selector/Pseudo-element (`div`, `::before`).

### Mengapa _responsive design_ menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan _responsive design_!

_Responsive design_ memungkinkan situs web untuk menyesuaikan tampilannya di berbagai ukuran layar dan perangkat, seperti desktop, tablet, dan smartphone. Ini penting karena pengguna mengakses internet melalui berbagai perangkat dengan resolusi dan dimensi yang berbeda. Desain yang tidak responsif dapat membuat pengalaman pengguna buruk, seperti teks atau elemen yang tidak terbaca atau terlalu kecil di layar yang lebih kecil.
- Contoh aplikasi yang sudah menerapkan _responsive design_ yaitu Facebook dan Google. Kedua platform ini menyesuaikan tampilan berdasarkan ukuran layar pengguna.
- Contoh aplikasi yang belum menerapkan _responsive design_ yaitu situs web lama atau situs yang menggunakan _fixed design_ sehingga tidak menerapkan responsivitas, misalnya situs web yang hanya dioptimalkan untuk desktop tanpa memperhatikan pengguna mobile.

### Jelaskan perbedaan antara _margin_, _border_, dan _padding_, serta cara untuk mengimplementasikan ketiga hal tersebut!

- **_Margin_** adalah ruang di luar border elemen. Ini digunakan untuk membuat jarak antara elemen yang berbeda.
- **_Border_** adalah garis yang mengelilingi padding dan konten elemen. _Border_ dapat dikustomisasi dengan warna, ketebalan, dan gaya.
- **_Padding_** adalah ruang antara konten elemen dan border. _Padding_ menambah ruang di dalam elemen itu sendiri.
- Contoh implementasi:
`div {
      margin: 20px;
      border: 2px solid;
      padding: 10px;
  }`

### Jelaskan konsep _flex box_ dan _grid layout_ beserta kegunaannya!

- **_Flexbox_** adalah modul CSS yang dirancang untuk menyusun elemen secara fleksibel dan dinamis dalam satu dimensi (baik itu kolom atau baris). _Flexbox_ memudahkan pengaturan alignment, distribusi ruang, dan pengelolaan ukuran elemen dalam satu baris atau kolom. Kegunaan dari _flexbox_ adalah membuat layout yang responsif dengan mudah mengatur posisi dan ukuran elemen.
- **_Grid Layout_** adalah modul CSS yang dapat membantu membuat tata letak dua dimensi (baris dan kolom). _Grid layout_ dapat membuat layout kompleks dengan lebih mudah dibandingkan metode tradisional.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!


</details>
