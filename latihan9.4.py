#Program Data_Mahasiswa
#input variable data mahasiswa pertama
ananda_nama1 = "Ananda"
ananda_umur1 = 19
ananda_program_studi1 = "Sistem Informasi"
ananda_jenis_kelamin1 = "Perempuan"
ananda_tinggi1 = 156
ananda_kelas1 = "SI-1A"
ananda_lulus1 = False

#input variable data mahasiswa kedua
ananda_nama2 = "Marcella"
ananda_umur2 = 20
ananda_program_studi2 = "Sistem Informasi"
ananda_jenis_kelamin2 = "Laki-laki"
ananda_tinggi2 = 170
ananda_kelas2 = "SI-1A"
ananda_lulus2 = True

#menampilkan data mahasiswa pertama
print("Nama:", ananda_nama1)
print("Umur:", ananda_umur1, "tahun")
print("Tinggi Badan:", ananda_tinggi1)
print("Program Studi:", ananda_program_studi1)
print("Kelas:", ananda_kelas1)
print("Jenis Kelamin:", ananda_jenis_kelamin1)

#proses menentukan status mahasiswa
if ananda_lulus1:
    print("Satus: Alumni")
else:
    print("Status: Mahasiswa aktif")

#menampilkan data mahasiswa kedua
print("Nama:", ananda_nama2)
print("Umur:", ananda_umur2, "tahun")
print("Tinggi Badan:", ananda_tinggi2)
print("Program Studi:", ananda_program_studi2)
print("Kelas:", ananda_kelas2)
print("Jenis Kelamin:", ananda_jenis_kelamin2)

#proses menentukan status mahasiuswa
if ananda_lulus2:
    print("Satus: Alumni")
else:
    print("Status: Mahasiswa aktif")