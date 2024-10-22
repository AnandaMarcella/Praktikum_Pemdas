#Program Menghitung_Gaji_Bersih
#nilai variable gaji pokok dan jumlah karyawan diinput oleh user
ananda_gaji_pokok = float(input("Masukkan gaji pokok: "))
ananda_jumlah_karyawan = int(input("Masukkan jumlah karyawan: "))

#menghitung tunjangan (20% dari gaji pokok)
ananda_tunjangan = 0.2 * ananda_gaji_pokok

#menghitung pajak (10% dari gaji pokok)
ananda_pajak = 0.1 * ananda_gaji_pokok

#menghitung gaji bersih
ananda_gaji_bersih = ananda_gaji_pokok + ananda_tunjangan - ananda_pajak

#menghitung gaji total
ananda_gaji_total = ananda_gaji_bersih * ananda_jumlah_karyawan

#menampilkan hasil perhitungan
print("Gaji Karyawan")
print("Gaji Pokok                   : Rp", ananda_gaji_pokok)
print("Tunjangan                    : Rp", ananda_tunjangan)
print("Pajak                        : Rp", ananda_pajak)
print("Gaji Bersih                  : Rp", ananda_gaji_bersih)
print("GAji Total Seluruh Karyawan  : Rp", ananda_gaji_total)