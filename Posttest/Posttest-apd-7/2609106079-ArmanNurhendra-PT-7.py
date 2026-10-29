import os

NAMA_TOKO = "SISTEM PENJUALAN IKAN SEGAR"      
MIN_PASSWORD = 4                                

users = {                                       
    "arman": {"username": "arman", "password": "arman079", "role": "admin"},
    "aldi": {"username": "aldi", "password": "aldi123", "role": "pembeli"},
}

produk = {                                      
    1: {"nama": "Ikan Tongkol", "harga": 35000, "stok": 50},
    2: {"nama": "Ikan Kembung", "harga": 40000, "stok": 40},
    3: {"nama": "Ikan Bandeng", "harga": 30000, "stok": 30},
    4: {"nama": "Ikan Kakap Merah", "harga": 75000, "stok": 20},
    5: {"nama": "Udang Segar", "harga": 90000, "stok": 15},
}

transaksi = {}
id_transaksi_terakhir = 0                       
jalan = True                                    

class InputTidakValid(Exception):
    pass

def buat_id_transaksi():
    global id_transaksi_terakhir
    id_transaksi_terakhir += 1
    return id_transaksi_terakhir


def hitung_total_pendapatan():
    total_semua = 0
    for t in transaksi.values():
        total_semua += t["total"]
    return total_semua

def format_rupiah(angka):
    teks = f"{angka:,}".replace(",", ".")        
    return "Rp" + teks


def baca_angka_positif(pesan):
    teks = input(pesan).strip()
    try:
        nilai = int(teks)
        if nilai <= 0:
            raise InputTidakValid("Angka harus lebih dari 0!")
    except ValueError:
        print("\n[ERROR] Input harus berupa angka bulat!")
        return None
    except InputTidakValid as e:
        print(f"\n[ERROR] {e}")
        return None
    else:
        return nilai


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def tampilkan_daftar_ikan(judul, tampil_harga=True):
    print(f"=== {judul} ===")
    if tampil_harga:
        print(f"{'ID':<5}{'Nama Ikan':<22}{'Harga/kg':<14}{'Stok(kg)':<10}")
    else:
        print(f"{'ID':<5}{'Nama Ikan':<22}{'Stok(kg)':<10}")

    for id_ikan, p in produk.items():
        if tampil_harga:
            print(f"{id_ikan:<5}{p['nama']:<22}{format_rupiah(p['harga']):<14}{p['stok']:<10}")
        else:
            print(f"{id_ikan:<5}{p['nama']:<22}{p['stok']:<10}")

try:
    while jalan:
        bersihkan_layar()
        print("=" * 50)
        print("      " + NAMA_TOKO)
        print("=" * 50)
        print("1. Register")
        print("2. Login")
        print("3. Keluar")
        print("-" * 50)
        pilihan = input("Pilih menu [1-3]: ").strip()

        # ================= REGISTER =================
        if pilihan == "1":
            bersihkan_layar()
            print("=== REGISTER AKUN PEMBELI ===")
            username = input("Username baru : ").strip()
            password = input("Password baru : ").strip()

            try:
                if username == "" or " " in username:
                    raise InputTidakValid("Username tidak boleh kosong atau mengandung spasi!")
                if username.lower() in users:
                    raise InputTidakValid("Username sudah digunakan!")
                if len(password) < MIN_PASSWORD:
                    raise InputTidakValid(f"Password minimal {MIN_PASSWORD} karakter!")
            except InputTidakValid as e:
                print(f"\n[ERROR] {e}")
            else:
                users[username.lower()] = {
                    "username": username,
                    "password": password,
                    "role": "pembeli",
                }
                print("\n[SUKSES] Registrasi berhasil! Silakan login.")
            finally:
                input("\nTekan Enter untuk kembali...")

        # ================= LOGIN =================
        elif pilihan == "2":
            bersihkan_layar()
            print("=== LOGIN ===")
            username = input("Username : ").strip()
            password = input("Password : ").strip()

            try:
                user_aktif = users[username.lower()]
                if user_aktif["password"] != password:
                    raise InputTidakValid("Password salah!")
            except KeyError:
                print("\n[ERROR] Username tidak ditemukan!")
                input("\nTekan Enter untuk kembali...")
                continue
            except InputTidakValid as e:
                print(f"\n[ERROR] {e}")
                input("\nTekan Enter untuk kembali...")
                continue

            sesi = True
            while sesi:
                bersihkan_layar()

                # ---------- MENU ADMIN ----------
                if user_aktif["role"] == "admin":
                    print("=" * 50)
                    print("  MENU ADMIN  |  Login sebagai:", user_aktif["username"])
                    print("=" * 50)
                    print("1. Lihat stok ikan")
                    print("2. Tambah ikan baru")
                    print("3. Restok ikan")
                    print("4. Lihat semua transaksi")
                    print("0. Logout")
                    print("-" * 50)
                    menu = input("Pilih menu [0-4]: ").strip()
                    print()

                    if menu == "1":
                        tampilkan_daftar_ikan("STOK IKAN")

                    elif menu == "2":
                        print("=== TAMBAH IKAN BARU ===")
                        nama = input("Nama ikan       : ").strip()

                        try:
                            if nama == "":
                                raise InputTidakValid("Nama ikan tidak boleh kosong!")
                            for p in produk.values():
                                if p["nama"].lower() == nama.lower():
                                    raise InputTidakValid("Nama ikan sudah ada di daftar!")
                        except InputTidakValid as e:
                            print(f"\n[ERROR] {e}")
                        else:
                            harga_baru = baca_angka_positif("Harga per kg    : ")
                            if harga_baru is not None:
                                stok_baru = baca_angka_positif("Stok awal (kg)  : ")
                                if stok_baru is not None:
                                    id_baru = max(produk.keys(), default=0) + 1
                                    produk[id_baru] = {
                                        "nama": nama,
                                        "harga": harga_baru,
                                        "stok": stok_baru,
                                    }
                                    print("\n[SUKSES] Ikan baru berhasil ditambahkan!")

                    elif menu == "3":
                        tampilkan_daftar_ikan("RESTOK IKAN", tampil_harga=False)
                        id_in = baca_angka_positif("\nMasukkan ID ikan : ")

                        if id_in is not None:
                            try:
                                terpilih = produk[id_in]
                            except KeyError:
                                print("\n[ERROR] ID ikan tidak ditemukan!")
                            else:
                                tambahan = baca_angka_positif("Jumlah tambahan (kg) : ")
                                if tambahan is not None:
                                    terpilih["stok"] += tambahan
                                    print("\n[SUKSES] Stok", terpilih["nama"],
                                          "sekarang", terpilih["stok"], "kg")

                    elif menu == "4":
                        print("=== SEMUA TRANSAKSI ===")

                        if len(transaksi) == 0:
                            print("Belum ada transaksi.")

                        for id_tr, t in transaksi.items():
                            print(f"\nTransaksi #{id_tr} | Pembeli: {t['pembeli']}")
                            print(f"  - {t['nama']} x {t['jumlah']} kg")
                            print("  TOTAL:", format_rupiah(t["total"]))

                        if len(transaksi) > 0:
                            print("\nTotal pendapatan:", format_rupiah(hitung_total_pendapatan()))

                    elif menu == "0":
                        sesi = False
                        print("Logout berhasil.")

                    else:
                        print("[ERROR] Pilihan tidak valid! Masukkan angka 0-4.")

                    if menu != "0":
                        input("\nTekan Enter untuk kembali ke menu admin...")

                # ---------- MENU PEMBELI ----------
                else:
                    print("=" * 50)
                    print("  MENU PEMBELI  |  Login sebagai:", user_aktif["username"])
                    print("=" * 50)
                    print("1. Lihat daftar ikan")
                    print("2. Beli Ikan")
                    print("3. Riwayat pembelian")
                    print("0. Logout")
                    print("-" * 50)
                    menu = input("Pilih menu [0-3]: ").strip()
                    print()

                    if menu == "1":
                        tampilkan_daftar_ikan("DAFTAR IKAN SEGAR")

                    elif menu == "2":
                        tampilkan_daftar_ikan("BELI IKAN")
                        id_in = baca_angka_positif("\nMasukkan ID ikan : ")

                        if id_in is not None:
                            try:
                                terpilih = produk[id_in]
                            except KeyError:
                                print("\n[ERROR] ID ikan tidak ditemukan!")
                            else:
                                qty = baca_angka_positif("Jumlah (kg)      : ")

                                if qty is not None:
                                    try:
                                        if qty > terpilih["stok"]:
                                            raise InputTidakValid("Stok tidak cukup!")
                                    except InputTidakValid as e:
                                        print(f"\n[ERROR] {e}")
                                    else:
                                        terpilih["stok"] -= qty
                                        id_tr = buat_id_transaksi()
                                        transaksi[id_tr] = {
                                            "pembeli": user_aktif["username"],
                                            "nama": terpilih["nama"],
                                            "jumlah": qty,
                                            "total": terpilih["harga"] * qty,
                                        }
                                        print("\n[SUKSES] Pembelian Berhasil!")
                                        print("Total bayar:", format_rupiah(transaksi[id_tr]["total"]))

                    elif menu == "3":
                        print("=== RIWAYAT PEMBELIAN ===")
                        ada_riwayat = False

                        for id_tr, t in transaksi.items():
                            if t["pembeli"] == user_aktif["username"]:
                                ada_riwayat = True
                                print(f"\nTransaksi #{id_tr}")
                                print(f"  - {t['nama']} x {t['jumlah']} kg")
                                print("  TOTAL:", format_rupiah(t["total"]))

                        if not ada_riwayat:
                            print("Belum ada riwayat pembelian.")

                    elif menu == "0":
                        sesi = False
                        print("Logout berhasil.")

                    else:
                        print("[ERROR] Pilihan tidak valid! Masukkan angka 0-3.")

                    if menu != "0":
                        input("\nTekan Enter untuk kembali ke menu pembeli...")

        # ================= KELUAR =================
        elif pilihan == "3":
            jalan = False

        else:
            print("\n[ERROR] Pilihan tidak valid! Masukkan angka 1-3.")
            input("\nTekan Enter untuk kembali...")

except (KeyboardInterrupt, EOFError):
    print("\n\n[INFO] Program dihentikan paksa oleh pengguna.")

finally:
    print("\nTerima kasih telah menggunakan sistem penjualan ikan segar!")