#Program Luas_Keliling_JajaranGenjang
#variable alas, tinggi, dan panjang sisi miring diinput oleh user
a = float(input("Masukkan panjang alas: "))
t = float(input("Masukkan tinggi: "))
s = float(input("Masukkan panjan sisi miring: "))

#proses menghitung luas dan keliling jajaran genjang
ananda_luas = a * t
ananda_keliling = 2 * (a + s)

#menampilkan hasil perhitungan 
print("Luas jajaran genjang adalah:", ananda_luas)
print("Keliling jajaran genjang adalah:", ananda_keliling)