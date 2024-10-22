#Program status_nilai
#I.S: Nilai diinput oleh user
#F.S: Menampilan status nilai berupa huruf

nilai=int(input("Masukkan nilai: "))

def status_nilai(nilai):
    match nilai:
        case 95:
            return "A"
        case 80:
            return "B"
        case 75:
            return "C"
        case 70:
            return "D"
        case 65:
            return "E"
        case _:
            return "status nilai tidak tersedia!"
keterangan=status_nilai(nilai)
print(keterangan)