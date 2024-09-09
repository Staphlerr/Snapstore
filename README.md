# Snapstore 🛍️

Nama: Belva Ghani Abhinaya

Kelas: PBP A

NPM: 2306203526

Link to the snapstore -> [LINK](http://belva-ghani-snapstore.pbp.cs.ui.ac.id/)

## Tugas 2

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
