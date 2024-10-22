#Program_nilai_terkecil

#I.S: suatu bilangan diinput oleh user
#F.S: menampilkan statement bilangan terkecil dai tiga bilangan

a = int(input("masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))

if a<b and a<c:
    print("Bilangan terkecil adalah: ",a)
else:
    if b<a and b<c:
        print("Bilangan terkecil adalah: ",b)
    else:
        c<a and c<b
        print("Bilangan terkecil adalah: ",c)