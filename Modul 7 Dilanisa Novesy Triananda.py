print()
nama = "Dilanisa Novesy Triananda"
nim = 2310432012
shift = "1"
print("Nama     : " + nama)
print("NIM      :",nim)
print("Shift    : " + shift)
print()
print("===============================================================================")
print("                        Program Mengelola Jadwal Harian")
print("===============================================================================")

jadwal_harian = []

# Menambahkan kegiatan
def tambah_kegiatan(waktu_mulai, waktu_selesai, deskripsi):
    kegiatan_baru = [waktu_mulai, waktu_selesai, deskripsi]
    jadwal_harian.append(kegiatan_baru)
print("Menambahkan kegiatan pada jadwal.")

# Menghapus kegiatan yang sudah ada
def hapus_kegiatan(deskripsi):
    for kegiatan in jadwal_harian:
        if kegiatan[2] == deskripsi:
            jadwal_harian.remove(kegiatan)
            print("Menghapus kegiatan pada jadwal.")
            return
    print("Kegiatan tidak ada dalam jadwal.")


# Menampilkan jadwal harian
def tampil_jadwal():
    print("Jadwal Harian :")
    for kegiatan in jadwal_harian:
        print("Waktu mulai:",kegiatan[0],",","Waktu selesai:",kegiatan[1],",","Deskripsi:",kegiatan[2])
    print()

# Memasukkan program
tambah_kegiatan("08.00", "10.00", "Meeting divisi pemasaran")
tambah_kegiatan("10:00", "12:30", "Meeting pengajuan produk")
tambah_kegiatan("12.30", "13.30", "Istirahat")
tambah_kegiatan("13.30", "16.00", "Kerja individu")
tambah_kegiatan("16.00", "18.00", "Gym")
tampil_jadwal()

hapus_kegiatan("Meeting divisi pemasaran")
tampil_jadwal()
