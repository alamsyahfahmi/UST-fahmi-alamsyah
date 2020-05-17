handphone = [
"{0.iphone 8 , harga : Rp. 4.350.000}",
"{1.iphone x , harga : Rp. 5.400.000}", 
"{2.iphone 11 , harga : Rp. 15.000.000 }"]
a=int(input("silahlakan pilih menu, tekan 1 jika ingin ke menu pembelian, dan tekan 2 jika ingin ke menu admin :"))
if a == 1:
    print("selamat datang pada aplikasi penjualan handphone pada toko kami")
    print("---------------------------------------------------------------")
    b = input("apakah anda mau membeli handphone, jika  ya / tidak ? :")
    if b in ["ya", "YA", "Ya"]:
        print("ini adalah beberapa jenis handphone di toko kami :")
        print("--------------------------------------------------")
        for x in handphone:
            print(x)
        pilih = int(input("masukan nomor handphone di atas :"))
        if pilih == 0:
            harga = 4350000
            print("handphone yang anda beli : \n",handphone[0])
            print("----------------------------------------------")
            tanya =str(input("apakah masih beli handphone, jika masi masukan nomor handphone, jika tidak, tuliskan tidak :"))
            if tanya == "1":
                harga = 9750000
                jum = 2
                print("-------------------------------------------")
                print("di batasi pembelian handphone maxsimal dua handphone ")
                print("handphone yang anda beli :",handphone[0],handphone[1])
                print("Total pembelian : Rp. 9.750.000")
                print("-------------------------------------------")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran : Rp.", harga)
                print("kembalian : Rp.", kembali)
            elif tanya == "2":
                harga = 19350000
                jum = 2
                print("-------------------------------------------")
                print("di batasi pembelian handphone maxsimal dua handphone ")
                print("handphone yang anda beli :",handphone[0],handphone[2])
                print("Total pembelian : Rp. 19.350.000")
                print("-------------------------------------------")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "tidak":
                harga = 4350000
                jum = 1
                print("------------------------------------------")
                print("handphone yang anda beli :",handphone[0])
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)  
        elif pilih == 1:
            harga = 5400000
            print("handphone yang anda beli : \n",handphone[1])
            print("-----------------------------------------------")
            tanya =str(input("apakah masih beli handphone, jika masih masukan nomor handphone, jika tidak, tuliskan tidak :"))
            if tanya == "2":
                harga = 20400000
                jum = 2
                print("-------------------------------------------")
                print("di batasi pembelian handphone maxsimal dua handphone ")
                print("handphone yang anda beli :",handphone[1],handphone[2])
                print("Total pembelian : Rp. 20.400.000")
                print("-------------------------------------------")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "0":
                harga = 9750000
                jum = 2
                print("-------------------------------------------")
                print("di batasi pembelian handphone maxsimal dua handphone ")
                print("handphone yang anda beli :",handphone[1],handphone[0])
                print("Total pembelian : Rp. 9.750.000")
                print("-------------------------------------------")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "tidak":
                harga = 5400000
                jum = 1
                print("-----------------------------------------")
                print("handphone yang anda beli :",handphone[1])
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
        elif pilih == 2:
            harga = 15000000
            print("handphone yang anda beli : \n",handphone[2])
            print("----------------------------------------------")
            tanya =str(input("apakah masih beli handphone, jika masih masukan n0mor handphone, jika tidak, tuliskan tidak :"))
            if  tanya == "0":
                harga = 19350000
                jum = 2
                print("-------------------------------------------")
                print("di batasi pembelian handphone maxsimal dua handphone ")
                print("handphone yang anda beli :",handphone[2],handphone[0])
                print("Total pembelian : Rp. 19.350.000")
                print("-------------------------------------------")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "1":
                harga = 20400000
                jum = 2
                print("============================================")
                print("di batasi pembelian handphone maxsimal dua handphone ")
                print("handphone yang anda beli :",handphone[2],handphone[1])
                print("Total pembelian : Rp. 20.400.000")
                print("----------------------------------------------")
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            elif tanya == "tidak":
                harga = 15000000
                jum = 1
                print("------------------------------------------------")
                print("handphone yang anda beli :",handphone[2])
                bayar = int(input("pembayaran :"))
                kembali = bayar - harga
                print("total pembeli :", jum)
                print("pembayaran :", harga)
                print("kembalian :", kembali)
            else:
                print("nomor yang anda masukan salah")
        else:
            print("angka yang anda masukan tidak tercantum dalah nomor handphone")
            print("silahkan mulai kembali!")
elif a == 2:
    print("selamat datang admin pada aplikasi penjualan handphone  pada Toko sejahtra")
    print("--------------------------------------------------------------------")
    print("stok handphone")
    print(handphone)
    print("-------------------------------------------------------------------")
    print("jikan menambah tekan 1, dan jika menghapus tekan 2")
    pilih = int(input("masukan pilihan :"))
    if pilih == 1:
        print("anda menambahkan stok handphone, dengan format ikuti di bawah ini")
        print("{nomor selanjutnya. nama handphone, harga : diisi}")
        stok = str(input("masukan stok : "))
        handphone.append(stok)
        print(handphone)
    elif pilih == 2:
        print("anda ingin menghapus stok yang telah habis ? ")
        print("pililah nomor handphone yang ingin anda hapus")
        stok = int(input ("masukan nomor :"))
        del handphone[stok]
        print(handphone)