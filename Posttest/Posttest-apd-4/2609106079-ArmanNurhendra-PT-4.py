percobaan = 0
saldo = 700000
username = "leaf"
password = "079"

while True:
    username_input = str(input("masukan username :"))
    password_input = str(input("masukan password :"))

    if username_input == username and password_input == password:
        print("login berhasil")
        while True:
            print("======= Pilihan Menu=====")
            print("1. Cek Saldo")
            print("2. Tarik Tunai")
            print("3. Setor Tunai")
            print("4. Keluar")
            menu = int(input("Masukan Pilihan Menu Anda :"))

            if menu == 1:
                print(f"Saldo Anda Tersisa : Rp.{saldo}\n")
                
            elif menu == 2:
                kelipatan = int(input("masukan kelipatan Rp.(50000 / 100000) : "))
                if kelipatan != 50000 and kelipatan != 100000:
                    print("Nominal harus kelipatan Rp. 50.000 atau Rp. 100.000\n")
                else:
                    nominal_tarik = int(input("masukan nominal yang ingin di tarik : "))
                    if nominal_tarik % kelipatan != 0:
                        print("Nominal harus kelipatan Rp. 50.000 atau Rp. 100.000\n")
                    elif nominal_tarik <= saldo:
                        saldo -= nominal_tarik
                        print("Tarik tunai berhasil")
                        print(f"Saldo anda menjadi: Rp.{saldo}\n")
                    else:
                        print("Saldo anda tidak mencukupi\n")

            elif menu == 3:
                kelipatan = int(input("masukan kelipatan Rp.(50000 / 100000) :"))
                if kelipatan != 50000 and kelipatan != 100000:
                    print("Nominal harus kelipatan Rp. 50.000 atau Rp. 100.000\n")
                else:
                    nominal_setor = int(input("masukan nominal yang ingin di setor : "))
                    if nominal_setor % kelipatan != 0:
                        print("Nominal harus kelipatan Rp. 50.000 atau Rp. 100.000\n")
                    else:
                        saldo += nominal_setor
                        print("Setor tunai berhasil")
                        print(f"Saldo anda menjadi: Rp.{saldo}\n")

            elif menu == 4:
                print("Terima kasih sudah menggunakan layanan kami\n")
                break

            else :
                print("Pilihan Menu Tidak Tersedia\n")
        break
    else:
        print("login gagal")
        percobaan += 1
        print(f"anda gagal login sebanyak {percobaan} kali")
        if percobaan >= 3:
            print("akun terblokir")
            break
