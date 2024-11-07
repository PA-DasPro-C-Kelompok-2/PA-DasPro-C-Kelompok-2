# Sistem Manajemen Toko Perhiasan

## Deskripsi Program
Program ini adalah sebuah sistem manajemen toko perhiasan. Terdapat 2 role yaitu admin dan user. Role admin dapat melakukan C.R.U.D. (Create, Read, Update dan Delete). Role user dapat melihat produk, transaksi pembelian, lihat saldo e-money, top up saldo e-money. cari produk dan sorting produk

## Library
Terdapat 5 library yab=ng kami gunakan yaitu:
1. PrettyTable membuat tabel secara otomatis dan rapi
2. os
3. pwinput
4. time
5. json

## Fitur
### User
1. Lihat Produk
2. Transaksi Pembelian
3. Lihat Saldo E-Money
4. Top Up Saldo E-Money
5. Cari Produk
6. Sorting Produk

### Admin
1. Lihat Produk
2. Tambah Produk
3. Perbarui Produk
4. Hapus Produk
5. Cari Produk


# Penggunaan Program

## Menu Utama

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

Gambar

Jika nomor 3 yang diinput maka akan masuk ke menu memperbarui produk. Tekan enter untuk melanjutkan.

Gambar

Jika sudah di enter, maka admin harus memasukkan nama produk yang akan diperbarui.

Gambar

Jika sudah memasukkan nama produk yang ingin di perbarui, lanjut memasukkan nama produk yang baru. 

Gambar

Selanjutnya memasukkan harga baru.

Gambar

Lalu memasukkan stok produk yang baru.

Gambar

Jika berhasil maka akan menampilkan pesan di atas.

### Hapus Produk

Gambar

Jika nomor 4 yang diinput maka akan masuk ke menu menghapus produk. Tekan enter untuk melanjutkan.

Gambar

Memasukkan nama produk yang ingin dihapus

Gambar

Selanjutnya admin akan ditanya untuk meyakinkan apakah ingin menghapus produk tersebut. 

Gambar

Jika 'y' maka akan menampilkan pesan diatas yang berarti produk sudah dihapus.

Gambar

Jika 'n' maka akan menampilkan pesan diatas yang berarti produk tidak jadi dihapus.

### Cari Produk

Gambar

Jika nomor 5 yang diinput maka akan masuk ke menu mencari produk

Gambar

Memasukkan kata kunci pencarian yang ingin dicari.

Gambar

Jila sudah memasukkan kata kunci, maka akan menampilkan produk yang ingin dicari.

### Logout

Gambar

Jika nomor 6 yang diinput maka akan kembali ke menu utama.

## Menu User

**Gambar**

Jika nama akun dan password di menu login benar sebagai user, maka akan menampilkan menu user. Disini terdapat 5 pilihan yaitu lihat produk, transaksi pembelian, lihat saldo, top up saldo, cari produk, sorting produk dan logout.

### Lihat Produk

Gambar

Jika nomor 1 yang diinput maka akan menampilkan semua produk.

### Transaksi Pembelian

Gambar

Jika nomor 2 yang diinput maka akan menampilkan apa saja produk hiasan yang akan dibeli.

Gambar

Masukkan nama produk yang ingin dibeli yang sudah ditampilkan dalam tabel.

**Gambar**

Selanjutnya masukkan jumlah yang ingin dibeli.

**Gambar**

Setelah itu pengguna akan diberikan detail pembelian dan diarahkan untuk melanjutkan pembelian atau tidak.

**Gambar**

Jika 'y' akan menampilkan invoice, sedangkan 'n' menampilkan pembelian dibatalkan.

### Lihat Saldo E-Money

**Gambar**

Jika nomor 3 yang diinput maka akan menampilkan saldo pengguna.

### Top Up Saldo E-Money

**Gambar**

Jika nomor 4 yang diinput maka akan menampilkan pilihan nominal top up

**Gambar**

Pengguna diarahkan memilih nominal top up

Gambar

Jika sudah memilih nominal top up yang diinginkan, maka akan menampilkan top up behasil dan sisa saldo pengguna.

### Cari Produk

Gambar

Jika nomor 5 yang diiinput maka akan diarahkan untuk mencari produk yang ingin dicari.

Gambar

Masukkan kata kunci pencarian produk.

Gambar

Jika sudah memasukkan kata kunci pencarian, maka akan menampilkan hasil pencarian.

### Sorting Produk

Gambar

Jika nomor 6 yang diinput maka akan diarahkan untuk menyorting produk

Gambar

Selanjutnya pengguna diarahkan untuk memilih urutan berdasarkan nama, harga atau stok.

Gambar

Lalu akan diarahkan lagi untuk memilih opsi pengurutan menaik atau menurun.

### Logout

Jika nomor 7 yang diinput, maka akan keluar dari menu dan kembali ke menu utama.

