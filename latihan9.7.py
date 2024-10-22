#Program Pertukaran_Nilai
#nlai Variable a dan b diinput user
a = int(input("Masukkan nilai a: "))
b = int(input("Masukka nilai b: "))

#Proses Pertukaran nilai variable a dan b
a = a + b
b = a - b
a = a - b

#menampilkan hasil pertukaran nilai variable a dan b
print("Nilai a sekarang adalah:", a)
print("Nilai b sekarang adalah:", b)