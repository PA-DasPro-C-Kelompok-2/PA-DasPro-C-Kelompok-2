# Sistem Manajemen Toko Perhiasan

## Anggota

| Nama                      | NIM           | Kelas             |
|---------------------------|---------------|-------------------|
| Indah Maramin Al Inayah   | 2409116086    | Sistem Informasi C |
| Rizky Wahyu Dina Putri    | 2409116111    | Sistem Informasi C |
| Luthfi Daffa Purbaya      | 374982479842739 | Sistem Informasi C |

## Deskripsi Program
Program ini adalah sebuah sistem manajemen toko perhiasan. Terdapat 2 role yaitu admin dan user. Role admin dapat melakukan C.R.U.D. (Create, Read, Update dan Delete). Role user dapat melihat produk, transaksi pembelian, lihat saldo e-money, top up saldo e-money. cari produk dan sorting produk

## 📚 Library yang Digunakan
Terdapat 5 library yang kami gunakan yaitu:
1. **PrettyTable**
   Membuat tabel secara otomatis dan rapi untuk tampilan data yang lebih mudah dibaca.
2. **os**
   Mengelola interaksi dengan sistem operasi, seperti membersihkan terminal dan manajemen file.
3. **pwinput** 
   Membuat password tidak langsung terlihat
4. **json**
   Menyimpan data yang bisa dibaca manusia dan memudahkan pertukaran data antar-sistem.

## ⚙️ Fitur

### 👤 User
Fitur yang tersedia untuk pengguna biasa:

1. **Lihat Produk** - Menampilkan daftar produk yang tersedia.
2. **Transaksi Pembelian** - Melakukan pembelian produk dengan saldo E-Money.
3. **Lihat Saldo E-Money** - Memeriksa jumlah saldo yang tersisa.
4. **Top Up Saldo E-Money** - Menambah saldo E-Money untuk digunakan dalam transaksi.
5. **Cari Produk** - Mencari produk tertentu berdasarkan nama atau kategori.
6. **Sorting Produk** - Mengurutkan produk berdasarkan harga atau popularitas.

### 🔧 Admin
Fitur yang tersedia khusus untuk administrator:

1. **Lihat Produk** - Menampilkan semua produk yang tersedia di toko.
2. **Tambah Produk** - Menambahkan produk baru ke dalam toko.
3. **Perbarui Produk** - Memperbarui informasi produk yang ada.
4. **Hapus Produk** - Menghapus produk yang tidak tersedia lagi atau tidak dijual.
5. **Cari Produk** - Mencari produk dengan cepat berdasarkan kriteria tertentu.

# Penggunaan Program

<details>
<summary><h3>Menu Utama</h3></summary>

![Screenshot 2024-11-07 104302](https://github.com/user-attachments/assets/95e179be-037f-4f43-953b-34599791cde5)

Tampilan yang pertama kali muncul saat menjalankan program adalah menu utama. Disini terdapat 3 pilihan yaitu Login, Registrasi dan Keluar.

## Menu Login
### Login Admin

![Screenshot 2024-11-07 104521](https://github.com/user-attachments/assets/26278fc1-bdc1-43af-a65b-6e9fe2eb34ef)

Jika ingin masuk ke menu admin masukkan:
nama akun: admin
password: admin123
Jika benar maka akan di arahkan ke menu admin.

### Login User

![Screenshot 2024-11-07 104954](https://github.com/user-attachments/assets/338f5c2e-32f4-4387-85c0-7df25dcba0c4)

Jika nomor 1 yang di input di menu awal, maka akan diarahkan untuk login. Pertama masukkan nama akun yang sudah terdaftar.

![Screenshot 2024-11-07 105003](https://github.com/user-attachments/assets/997b6870-a39f-485e-85d4-bef660120329)

Lalu masukkan password yang sesuai dengan nama akun yang telah diinput sebelumnya.

![Screenshot 2024-11-07 105012](https://github.com/user-attachments/assets/f0293042-1879-4acf-aedf-f5d721960126)

Jika nama akun dan password yang di input benar maka akan muncul login sukses dan akan di arahkan ke menu user.

### Registrasi

![Screenshot 2024-11-07 105536](https://github.com/user-attachments/assets/a10da00a-e218-45d4-bc23-ade6bbd8927b)

Jika nomor 2 yang diinput di menu awal, maka akan di arahkan untuk registrasi telebih dahulu untuk membuat akun. Pertama masukkan nama akun yang ingin di registrasi.

**Gambar**
Lalu masukkan password

**Gambar**

Jika berhasil maka akan muncul pesan akun sudah terdaftar.

### Keluar Program

![Screenshot 2024-11-07 110001](https://github.com/user-attachments/assets/a6978fca-9ddf-4aa7-8b84-e64843ec66f0)

Jika nomor 3 yang di input di menu utama, maka program akan berhenti dan menampilkan pesan di atas.

## Menu Admin

![Screenshot 2024-11-07 110105](https://github.com/user-attachments/assets/9c561710-95c8-4b5c-98dd-f53520f90c75)

Berikut adalah menu admin jika di menu login memasukkan nama dan password admin.

### Tampilkan Produk

![Screenshot 2024-11-07 110217](https://github.com/user-attachments/assets/304f34d8-81e6-4494-a637-4298cb79864e)

Jika nomor 1 yang diinput maka akan menampilkan apa saja produk perhiasan dengan tabel yang rapi.

### Tambah Produk

![Screenshot 2024-11-07 110506](https://github.com/user-attachments/assets/606dbf4f-5e09-495d-9d43-55bce58010e9)

Jika nomor 2 yang diinput maka akan masuk ke menu menambahkan produk. Masukkan nama produk yang ingin ditambah

![Screenshot 2024-11-07 110540](https://github.com/user-attachments/assets/b1f8f9cc-17fe-4946-85a8-653e05a522c0)

Jika nama produk sudah diinput maka diarahkan untuk memasukkan harga produk. Harga produk tidah boleh melebihi dari 10 digit.

![Screenshot 2024-11-07 110655](https://github.com/user-attachments/assets/2ea20d9a-709c-4aff-815f-0572918038e2)

Apabila memasukkan harga produk melebihi 10 digit, maka akan menampilkan pesan diatas.

![Screenshot 2024-11-07 110815](https://github.com/user-attachments/assets/4c503bd1-f798-42d1-997a-32897f3197ab)

Selanjutnya masukkan stok produk

![Screenshot 2024-11-07 110836](https://github.com/user-attachments/assets/240b3431-20ee-4f20-a1ab-d320015eb1c0)

Jika berhasil maka akan muncul pesan seperti gambar di atas.

### Perbarui Produk

![Screenshot 2024-11-07 111206](https://github.com/user-attachments/assets/a76bb186-faee-4f10-8464-8a0647dbd258)

Jika nomor 3 yang diinput maka akan masuk ke menu memperbarui produk. Tekan enter untuk melanjutkan.

![Screenshot 2024-11-07 111337](https://github.com/user-attachments/assets/030c77b6-e37d-425b-aa35-def3c2caf200)

Jika sudah di enter, maka admin harus memasukkan nama produk yang akan diperbarui.

![Screenshot 2024-11-07 111404](https://github.com/user-attachments/assets/7b37afcd-ddd1-46aa-898f-eb98095ae92b)

Jika sudah memasukkan nama produk yang ingin di perbarui, lanjut memasukkan nama produk yang baru. Kosongkan jika tidak jadi mengubah.

![Screenshot 2024-11-07 111511](https://github.com/user-attachments/assets/7f2649c0-3348-47bf-b9fd-3f8f8f032184)

Selanjutnya memasukkan harga baru.

![Screenshot 2024-11-07 111535](https://github.com/user-attachments/assets/c04f389f-4075-4c21-8094-284378b2b830)

Lalu memasukkan stok produk yang baru.

![Screenshot 2024-11-07 111555](https://github.com/user-attachments/assets/651296c6-b081-4700-9070-c27a8ee14a27)

Jika berhasil maka akan menampilkan pesan di atas.

### Hapus Produk

![Screenshot 2024-11-07 112121](https://github.com/user-attachments/assets/5a15ee64-820e-4f4f-8ff7-17bac7cdb807)

Jika nomor 4 yang diinput maka akan masuk ke menu menghapus produk. Tekan enter untuk melanjutkan.

![Screenshot 2024-11-07 112150](https://github.com/user-attachments/assets/f71797f4-afea-42d0-ad0e-87f8af9a4416)

Memasukkan nama produk yang ingin dihapus

![Screenshot 2024-11-07 112227](https://github.com/user-attachments/assets/7ef3d00e-b663-4d12-8eee-c786eb527c1f)

Selanjutnya admin akan ditanya untuk meyakinkan apakah ingin menghapus produk tersebut. 

![Screenshot 2024-11-07 112256](https://github.com/user-attachments/assets/d754db1a-e6ee-40b9-9ded-374182cb9598)

Jika 'y' maka akan menampilkan pesan diatas yang berarti produk sudah dihapus.

![Screenshot 2024-11-07 112339](https://github.com/user-attachments/assets/f588f9e8-d9e3-427a-9161-80da3d75f146)

Jika 'n' maka akan menampilkan pesan diatas yang berarti produk tidak jadi dihapus.

### Cari Produk

![Screenshot 2024-11-07 112405](https://github.com/user-attachments/assets/e8831bf2-c600-4026-8546-2588f8fb18d2)

Jika nomor 5 yang diinput maka akan masuk ke menu mencari produk. Memasukkan kata kunci pencarian yang ingin dicari.

![Screenshot 2024-11-07 112452](https://github.com/user-attachments/assets/3a860d4d-41c8-4060-8096-38014895d735)

Jila sudah memasukkan kata kunci, maka akan menampilkan produk yang ingin dicari.

### Logout

Gambar

Jika nomor 6 yang diinput maka akan kembali ke menu utama.

## Menu User

![Screenshot 2024-11-07 114244](https://github.com/user-attachments/assets/5e864636-5258-4d4d-bc83-302eb8391eb3)

Jika nama akun dan password di menu login benar sebagai user, maka akan menampilkan menu user. Disini terdapat 5 pilihan yaitu lihat produk, lihat saldo, top up saldo, transaksi, cari produk, ![image](https://github.com/user-attachments/assets/1340ea90-3f18-4c91-817a-069deb306098)
 sorting produk dan logout.

### Lihat Produk

![Screenshot 2024-11-07 112837](https://github.com/user-attachments/assets/3d8d1041-a244-4b02-9e16-0a42d4474375)

Jika nomor 1 yang diinput maka akan menampilkan semua produk. Tekan enter untuk melanjutkan.

### Lihat Saldo E-Money

![Screenshot 2024-11-07 234820](https://github.com/user-attachments/assets/559913f6-9ca6-4a98-a724-728556b44f4a)

Jika nomor 2 yang diinput maka akan menampilkan saldo pengguna.

### Top Up Saldo E-Money

![Screenshot 2024-11-07 234928](https://github.com/user-attachments/assets/45cacda9-5b94-48fc-8d0e-5dd8f9d7cabf)

Jika nomor 3 yang diinput maka akan menampilkan pilihan nominal top up. Pengguna diarahkan memilih nominal top up.

![Screenshot 2024-11-07 235114](https://github.com/user-attachments/assets/6019e729-b8d1-4092-bc3f-d15207ec1294)

Jika sudah memilih nominal top up yang diinginkan, maka akan menampilkan top up behasil dan sisa saldo pengguna.

### Transaksi Pembelian

![Screenshot 2024-11-07 112935](https://github.com/user-attachments/assets/bafc6058-644a-434d-befc-ca1675f02310)

Jika nomor 4 yang diinput maka akan menampilkan apa saja produk perhiasan yang akan dibeli. Tekan enter untuk melanjutkan.

![Screenshot 2024-11-08 003527](https://github.com/user-attachments/assets/f5f3ac7b-1ab6-450f-acd7-3e3094826401)

Masukkan nama produk yang ingin dibeli yang sudah ditampilkan dalam tabel.

![Screenshot 2024-11-08 003612](https://github.com/user-attachments/assets/c270dc59-783c-4107-8677-787d85d145c3)

Selanjutnya masukkan jumlah yang ingin dibeli.

![Screenshot 2024-11-08 003642](https://github.com/user-attachments/assets/4b9127c1-0e79-437f-b1eb-5fb7d7b81145)

Setelah itu pengguna akan diberikan detail pembelian dan diarahkan untuk melanjutkan pembelian atau tidak.

![Screenshot 2024-11-08 003702](https://github.com/user-attachments/assets/d7bb0ae0-ea0c-442c-bbd3-546c47db5fbc)

Jika 'y' akan menampilkan invoice

![Screenshot 2024-11-08 003729](https://github.com/user-attachments/assets/e1846d85-dd21-4672-b747-4208ab744837)

sedangkan 'n' menampilkan pembelian dibatalkan.

### Cari Produk

![Screenshot 2024-11-07 113103](https://github.com/user-attachments/assets/74af3e89-54be-4f37-a1d9-9636e8b67648)

Jika nomor 5 yang diiinput maka akan diarahkan untuk mencari produk yang ingin dicari. Masukkan kata kunci pencarian produk.

![Screenshot 2024-11-07 113154](https://github.com/user-attachments/assets/f348cdfb-4abd-4e8f-8ba8-727504b26735)

Jika sudah memasukkan kata kunci pencarian, maka akan menampilkan hasil pencarian.

### Sorting Produk

Jika nomor 6 yang diinput maka akan diarahkan untuk menyorting produk

![Screenshot 2024-11-07 113234](https://github.com/user-attachments/assets/33573e3d-ae5d-486d-addf-c1769833f9d4)

Selanjutnya pengguna diarahkan untuk memilih urutan berdasarkan nama, harga atau stok.

![Screenshot 2024-11-07 113331](https://github.com/user-attachments/assets/2146d71c-5624-4858-be12-c70c8b820a8b)

Lalu akan diarahkan lagi untuk memilih opsi pengurutan menaik atau menurun.

### Logout

Jika nomor 7 yang diinput, maka akan keluar dari menu dan kembali ke menu utama.

