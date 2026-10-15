import os

users = [
    ["arman", "arman079", "admin"],
    ["aldi", "aldi123", "pembeli"],
]

produk = [
    [1, "Ikan Tongkol", 35000, 50],
    [2, "Ikan Kembung", 40000, 40],
    [3, "Ikan Bandeng", 30000, 30],
    [4, "Ikan Kakap Merah", 75000, 20],
    [5, "Udang Segar", 90000, 15],
]

transaksi = []

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
        for u in users:
            if u[0].lower() == username.lower():
                sudah_ada = True

        if username == "" or " " in username:
            print("\n[ERROR] Username tidak boleh kosong atau mengandung spasi!")
        elif sudah_ada:
            print("\n[ERROR] Username sudah digunakan!")
        elif len(password) < 4:
            print("\n[ERROR] Password minimal 4 karakter!")
        else:
            users.append([username, password, "pembeli"])
            print("\n[SUKSES] Registrasi berhasil! Silakan login.")
        input("\nTekan Enter untuk kembali...")

    # ================= LOGIN =================
    elif pilihan == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("=== LOGIN ===")
        username = input("Username : ").strip()
        password = input("Password : ").strip()

        user_aktif = None
        for u in users:
            if u[0].lower() == username.lower() and u[1] == password:
                user_aktif = u

        if user_aktif is None:
            print("\n[ERROR] Username atau password salah!")
            input("\nTekan Enter untuk kembali...")
        else:
            sesi = True
            while sesi:
                os.system("cls" if os.name == "nt" else "clear")

                # ---------- MENU ADMIN ----------
                if user_aktif[2] == "admin":
                    print("=" * 50)
                    print("  MENU ADMIN  |  Login sebagai:", user_aktif[0])
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
                        for p in produk:
                            harga_txt = "Rp" + f"{p[2]:,}".replace(",", ".")
                            print(f"{p[0]:<5}{p[1]:<22}{harga_txt:<14}{p[3]:<10}")

                    elif menu == "2":
                        print("=== TAMBAH IKAN BARU ===")
                        nama = input("Nama ikan       : ").strip()
                        harga_in = input("Harga per kg    : ").strip()
                        stok_in = input("Stok awal (kg)  : ").strip()

                        nama_ada = False
                        for p in produk:
                            if p[1].lower() == nama.lower():
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
                            id_baru = produk[-1][0] + 1
                            produk.append([id_baru, nama, int(harga_in), int(stok_in)])
                            print("\n[SUKSES] Ikan baru berhasil ditambahkan!")

                    elif menu == "3":
                        print("=== RESTOK IKAN ===")
                        print(f"{'ID':<5}{'Nama Ikan':<22}{'Stok(kg)':<10}")
                        for p in produk:
                            print(f"{p[0]:<5}{p[1]:<22}{p[3]:<10}")
                        id_in = input("\nMasukkan ID ikan : ").strip()

                        if not id_in.isdigit():
                            print("\n[ERROR] ID harus berupa angka!")
                        else:
                            terpilih = None
                            for p in produk:
                                if p[0] == int(id_in):
                                    terpilih = p
                            if terpilih is None:
                                print("\n[ERROR] ID ikan tidak ditemukan!")
                            else:
                                jumlah_in = input("Jumlah tambahan (kg) : ").strip()
                                if not jumlah_in.isdigit() or int(jumlah_in) <= 0:
                                    print("\n[ERROR] Jumlah harus angka lebih dari 0!")
                                else:
                                    terpilih[3] += int(jumlah_in)
                                    print("\n[SUKSES] Stok", terpilih[1], "sekarang", terpilih[3], "kg")

                    elif menu == "4":
                        print("=== SEMUA TRANSAKSI ===")
                        if len(transaksi) == 0:
                            print("Belum ada transaksi.")
                        for t in transaksi:
                            print(f"\nTransaksi #{t[0]} | Pembeli: {t[1]}")
                            print(f"  - {t[2]} x {t[3]} kg")
                            print("  TOTAL: Rp" + f"{t[4]:,}".replace(",", "."))

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
                    print("  MENU PEMBELI  |  Login sebagai:", user_aktif[0])
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
                        for p in produk:
                            harga_txt = "Rp" + f"{p[2]:,}".replace(",", ".")
                            print(f"{p[0]:<5}{p[1]:<22}{harga_txt:<14}{p[3]:<10}")

                    elif menu == "2":
                        print("=== BELI IKAN ===")
                        print(f"{'ID':<5}{'Nama Ikan':<22}{'Harga/kg':<14}{'Stok(kg)':<10}")
                        for p in produk:
                            harga_txt = "Rp" + f"{p[2]:,}".replace(",", ".")
                            print(f"{p[0]:<5}{p[1]:<22}{harga_txt:<14}{p[3]:<10}")
                        id_in = input("\nMasukkan ID ikan : ").strip()

                        if not id_in.isdigit():
                            print("\n[ERROR] ID harus berupa angka!")
                        else:
                            terpilih = None
                            for p in produk:
                                if p[0] == int(id_in):
                                    terpilih = p
                            if terpilih is None:
                                print("\n[ERROR] ID ikan tidak ditemukan!")
                            else:
                                qty_in = input("Jumlah (kg)      : ").strip()
                                if not qty_in.isdigit() or int(qty_in) <= 0:
                                    print("\n[ERROR] Jumlah harus angka lebih dari 0!")
                                else:
                                    qty = int(qty_in)
                                    if qty > terpilih[3]:
                                        print("\n[ERROR] Stok tidak cukup!")
                                    else:
                                        terpilih[3] -= qty
                                        transaksi.append([len(transaksi) + 1, user_aktif[0], terpilih[1], qty, terpilih[2] * qty])
                                        print("\n[SUKSES] Pembelian Berhasil!")

                    elif menu == "3":
                        print("=== RIWAYAT PEMBELIAN ===")
                        ada_riwayat = False
                        for t in transaksi:
                            if t[1] == user_aktif[0]:
                                ada_riwayat = True
                                print(f"\nTransaksi #{t[0]}")
                                print(f"  - {t[2]} x {t[3]} kg")
                                print("  TOTAL: Rp" + f"{t[4]:,}".replace(",", "."))
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
