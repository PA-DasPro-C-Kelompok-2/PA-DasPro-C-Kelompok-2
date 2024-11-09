import json
import os
from prettytable import PrettyTable
import pwinput

def clear():
    os.system("cls")

def inisialisasi_file():
    if not os.path.exists("pengguna.json"):
        with open("pengguna.json", "w") as file:
            json.dump([], file, indent=4)
            
jsonPathProduk = r"produk.json"
try:
    with open(jsonPathProduk, "r") as file:
        dataProduk = json.load(file)
except FileNotFoundError:
    print("File produk.json tidak ditemukan!")
    dataProduk = []
except json.JSONDecodeError:
    print("Terjadi kesalahan dalam membaca data produk.")
    dataProduk = []

def simpan_produk(produk):
    with open('produk.json', 'w') as f:
        json.dump(produk, f, indent=4)

def simpan_pengguna(pengguna):
    with open('pengguna.json', 'w') as f:
        json.dump(pengguna, f, indent=4)

def muat_pengguna():
    try:
        with open('pengguna.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def tampilkan_produk():
    clear()
    produk = dataProduk
    if not produk:
        print("Belum ada produk tersedia!")
        return
    
    tabel = PrettyTable()
    tabel.title = "Produk Perhiasan"
    tabel.field_names = ["Nama", "Harga", "Stok"]
    for detail in produk:
        Harga = int(detail["Harga"])
        tabel.add_row([
            detail["Nama"],
            f"Rp {Harga:,}",
            detail["Stok"]
        ])
    print(tabel)

def tambah_produk():
    clear()
    produk = dataProduk
    try:
        nama = input("Masukkan nama produk: ")
        if not nama.isalnum():
            print("+====================================================================+")
            print("|                   Nama produk harus diisi!                         |")
            print("+====================================================================+")
            return
        harga = int(input("Masukkan harga produk: Rp "))
        if harga <= 0:
            print("+====================================================================+")
            print("|                     Harga harus lebih dari 0!                      |")
            print("+====================================================================+")
            return
        if len(str(harga)) > 10:
            print("+====================================================================+")
            print("|             Harga tidak boleh lebih dari 10 digit!                 |")
            print("+====================================================================+")
            input("Tekan enter untuk kembali...")
            return
        stok = int(input("Masukkan stok produk: "))
        if stok < 0:
            print("+====================================================================+")
            print("|                      Stok tidak boleh negatif!                     |")
            print("+====================================================================+")
            return       
    except ValueError:
        print("+====================================================================+")
        print("|              Harga dan stok harus berupa angka!                    |")
        print("+====================================================================+")
        return
    except KeyboardInterrupt:
        ("")
    except EOFError:
        ("")
    produk.append({
        "Nama": nama,
        "Harga": harga,
        "Stok": stok
    })
    simpan_produk(produk)
    print("+====================================================================+")
    print("|                  Produk berhasil ditambahkan!                      |")
    print("+====================================================================+")

def perbarui_produk():
    clear()
    produk = dataProduk
    if not produk:
        print("+====================================================================+")
        print("|                  Belum ada produk tersedia!                        |")
        print("+====================================================================+")
        return

    tampilkan_produk()
    nama_produk = input("Masukkan nama produk yang akan diperbarui: ")
    produk_ditemukan = None
    for item in produk:
        if item["Nama"].lower() == nama_produk.lower():
            produk_ditemukan = item
            break
    if not produk_ditemukan:
        print("+====================================================================+")
        print("|                   Produk tidak ditemukan!                          |")
        print("+====================================================================+")
        return
    print("\nBiarkan kosong jika tidak ingin mengubah")
    nama_baru = input(f"Masukkan nama baru ({produk_ditemukan['Nama']}): ")
    harga_baru = input(f"Masukkan harga baru (Rp {produk_ditemukan['Harga']:,}): ")
    stok_baru = input(f"Masukkan stok baru ({produk_ditemukan['Stok']}): ")
    if nama_baru:
        produk_ditemukan["Nama"] = nama_baru
    if harga_baru:
        try:
            harga_baru = int(harga_baru)
            if harga_baru <= 0:
                print("+====================================================================+")
                print("|                    Harga harus lebih dari 0!                       |")
                print("+====================================================================+")
                return
            produk_ditemukan["Harga"] = harga_baru
        except ValueError:
            print("+====================================================================+")
            print("|                   Harga harus berupa angka!                         |")
            print("+====================================================================+")
            return
        except KeyboardInterrupt:
            input("Tekan enter untuk melanjutkan.....")
    if stok_baru:
        try:
            stok_baru = int(stok_baru)
            if stok_baru < 0:
                print("+====================================================================+")
                print("|                  Stok tidak boleh negatif!                         |")
                print("+====================================================================+")
                return
            produk_ditemukan["Stok"] = stok_baru
        except ValueError:
            print("+====================================================================+")
            print("|                    Stok harus berupa angka!                        |")
            print("+====================================================================+")
            return
        except KeyboardInterrupt:
            input("Tekan enter untuk melanjutkan.....")
    simpan_produk(produk)
    print("+====================================================================+")
    print("|                    Produk berhasil diperbarui!                     |")
    print("+====================================================================+")

def hapus_produk():
    clear()
    produk = dataProduk
    if not produk:
        print("+====================================================================+")
        print("|                   Belum ada produk tersedia!                       |")
        print("+====================================================================+")
        return
    tampilkan_produk()
    nama_produk = input("Masukkan nama produk yang akan dihapus: ")
    produk_ditemukan = None
    for item in produk:
        if item["Nama"].lower() == nama_produk.lower():
            produk_ditemukan = item
            break
    if not produk_ditemukan:
        print("+====================================================================+")
        print("|                    Produk tidak ditemukan!                         |")
        print("+====================================================================+")
        return
    konfirmasi = input(f"Yakin ingin menghapus {produk_ditemukan['Nama']}? (y/n): ").lower()
    if konfirmasi == 'y':
        produk.remove(produk_ditemukan) 
        simpan_produk(produk)
        print("+====================================================================+")
        print("|                      Produk berhasil dihapus!                      |")
        print("+====================================================================+")
    else:
        print("+====================================================================+")
        print("|                      Penghapusan dibatalkan.                       |")
        print("+====================================================================+")

def cari_produk():
    clear()
    produk = dataProduk
    if not produk:
        print("+====================================================================+")
        print("|                  Belum ada produk tersedia!                        |")
        print("+====================================================================+")
        return
    kata_kunci = input("Masukkan kata kunci pencarian: ").lower()
    hasil = [detail for detail in produk if kata_kunci in detail["Nama"].lower()]
    if hasil:
        tabel = PrettyTable()
        tabel.title = "Hasil Pencarian"
        tabel.field_names = ["Nama", "Harga", "Stok"]
        for detail in hasil:
            try:
                harga = int(detail["Harga"])  
                tabel.add_row([
                    detail["Nama"],
                    f"Rp {harga:,}",
                    detail["Stok"]
                ])
            except ValueError:
                print(f"Data harga untuk {detail['Nama']} tidak valid.")
                continue  
        print(tabel)
    else:
        print("+====================================================================+")
        print("|                  Produk tidak ditemukan!                           |")
        print("+====================================================================+")

def urutkan_produk(user):
    while True:
        clear()
        if not dataProduk:
            print("+====================================================================+")
            print("|                  Belum ada produk tersedia!                        |")
            print("+====================================================================+")
            return
        print("+====================================================================+")
        print("|                        Silahkan Pilih Menu                         |")
        print("+====================================================================+")
        print("| [1]. Berdasarkan Nama                                              |")
        print("| [2]. Berdasarkan Harga                                             |")
        print("| [3]. Berdasarkan Stok                                              |")
        print("| [4]. Kembali                                                       |")
        print("+====================================================================+")
        try:
            pilihan = int(input("Pilih menu: "))
            if pilihan in [1, 2, 3]:
                tabel = PrettyTable()
                tabel.clear_rows()
                tabel.title = "Data Produk"
                tabel.field_names = ["Nomor", "Nama", "Harga", "Stok"]
                sorted_data = dataProduk.copy()
                for produk in sorted_data:
                    if isinstance(produk['Harga'], str):
                        produk['Harga'] = int(produk['Harga'])
                    if isinstance(produk['Stok'], str):
                        produk['Stok'] = int(produk['Stok'])
                if pilihan == 1:
                    sorted_data = sorted(sorted_data, key=lambda x: x['Nama'])
                elif pilihan == 2:
                    sorted_data = sorted(sorted_data, key=lambda x: x['Harga'])
                else:
                    sorted_data = sorted(sorted_data, key=lambda x: x['Stok'])
                for nomor, produk in enumerate(sorted_data, start=1):
                    tabel.add_row([
                        nomor,
                        produk["Nama"],
                        f"Rp.{produk['Harga']:,}",
                        produk["Stok"]
                    ])
                print(tabel)
                input("Tekan enter untuk melanjutkan.....")
            elif pilihan == 4:
                break
            else:
                print("+====================================================================+")
                print("|                     Pilihan tidak valid!                            |")
                print("+====================================================================+")
                input("Tekan enter untuk melanjutkan.....")
        except ValueError:
            print("+====================================================================+")
            print("|           Input tidak valid. Harap masukkan nomor.                 |")
            print("+====================================================================+")
            input("Tekan enter untuk melanjutkan.....")
        except KeyboardInterrupt:
            print("========================================================")
            print("|  Tolong jangan menekan ctrl dan c secara bersamaan!  |")
            print("========================================================")
            input("Tekan enter untuk melanjutkan.....")

def transaksi(user):
    clear()
    produk = dataProduk  
    if not produk:
        print("+====================================================================+")
        print("|                Belum ada produk yang tersedia!                     |")
        print("+====================================================================+")
        return
    tampilkan_produk()  
    nama_produk = input("Masukkan nama produk yang ingin dibeli: ").lower()
    produk_ditemukan = None
    for detail in produk:  
        if detail["Nama"].lower() == nama_produk:
            produk_ditemukan = detail
            break
    if not produk_ditemukan:
        print("+====================================================================+")
        print("|                    Produk tidak ditemukan!                         |")
        print("+====================================================================+")
        return
    try:
        jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
        if jumlah <= 0:
            print("+====================================================================+")
            print("|              Jumlah pembelian harus lebih dari 0!                  |")
            print("+====================================================================+")
            return
        stok_produk = int(produk_ditemukan["Stok"])  
        harga_produk = int(produk_ditemukan["Harga"])  
        saldo_user = int(user["saldo"])  
    except ValueError:
        print("Data input tidak valid. Pastikan jumlah, stok, harga, dan saldo adalah angka yang valid.")
        return
    if jumlah > stok_produk:
        print("+====================================================================+")
        print("|                      Stok tidak mencukupi!                         |")
        print("+====================================================================+")
        return
    total_harga = harga_produk * jumlah  
    if saldo_user < total_harga:
        print(f"Saldo tidak mencukupi! Total pembelian: Rp {total_harga:,}")
        return
    print(f"\nDetail Pembelian:")
    print(f"Produk: {produk_ditemukan['Nama']}")
    print(f"Jumlah: {jumlah}")
    print(f"Total: Rp {total_harga:,}")
    konfirmasi = input("Lanjutkan pembelian? (y/n): ").lower()
    if konfirmasi != 'y':
        print("+====================================================================+")
        print("|                     Pembelian dibatalkan.                          |")
        print("+====================================================================+")
        return
    produk_ditemukan["Stok"] = str(stok_produk - jumlah)  
    simpan_produk(produk)  
    pengguna = muat_pengguna()
    for p in pengguna:
        if p["username"] == user["username"]:
            p["saldo"] = str(saldo_user - total_harga)  
            user["saldo"] = p["saldo"]  
            break
    simpan_pengguna(pengguna)  
    print("+====================================================================+")
    print("|              Selamat! Pembelian anda berhasil.                     |")
    print("+====================================================================+")
    input("Tekan Enter untuk mencetak invoice...")
    print("\n========= INVOICE ========")
    print(f"Pembeli: {user['username']}")
    print(f"Produk: {produk_ditemukan['Nama']}")
    print(f"Jumlah: {jumlah}")
    print(f"Total: Rp {total_harga:,}")
    print(f"Sisa saldo: Rp {saldo_user - total_harga:,}")

def lihat_saldo(user):
    clear()
    try:
        clear()
        saldo_user = int(user['saldo'])  
        print(f"Saldo Anda: Rp {saldo_user:,}")
    except ValueError:
        print("Saldo tidak valid. Harap periksa data pengguna.")
    except KeyboardInterrupt:
            input("Tekan enter untuk melanjutkan.....")

def top_up_saldo(user):
    clear()
    pilihan_nominal = [5000000, 7000000, 10000000, 15000000, 17000000, 20000000]
    tabel = PrettyTable()
    tabel.title = "Pilihan Nominal Top-Up"
    tabel.field_names = ["Nomor", "Nominal"]
    
    for i, nominal in enumerate(pilihan_nominal, 1):
        tabel.add_row([i, f"Rp {nominal:,}"])
    
    print("\n======== Pilihan Nominal Top-Up ========")
    print(tabel)
    
    try:
        pilihan = int(input("Pilih nominal top-up (1-6): "))
        if not (1 <= pilihan <= len(pilihan_nominal)):
            print("+====================================================================+")
            print("|                     Pilihan tidak valid.                           |")
            print("+====================================================================+")
            return
        jumlah = pilihan_nominal[pilihan - 1]
        pengguna = muat_pengguna()
        for p in pengguna:
            if p["username"] == user["username"]:
                try:
                    saldo_terbaru = int(p["saldo"]) + jumlah  
                    p["saldo"] = saldo_terbaru  
                    user["saldo"] = saldo_terbaru  
                    break
                except:
                    print("+====================================================================+")
                    print("|        Saldo tidak valid. Harap periksa data pengguna.             |")
                    print("+====================================================================+")
        simpan_pengguna(pengguna)
        print(f"Top-up berhasil! Saldo Anda sekarang: Rp {user['saldo']:,}")
    except ValueError:
        print("+====================================================================+")
        print("|            Input tidak valid. Harap masukkan nomor.                |")
        print("+====================================================================+")
    except KeyboardInterrupt:
        ("")
    except EOFError:
        ("") 

def registrasi():
    clear()
    pengguna = muat_pengguna()
    username = input("Masukkan username: ")
    if not username.isalnum():
        print("+====================================================================+")
        print("|          Username hanya boleh berisi huruf dan angka!              |")
        print("+====================================================================+")
        return
    if len(str(username)) > 10:
        print("+====================================================================+")
        print("|           Username tidak boleh lebih dari 10 karakter!             |")
        print("+====================================================================+")
        return
    if any(user["username"] == username for user in pengguna):
        print("+====================================================================+")
        print("|                    Username sudah digunakan!                       |")
        print("+====================================================================+")
        return
    password = pwinput.pwinput("Masukkan password: ")
    if len(str(password)) > 10:
        print("+====================================================================+")
        print("|           Password tidak boleh lebih dari 10 karakter!             |")
        print("+====================================================================+")
        return
    if not password.isalnum():
        print("+====================================================================+")
        print("|        Password hanya boleh berisi huruf dan angka!                |")
        print("+====================================================================+")
        return
    pengguna.append({
        "username": username.lower(),
        "password": password,
        "role": "user",
        "saldo": 0
    })
    print("+====================================================================+")
    print("|               Selamat! akun anda sudah terdaftar.                  |")
    print("+====================================================================+")
    simpan_pengguna(pengguna)
    
def login(): 
    clear()
    pengguna = muat_pengguna()
    try:
        username = input("Masukkan username: ").lower()
        if not username.isalnum():
            print("+====================================================================+")
            print("|                      Username harus diisi!                         |")
            print("+====================================================================+")
            input('Tekan Enter untuk melanjutkan...')
            return
        password = pwinput.pwinput("Masukkan password: ").lower()
        if not password.isalnum():
            print("+====================================================================+")
            print("|                       Password harus diisi!                        |")
            print("+====================================================================+")
            input('Tekan Enter untuk melanjutkan...')
            return
        if username == "admin" and password == "admin123":
            print("+====================================================================+")
            print("|                   Login sebagai Admin berhasil!                    |")
            print("+====================================================================+")
            input("Tekan enter untuk melanjutkan ke menu..")
            menu_admin()
            return
        for user in pengguna:
            if user["username"].lower() == username and user["password"].lower() == password:
                print("+====================================================================+")
                print("|                           Login berhasil!                          |")
                print("+====================================================================+")
                input("Tekan enter untuk melanjutkan ke menu..")
                menu_user(user)
                return
        print("+====================================================================+")
        print("|               Mohon Maaf, akun Anda tidak terdaftar.               |")
        print("+====================================================================+")
        pilih = input("Apakah Anda ingin mendaftar? (y/n): ").lower()
        if pilih == "y":
            registrasi()
        else:
            print("+====================================================================+")
            print("|  Silahkan registrasi terlebih dahulu untuk menggunakan sistem.     |")
            print("+====================================================================+")
            input("Tekan enter untuk kembali ke menu..")
    except ValueError:
        print("+====================================================================+")
        print("|         Masukkan huruf dan angka, bukan karakter simbol.           |")
        print("+====================================================================+")
    except KeyboardInterrupt:
        ("")
    except EOFError:
        ("")

def menu_user(user):
    while True:
        clear()
        print("\n+====================================================================+")
        print("|                           Menu Pembeli                             |")
        print("+====================================================================+")
        print("| [1]. Lihat Produk                                                  |")
        print("| [2]. Lihat Saldo E-Money                                           |")
        print("| [3]. Top Up Saldo E-Money                                          |")
        print("| [4]. Transaksi Pembelian                                           |")
        print("| [5]. Cari Produk                                                   |")
        print("| [6]. Sorting Produk                                                |")
        print("| [7]. Logout                                                        |")
        print("+====================================================================+")
        try:                
            pilihan_pengguna = input("Pilihan opsi: ")
            if pilihan_pengguna == "1":
                tampilkan_produk()
                input('Tekan Enter untuk melanjutkan...')
            elif pilihan_pengguna == "2":
                lihat_saldo(user)
                input("Tekan enter untuk melanjutkan...")
            elif pilihan_pengguna == "3":
                top_up_saldo(user)
                input('Tekan Enter untuk melanjutkan...')
            elif pilihan_pengguna == "4":
                transaksi(user)
                input('Tekan Enter untuk melanjutkan...')
            elif pilihan_pengguna == "5":
                cari_produk()
                input('Tekan Enter untuk melanjutkan...')
            elif pilihan_pengguna == "6":
                urutkan_produk(user)
                input('Tekan Enter untuk melanjutkan...')
            elif pilihan_pengguna == "7":
                print("+====================================================================+")
                print("|                          Logout Berhasil!                          |")
                print("+====================================================================+")
                input('Tekan Enter untuk melanjutkan...')
                break
            else:
                print("+====================================================================+")
                print("|                        Pilihan tidak valid!                        |")
                print("+====================================================================+")
        except ValueError:
            print("+====================================================================+")
            print("|         Masukkan huruf dan angka, bukan karakter simbol.           |")
            print("+====================================================================+")
        except KeyboardInterrupt:
            ("")
        except EOFError:
            ("")

def menu_admin():
    while True:
        clear()
        print("\n+====================================================================+")
        print("|                             Menu Admin                             |")
        print("+====================================================================+")
        print("| [1]. Tampilkan Produk                                              |")
        print("| [2]. Tambah Produk                                                 |")
        print("| [3]. Perbarui Produk                                               |")
        print("| [4]. Hapus Produk                                                  |")
        print("| [5]. Cari Produk                                                   |")
        print("| [6]. Logout                                                        |")
        print("+====================================================================+")
        try:                
            pilihan_admin = input("Pilihan opsi: ")
                            
            if pilihan_admin == "1":
                tampilkan_produk()
                input('Tekan Enter untuk melanjutkan...')
            elif pilihan_admin == "2":
                tambah_produk()
                input('Tekan Enter untuk melanjutkan...')
            elif pilihan_admin == "3":
                perbarui_produk()
                input('Tekan Enter untuk melanjutkan...')
            elif pilihan_admin == "4":
                hapus_produk()
                input('Tekan Enter untuk melanjutkan...')
            elif pilihan_admin == "5":
                cari_produk()
                input('Tekan Enter untuk melanjutkan...')
            elif pilihan_admin == "6":
                print("+====================================================================+")
                print("|                          Logout Berhasil!                          |")
                print("+====================================================================+")
                input('Tekan Enter untuk melanjutkan...')
                break
            else:
                print("+====================================================================+")
                print("|                        Pilihan tidak valid!                        |")
                print("+====================================================================+")
        except ValueError:
            print("+====================================================================+")
            print("|         Masukkan huruf dan angka, bukan karakter simbol.           |")
            print("+====================================================================+")
        except KeyboardInterrupt:
            ("")
        except EOFError:
            ("")   

def main():
    inisialisasi_file()
    while True:
        clear()
        print("\n+====================================================================+")
        print("|              Selamat Datang di Sistem Toko Perhiasan               |")
        print("+====================================================================+")
        print("|                            Menu Utama                              |")
        print("+====================================================================+")
        print("| [1]. Login                                                         |")
        print("| [2]. Registrasi                                                    |")
        print("| [3]. Keluar                                                        |")
        print("+====================================================================+")
        try:
            pilihan = input("Pilih opsi: ")
            if pilihan == "1":
                login()
            elif pilihan == "2": 
                registrasi()
                input('Tekan Enter untuk melanjutkan...')
            elif pilihan == "3":
                print("+====================================================================+")
                print("|  Anda berhasil keluar. Terimakasih telah menggunakan pogram ini!   |")
                print("+====================================================================+")
                break
            else:
                print("+====================================================================+")
                print("|                       Pilihan tidak valid!                         |")
                print("+====================================================================+")
                input("Tekan enter untuk melanjutkan.....")    
        except ValueError:
            print("+====================================================================+")
            print("|         Masukkan huruf dan angka, bukan karakter simbol.           |")
            print("+====================================================================+")
        except KeyboardInterrupt:
            ("")
        except EOFError:
            ("")

main()