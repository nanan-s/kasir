# code by m.ginanjar 

menu = {
    "coklat": 20000,
    "indomi": 3500,
    "susu": 7500,
}
print("=================== Daftar menu ====================")
for g in menu:
    print("Daftar menu", g, "\t Harga", menu[g])
print("Jika pembelian > 100000")
print("- mendapatkan diskon 5%, dan bonus 1lt minyak")
print("Jika pembelian < 100000")
print("- mendapatkan diskon 2%, dan bonus 1 bungkus kopi")
print("===================================================")

beli = []
jumlah = []
subtotal = 0  

while True:
    beli2 = input("Pilih menu : ")
    jumlah2 = int(input("jumlah yang di beli : "))
    harga_item = menu[beli2]
    bayar = jumlah2 * harga_item
    lanjut = input("lanjut belanja? [y/t] : ")
    beli.append(beli2)
    jumlah.append(jumlah2)

    subtotal += bayar 

    if lanjut == "t":
        print("baiklah")
        break

if subtotal > 100000:
    diskon = subtotal * 5 / 100
    total = subtotal - diskon
elif subtotal < 100000:
    diskon = subtotal * 2 / 100
    total = subtotal - diskon
else:
    total = subtotal

uang = int(input("uang yang dapat di bayar ? "))
kembalian = uang - total

print("================== Detail Pembelian ===================")
print("Menu yang ingin di beli   : ", beli)
print("Jumlah yang ingin di beli : ", jumlah)
print("Uang yang anda bayar      : ", uang)
print("Subtotal pembayaran       : ", subtotal)
print("Total yang harus di bayar : ", total)
print("Uang kembalian            : ", kembalian)
print("======================================================")
