nama_game = ["genshin impact", "minecraft", "mobile legend"]
kategori_topup = ["kecil", "menengah", "besar"]
metode_pembayaran = ["pulsa", "e-wallet"]

username = input("masukkan username :")
password = input("masukkan password :") 

if username == "arman" and password == "79" :
    print("Login Berhasil")

    print("")
    id_player = input("masukkan id player :")

    print("")
    for index, game in enumerate(nama_game) :
        print(index+1, game)
    id_game = int(input("masukkan id game : "))
    game = nama_game[id_game-1]
    
    print("")
    for index, kategori in enumerate(kategori_topup) :
        print(index+1, kategori)
    id_kategori = int(input("masukkan id kategori : "))
    kategori = kategori_topup[id_kategori-1]

    print("")
    for index, metode in enumerate(metode_pembayaran) :
        print(index+1, metode)
    id_metode_pembayaran = int(input("masukkan id metode pembayaran : "))
    metode = metode_pembayaran[id_metode_pembayaran-1]

    biaya = 0
    if kategori == "kecil" :
        biaya = 15000
    elif kategori == "menengah" :
        biaya = 50000
    elif kategori == "besar" :
        biaya = 150000

    admin = 2500 if metode == "pulsa" else 500
    total_biaya = biaya + admin
    print("total biaya :", total_biaya)
    jumlah_bayar = int(input("masukkan jumlah bayar : "))
    if jumlah_bayar >= total_biaya :
        kembalian = jumlah_bayar - total_biaya
        
        print("")
        print("=============transaksi=============")
        print("username          :", username)
        print("id_player         :", id_player)
        print("game              :", game)
        print("kategori          :", kategori)
        print("metode_pembayaran :", metode)
        print("jumlah bayar      :", jumlah_bayar)
        print("total_biaya       :", total_biaya)
        print("kembalian         :", kembalian)
        print("===================================")

    else :
        print("Transaksi Gagal Saldo Anda Tidak Mencukupi")
else:
    print("Login Gagal")
