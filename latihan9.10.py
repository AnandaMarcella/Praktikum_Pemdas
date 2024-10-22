#Program Data_dan_StatusKelulusan_Mahasiswa
#Input nilai variable nama dan NIM oleh user
ananda_mahasiswa = input("Masukkan nama mahasiswa: ")
ananda_nim = input("Masukkan NIM mahasiswa: ")

# inisialisasi variabel untuk IPS
ananda_ips = 0

#Input nilai mutu mata kuliah
AMPA = int(input("Masukkan angka mutu Pendidikan Agama: "))
AMPP = int(input("Masukkan angka mutu Pendidikan Pancasila: "))
AMBI1 = int(input("Masukkan angka mutu Bahasa Inggris 1: "))
AMPDI = int(input("Masukkan angka mutu Pengolahan Data dan Informasi: "))
AMPTIK = int(input("Masukkan angka mutu Pengantar Teknologi Informasi dan Komunikasi: "))
AMMD = int(input("Masukkan angka mutu Matematika Diskrit: "))
AMPD1 = int(input("Masukkan angka mutu Pemrograman Dasar: "))

#Proses menghitung nilai
ananda_ips = (((AMPA * 2) + (AMPP * 2) + (AMBI1 * 2) + (AMPDI * 3) + (AMPTIK * 4) + (AMMD * 3) + (AMPD1 * 4)) / 20)

#Proses menentukan status kelulusan
if ananda_ips > 2.75:
  ananda_status_kelulusan = "Tetap"
elif ananda_ips > 2.00:
  ananda_status_kelulusan = "Percobaan"
else:
  ananda_status_kelulusan = "Tidak Lulus"

#Menampilkan hasil input dan proses serta penentuan status kelulusan
print("Nama Mahasiswa: ", ananda_mahasiswa)
print("NIM: ", ananda_nim)
print("IPS: ", ananda_ips)
print("Status Kelulusan: ", ananda_status_kelulusan)