#Program Biaya_Sewa
#nilai variable jarak diinput user
jarak = int(input("Masukkan jarak tempuh (km): "))

#proses menghitung biaya sewa
if jarak <= 1:
    ananda_biaya = 4500
else:
    ananda_biaya = 4500 + (jarak - 1) * 2000

#menampikan harga sewa hasil perhitungan
print("Biaya sewa: Rp.", ananda_biaya)