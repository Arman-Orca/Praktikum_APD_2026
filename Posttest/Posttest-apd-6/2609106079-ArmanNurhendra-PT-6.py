
import os

users = {
    "arman": 
    {
        "username": "arman",
        "password": "arman079",
        "role": "admin"
    },

    "aldi": 
    {
        "username": "aldi", 
        "password": "aldi123", 
        "role": "pembeli"
    },
}

produk = [
    {"nama": "Ikan Tongkol", "harga": 35000, "stok": 50},
    {"nama": "Ikan Kembung", "harga": 40000, "stok": 40},
    {"nama": "Ikan Bandeng", "harga": 30000, "stok": 30},
    {"nama": "Ikan Kakap Merah", "harga": 75000, "stok": 20},
    {"nama": "Udang Segar", "harga": 90000, "stok": 15},
]

transaksi = {}
jalan = True

while jalan:
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 50)
    print("      SISTEM PENJUALAN IKAN SEGAR")
    print("=" * 50)
    print("1. Register")
    print("2. Login")
    print("3. Keluar")
    print("-" * 50)
    pilihan = input("Pilih menu [1-3]: ").strip()

    # ================= REGISTER =================
    if pilihan == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("=== REGISTER AKUN PEMBELI ===")
        username = input("Username baru : ").strip()
        password = input("Password baru : ").strip()
        sudah_ada = False

        for u in users.values():
            if u["username"].lower() == username.lower():
                sudah_ada = True

        if username == "" or " " in username:
            print("\n[ERROR] Username tidak boleh kosong atau mengandung spasi!")
        elif sudah_ada:
            print("\n[ERROR] Username sudah digunakan!")
        elif len(password) < 4:
            print("\n[ERROR] Password minimal 4 karakter!")
        else:
            users[username.lower()] = {
                "username": username,
                "password": password,
                "role": "pembeli"
            }
            print("\n[SUKSES] Registrasi berhasil! Silakan login.")

        input("\nTekan Enter untuk kembali...")

    # ================= LOGIN =================
    elif pilihan == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("=== LOGIN ===")
        username = input("Username : ").strip()
        password = input("Password : ").strip()
        user_aktif = None

        for u in users.values():
            if u["username"].lower() == username.lower() and u["password"] == password:
                user_aktif = u

        if user_aktif is None:
            print("\n[ERROR] Username atau password salah!")
            input("\nTekan Enter untuk kembali...")
        else:
            sesi = True
            while sesi:
                os.system("cls" if os.name == "nt" else "clear")

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
                        print("=== STOK IKAN ===")
                        print(f"{'ID':<5}{'Nama Ikan':<22}{'Harga/kg':<14}{'Stok(kg)':<10}")

                        for id_ikan, p in produk.items():
                            harga_txt = "Rp" + f"{p['harga']:,}".replace(",", ".")
                            print(f"{id_ikan:<5}{p['nama']:<22}{harga_txt:<14}{p['stok']:<10}")

                    elif menu == "2":
                        print("=== TAMBAH IKAN BARU ===")
                        nama = input("Nama ikan       : ").strip()
                        harga_in = input("Harga per kg    : ").strip()
                        stok_in = input("Stok awal (kg)  : ").strip()
                        nama_ada = False

                        for p in produk.values():
                            if p["nama"].lower() == nama.lower():
                                nama_ada = True

                        if nama == "":
                            print("\n[ERROR] Nama ikan tidak boleh kosong!")
                        elif nama_ada:
                            print("\n[ERROR] Nama ikan sudah ada di daftar!")
                        elif not harga_in.isdigit() or int(harga_in) <= 0:
                            print("\n[ERROR] Harga harus berupa angka lebih dari 0!")
                        elif not stok_in.isdigit() or int(stok_in) <= 0:
                            print("\n[ERROR] Stok harus berupa angka lebih dari 0!")
                        else:
                            id_baru = max(produk.keys(), default=0) + 1
                            produk[id_baru] = {
                                "nama": nama,
                                "harga": int(harga_in),
                                "stok": int(stok_in)
                            }
                            print("\n[SUKSES] Ikan baru berhasil ditambahkan!")

                    elif menu == "3":
                        print("=== RESTOK IKAN ===")
                        print(f"{'ID':<5}{'Nama Ikan':<22}{'Stok(kg)':<10}")

                        for id_ikan, p in produk.items():
                            print(f"{id_ikan:<5}{p['nama']:<22}{p['stok']:<10}")

                        id_in = input("\nMasukkan ID ikan : ").strip()

                        if not id_in.isdigit():
                            print("\n[ERROR] ID harus berupa angka!")
                        else:
                            terpilih = produk.get(int(id_in))

                            if terpilih is None:
                                print("\n[ERROR] ID ikan tidak ditemukan!")
                            else:
                                jumlah_in = input("Jumlah tambahan (kg) : ").strip()

                                if not jumlah_in.isdigit() or int(jumlah_in) <= 0:
                                    print("\n[ERROR] Jumlah harus angka lebih dari 0!")
                                else:
                                    terpilih["stok"] += int(jumlah_in)
                                    print("\n[SUKSES] Stok", terpilih["nama"], "sekarang", terpilih["stok"], "kg")

                    elif menu == "4":
                        print("=== SEMUA TRANSAKSI ===")

                        if len(transaksi) == 0:
                            print("Belum ada transaksi.")

                        for id_tr, t in transaksi.items():
                            print(f"\nTransaksi #{id_tr} | Pembeli: {t['pembeli']}")
                            print(f"  - {t['nama']} x {t['jumlah']} kg")
                            print("  TOTAL: Rp" + f"{t['total']:,}".replace(",", "."))

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
                        print("=== DAFTAR IKAN SEGAR ===")
                        print(f"{'ID':<5}{'Nama Ikan':<22}{'Harga/kg':<14}{'Stok(kg)':<10}")

                        for id_ikan, p in produk.items():
                            harga_txt = "Rp" + f"{p['harga']:,}".replace(",", ".")
                            print(f"{id_ikan:<5}{p['nama']:<22}{harga_txt:<14}{p['stok']:<10}")

                    elif menu == "2":
                        print("=== BELI IKAN ===")
                        print(f"{'ID':<5}{'Nama Ikan':<22}{'Harga/kg':<14}{'Stok(kg)':<10}")

                        for id_ikan, p in produk.items():
                            harga_txt = "Rp" + f"{p['harga']:,}".replace(",", ".")
                            print(f"{id_ikan:<5}{p['nama']:<22}{harga_txt:<14}{p['stok']:<10}")

                        id_in = input("\nMasukkan ID ikan : ").strip()

                        if not id_in.isdigit():
                            print("\n[ERROR] ID harus berupa angka!")
                        else:
                            terpilih = produk.get(int(id_in))

                            if terpilih is None:
                                print("\n[ERROR] ID ikan tidak ditemukan!")
                            else:
                                qty_in = input("Jumlah (kg)      : ").strip()

                                if not qty_in.isdigit() or int(qty_in) <= 0:
                                    print("\n[ERROR] Jumlah harus angka lebih dari 0!")
                                else:
                                    qty = int(qty_in)

                                    if qty > terpilih["stok"]:
                                        print("\n[ERROR] Stok tidak cukup!")
                                    else:
                                        terpilih["stok"] -= qty
                                        id_tr = max(transaksi.keys(), default=0) + 1

                                        transaksi[id_tr] = {
                                            "pembeli": user_aktif["username"],
                                            "nama": terpilih["nama"],
                                            "jumlah": qty,
                                            "total": terpilih["harga"] * qty
                                        }

                                        print("\n[SUKSES] Pembelian Berhasil!")

                    elif menu == "3":
                        print("=== RIWAYAT PEMBELIAN ===")
                        ada_riwayat = False

                        for id_tr, t in transaksi.items():
                            if t["pembeli"] == user_aktif["username"]:
                                ada_riwayat = True
                                print(f"\nTransaksi #{id_tr}")
                                print(f"  - {t['nama']} x {t['jumlah']} kg")
                                print("  TOTAL: Rp" + f"{t['total']:,}".replace(",", "."))

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
        print("\nTerima kasih telah menggunakan sistem penjualan ikan segar!")

    else:
        print("\n[ERROR] Pilihan tidak valid! Masukkan angka 1-3.")
        input("\nTekan Enter untuk kembali...")
