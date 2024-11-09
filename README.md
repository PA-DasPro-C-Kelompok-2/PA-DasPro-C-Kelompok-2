# Sistem Manajemen Toko Perhiasan

## Anggota Kelompok

| Nama                      | NIM           | Kelas             |
|---------------------------|---------------|-------------------|
| Indah Maramin Al Inayah   | 2409116086    | Sistem Informasi C |
| Luthfi Daffa Purbaya      | 2409116102    | Sistem Informasi C |
| Rizky Wahyu Dina Putri    | 2409116111    | Sistem Informasi C |

## 📄Deskripsi Program
Program ini adalah sebuah sistem manajemen toko perhiasan. Terdapat 2 role yaitu admin dan user. Role admin dapat melakukan C.R.U.D. (Create, Read, Update dan Delete). Role user dapat melihat produk, transaksi pembelian, lihat saldo e-money, top up saldo e-money. cari produk dan sorting produk

### 🎯 Tujuan
Program ini bertujuan untuk mempermudah proses manajemen produk dan transaksi di toko perhiasan secara digital.

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

1. **Lihat Produk** : Menampilkan daftar produk yang tersedia.
2. **Transaksi Pembelian** : Melakukan pembelian produk dengan saldo E-Money.
3. **Lihat Saldo E-Money** : Memeriksa jumlah saldo yang tersisa.
4. **Top Up Saldo E-Money** : Menambah saldo E-Money untuk digunakan dalam transaksi.
5. **Cari Produk** : Mencari produk tertentu berdasarkan nama atau kategori.
6. **Sorting Produk** : Mengurutkan produk berdasarkan harga atau popularitas.

### 🔧 Admin
Fitur yang tersedia khusus untuk administrator:

1. **Lihat Produk** : Menampilkan semua produk yang tersedia di toko.
2. **Tambah Produk** : Menambahkan produk baru ke dalam toko.
3. **Perbarui Produk** : Memperbarui informasi produk yang ada.
4. **Hapus Produk** : Menghapus produk yang tidak tersedia lagi atau tidak dijual.
5. **Cari Produk** : Mencari produk dengan cepat berdasarkan kriteria tertentu.

## Flowchart

<details>
  <summary>1. Flowchart Menu Utama</summary>
  <img src="https://github.com/user-attachments/assets/f935e536-ad8d-4683-aeea-c668910f517b" alt="">
</details>

<details>
  <summary>2. Flowchart Login Admin</summary>
  <img src="https://github.com/user-attachments/assets/7f368320-8b2c-444b-8356-e817fbdc1acd" alt="">
</details>

<details>
  <summary>3. Flowchart Menu Admin</summary>
  <img src="https://github.com/user-attachments/assets/b4ff04bb-04aa-48e7-b649-2560a7dc4669" alt="">
</details>

<details>
  <summary>4. Flowchart Login User</summary>
  <img src="https://github.com/user-attachments/assets/3923fd84-c5c8-44de-990a-e09b6cedf0f6" alt="">
</details>

<details>
  <summary>5. Flowchart Menu User</summary>
  <img src="https://github.com/user-attachments/assets/99315b84-ed56-492e-a720-6c5bc0ea24bc" alt="">
</details>

<details>
  <summary>6. Flowchart Keluar Program</summary>
  <img src="https://github.com/user-attachments/assets/da3118cf-2e52-4081-ac71-95105173ea86" alt="">
</details>

# Penggunaan Program

<details>
<summary><h3>🏠Menu Utama</h3></summary>

![Screenshot 2024-11-09 190802](https://github.com/user-attachments/assets/4479a94c-4638-4963-878e-29c1e0d7353b)

Tampilan yang pertama kali muncul saat menjalankan program adalah menu utama. Disini terdapat 3 pilihan yaitu Login, Registrasi dan Keluar.

<details>
<summary><h3>🔑Menu Login</h3></summary>
   
### Login Admin

![Screenshot 2024-11-09 190845](https://github.com/user-attachments/assets/e064fdab-9d0b-47f3-82c3-61616b3b7dc9)

Jika ingin masuk ke menu admin masukkan:

username: admin

password: admin123

Jika benar, tekan enter untuk melanjutkan ke menu.

![Screenshot 2024-11-09 191320](https://github.com/user-attachments/assets/27b45081-215a-426b-8b66-7107d8ec06dc)

Apabila mengosongkan username, maka akan menampilkan pesan diatas.

![Screenshot 2024-11-09 191417](https://github.com/user-attachments/assets/61f46563-667a-4cd5-8cb3-f899d6eb3dc5)

Apabila mengosongkan password, maka akan menampilkan pesan di atas.

### Login User

![Screenshot 2024-11-07 104954](https://github.com/user-attachments/assets/338f5c2e-32f4-4387-85c0-7df25dcba0c4)

Jika nomor 1 yang di input di menu awal, maka akan diarahkan untuk login. Pertama masukkan nama akun yang sudah terdaftar.

![Screenshot 2024-11-07 105003](https://github.com/user-attachments/assets/997b6870-a39f-485e-85d4-bef660120329)

Lalu masukkan password yang sesuai dengan nama akun yang telah diinput sebelumnya.

![Screenshot 2024-11-09 191235](https://github.com/user-attachments/assets/80d3baaa-aba4-48e9-82cd-f9fa80c20c2c)

Jika nama akun dan password yang di input benar maka akan muncul login berhasil. Tekan enter untuk lanjut ke menu.

![Screenshot 2024-11-09 191320](https://github.com/user-attachments/assets/31abe5b0-1459-42f3-816c-d56452ab37d4)

Apabila mengosongkan username, maka akan menampilkan pesan di atas.

![Screenshot 2024-11-09 191417](https://github.com/user-attachments/assets/61f46563-667a-4cd5-8cb3-f899d6eb3dc5)

Apabila mengosongkan password, maka akan menampilkan pesan di atas.

![Screenshot 2024-11-09 191731](https://github.com/user-attachments/assets/2bc25bb1-af28-4c34-81d7-3177e9061815)

Apabila akun belum terdaftar, maka akan menampilkan pesan diatas dan memilih ingin mendaftar apa tidak. jika 'y' akan diarahkan untuk registrasi.

![Screenshot 2024-11-09 191845](https://github.com/user-attachments/assets/7ba97bb7-9350-4ef4-a890-d5b3742bdb2d)

jika 'n' maka akan menampilkan pesan diatas.

### Registrasi

![Screenshot 2024-11-07 105536](https://github.com/user-attachments/assets/a10da00a-e218-45d4-bc23-ade6bbd8927b)

Jika nomor 2 yang diinput di menu utama, maka akan di arahkan untuk registrasi telebih dahulu untuk membuat akun. Pertama masukkan nama akun yang ingin di registrasi.

![Screenshot 2024-11-09 192922](https://github.com/user-attachments/assets/bb536538-c1cb-4765-9594-de8d469f0ab9)

Lalu masukkan password

![Screenshot 2024-11-09 192949](https://github.com/user-attachments/assets/097700bc-6667-48dd-9a04-867bc89fe646)

Jika berhasil maka akan muncul pesan di atas. Tekan enter untuk lanjut.

![Screenshot 2024-11-09 193025](https://github.com/user-attachments/assets/232becfd-e8cd-42a8-b373-698bdda2e9ef)

Apabila username diisi selain huruf dan angka, maka akan menampilkan pesan diatas.

![Screenshot 2024-11-09 193112](https://github.com/user-attachments/assets/c1d39fc3-c80f-4c32-b19c-290b43e6f00e)

Apabila password diisi selain huruf dan angka, maka akan menampilkan pesan diatas.

![Screenshot 2024-11-09 193148](https://github.com/user-attachments/assets/a8bfc8e4-2451-4031-ab31-ee031a061d06)

Apabila memasukkan username dan password lebih dari 10 karakter, maka akan menampilkan pesan diatas.

### Keluar Program

![Screenshot 2024-11-07 110001](https://github.com/user-attachments/assets/a6978fca-9ddf-4aa7-8b84-e64843ec66f0)

Jika nomor 3 yang di input di menu utama, maka program akan berhenti dan menampilkan pesan di atas.

</details>

<details>
<summary><h3>🔧Menu Admin</h3></summary>

![Screenshot 2024-11-09 171743](https://github.com/user-attachments/assets/cb464432-91ca-412e-a5b3-32af19cf975b)

Masukkan usermame admin dan password admin123. Tekan enter untuk melanjutkan ke menu

![Screenshot 2024-11-09 172026](https://github.com/user-attachments/assets/24979642-b8e1-4fff-920e-4d98258324a1)

Berikut adalah menu admin.

### Tampilkan Produk

![Screenshot 2024-11-09 172108](https://github.com/user-attachments/assets/b6576d93-2bdf-416a-b63a-483ca65eef00)

Jika nomor 1 yang diinput maka akan menampilkan apa saja produk perhiasan dengan tabel yang rapi. Tekan enter untuk melanjutkan.

### Tambah Produk

![Screenshot 2024-11-07 110506](https://github.com/user-attachments/assets/606dbf4f-5e09-495d-9d43-55bce58010e9)

Jika nomor 2 yang diinput maka akan masuk ke menu menambahkan produk. Masukkan nama produk yang ingin ditambah.

![Screenshot 2024-11-09 172244](https://github.com/user-attachments/assets/72d388cb-6a55-46c4-bc4a-7268c46ab497)

Apabila pengguna tidak mengisi nama produk, maka akan menampilkan pesan diatas.

![Screenshot 2024-11-07 110540](https://github.com/user-attachments/assets/b1f8f9cc-17fe-4946-85a8-653e05a522c0)

Jika nama produk sudah diinput maka diarahkan untuk memasukkan harga produk. Harga produk tidah boleh melebihi dari 10 digit.

![Screenshot 2024-11-07 110655](https://github.com/user-attachments/assets/2ea20d9a-709c-4aff-815f-0572918038e2)

Apabila memasukkan harga produk melebihi 10 digit, maka akan menampilkan pesan diatas.

![Screenshot 2024-11-09 180640](https://github.com/user-attachments/assets/c290103f-783e-415f-8fa4-6841cf4d9f97)

Apabila memasukkan harga selain angka, maka akan menampilkan pesan diatas.

![Screenshot 2024-11-07 110815](https://github.com/user-attachments/assets/4c503bd1-f798-42d1-997a-32897f3197ab)

Selanjutnya masukkan stok produk

![Screenshot 2024-11-07 110836](https://github.com/user-attachments/assets/240b3431-20ee-4f20-a1ab-d320015eb1c0)

Jika berhasil maka akan muncul pesan seperti gambar di atas.

![Screenshot 2024-11-09 180755](https://github.com/user-attachments/assets/2f7a60c8-59e1-4d74-bf57-f762882d110e)

Apabila memasukkan stok selain angka, maka akan menampilkan pesan diatas.

### Perbarui Produk

![Screenshot 2024-11-09 173420](https://github.com/user-attachments/assets/3de4cb55-c4e3-49a3-8719-f2be8f6f248d)

Jika nomor 3 yang diinput maka akan masuk ke menu memperbarui produk. Admin harus memasukkan nama produk yang akan diperbarui.

![Screenshot 2024-11-09 174545](https://github.com/user-attachments/assets/359c4118-1570-4c72-aaad-bd938220e42e)

Apabila memasukkan nama produk yang tidak ada, maka akan menampilkan pesan diatas.

![Screenshot 2024-11-07 111404](https://github.com/user-attachments/assets/7b37afcd-ddd1-46aa-898f-eb98095ae92b)

Jika sudah memasukkan nama produk yang ingin di perbarui, lanjut memasukkan nama produk yang baru. Kosongkan jika tidak jadi mengubah.

![Screenshot 2024-11-07 111511](https://github.com/user-attachments/assets/7f2649c0-3348-47bf-b9fd-3f8f8f032184)

Selanjutnya memasukkan harga baru.

![Screenshot 2024-11-07 111535](https://github.com/user-attachments/assets/c04f389f-4075-4c21-8094-284378b2b830)

Lalu memasukkan stok produk yang baru.

![Screenshot 2024-11-09 181015](https://github.com/user-attachments/assets/3893ad3c-20cf-4a92-8be6-a6e4ff3a0916)

Jika berhasil maka akan menampilkan pesan di atas. Tekan enter untuk lanjut.

### Hapus Produk

![Screenshot 2024-11-09 181052](https://github.com/user-attachments/assets/b202c395-69a2-40ea-841e-b3adc24af11b)

Jika nomor 4 yang diinput maka akan masuk ke menu menghapus produk. Masukkan nama produk yang ingin dihapus

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

![Screenshot 2024-11-09 181258](https://github.com/user-attachments/assets/389ad3c0-ad97-4581-bb3f-efdf7557f448)

Jika nomor 6 yang diinput maka menampilkan pesan diatas. Enter untuk lanjut kembali ke menu utama.

</details>

<details>
<summary><h3>👤Menu User</h3></summary>

![Screenshot 2024-11-07 114244](https://github.com/user-attachments/assets/5e864636-5258-4d4d-bc83-302eb8391eb3)

Jika nama akun dan password di menu login benar sebagai user, maka akan menampilkan menu user. Disini terdapat 5 pilihan yaitu lihat produk, lihat saldo, top up saldo, transaksi, cari produk, sorting produk dan logout.

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

![Screenshot 2024-11-09 181800](https://github.com/user-attachments/assets/481d2b5a-efff-4060-8910-479fe1364956)

Apabila pengguna tidak mengisi pilihan nominal, maka akan menampilkan pesan diatas.

### Transaksi Pembelian

![Screenshot 2024-11-09 181901](https://github.com/user-attachments/assets/9aadf506-7b88-482d-9d61-7c0113d4004a)

Jika nomor 4 yang diinput maka akan menampilkan apa saja produk perhiasan yang akan dibeli. Masukkan nama produk yang ingin dibeli yang sudah ditampilkan dalam tabel.

![Screenshot 2024-11-09 182117](https://github.com/user-attachments/assets/4e2bc41f-3592-4f6c-8cf3-5bca7f482528)

Apabila pengguna masukkan nama yang tidak ada di menu produk, maka akan menampilkan pesan diatas.

![Screenshot 2024-11-08 003612](https://github.com/user-attachments/assets/c270dc59-783c-4107-8677-787d85d145c3)

Selanjutnya masukkan jumlah yang ingin dibeli.

![Screenshot 2024-11-08 003642](https://github.com/user-attachments/assets/4b9127c1-0e79-437f-b1eb-5fb7d7b81145)

Setelah itu pengguna akan diberikan detail pembelian dan diarahkan untuk melanjutkan pembelian atau tidak.

![Screenshot 2024-11-09 182402](https://github.com/user-attachments/assets/5d048ac4-72a0-4b5c-9a10-19ae1d4f409d)

Jika 'y' akan menampilkan pesan diatas. Tekan enter untuk mencetak invoice.

![Screenshot 2024-11-09 182459](https://github.com/user-attachments/assets/6ce4c4c8-551b-4a10-b311-71a3ab9004e2)

Selanjutnya akan menampilkan invoice. Tekan enter untuk lanjut.

![Screenshot 2024-11-09 182612](https://github.com/user-attachments/assets/602601c9-5368-489e-9a1d-61dbdcef97fb)

sedangkan 'n' menampilkan pembelian dibatalkan. Enter untuk lanjut.

### Cari Produk

![Screenshot 2024-11-07 113103](https://github.com/user-attachments/assets/74af3e89-54be-4f37-a1d9-9636e8b67648)

Jika nomor 5 yang diiinput maka akan diarahkan untuk mencari produk yang ingin dicari. Masukkan kata kunci pencarian produk.

![Screenshot 2024-11-07 113154](https://github.com/user-attachments/assets/f348cdfb-4abd-4e8f-8ba8-727504b26735)

Jika sudah memasukkan kata kunci pencarian, maka akan menampilkan hasil pencarian.

### Sorting Produk

![Screenshot 2024-11-09 182751](https://github.com/user-attachments/assets/f99cdada-b457-49da-85a0-fe7e8c278d98)

Jika nomor 6 yang diinput maka akan menampilkan menu sorting produk dan diarahkan memilih menu berdasarkan nama, harga atau stok. Jika memilih nomor 4 yaitu kembali, maka akan kembali ke menu pembeli.

![Screenshot 2024-11-09 182947](https://github.com/user-attachments/assets/221c95b5-1691-443e-a6ac-fc9ef4ed58ac)

Apabila memasukkan selain pilihan yang ada atau bukan nomor yang ada, maka akan menampilkan pesan diatas.

### Logout

![Screenshot 2024-11-09 183216](https://github.com/user-attachments/assets/31d83dbe-e103-4782-839f-58017d181a2b)

Jika nomor 7 yang diinput, maka akan menampilkan pesan diatas. Tekan enter untuk lanjut ke menu utama.

