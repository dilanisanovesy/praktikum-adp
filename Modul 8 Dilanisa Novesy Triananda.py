nama   = 'Dilanisa Novesy Triananda'
nim    = 2310432012
shift  = '1'
print('Nama         : '+ nama)
print('NIM          : ', nim)
print('Shift        : '+ shift)
print()

data = {
    'Nama pasien' : 'Luthfina',
    'Umur pasien' : 18,
    'Jenis kelamin pasien' : 'Perempuan',
    'Golongan darah pasien' : 'O',
    'Riwayat penyakit pasien' : 'Asam Lambung',
    'Daftar obat pasien' : 'Lansoprazole'   
}

def simpan(data):
    with open("data.txt", "a") as file:
        for key, value in data.items():
            file.write(f"{value} ")
        file.write("\n")
    
def hapus(nama):
    with open("data.txt", "r") as file:
        lines = file.readlines()
        
    with open("data.txt", "w") as file:
        for line in lines:
            if nama not in line: 
                file.write(line)
    
def tampilkan():
     with open("data.txt","r") as f :
         print(f.read())

while True:
   print ("1. Simpan data pasien")
   print ("2. Hapus data pasien")
   print ("3. Tampilkan data pasien")
   print ("4. Keluar")
   pilih = input ("Pilih Menu 1/2/3/4: ")

   if pilih == "1":
       simpan(data)
       print("Berhasil menyimpan data\n")

   elif pilih == "2":
       nama = input("Masukkan nama yang ingin dihapus: ")
       hapus(nama)
       print(f"Data {nama} telah dihapus\n")

   elif pilih == "3":
      tampilkan()
      print()

   elif pilih == "4":
      break
 
   else:
      print("Masukkan menu valid\n")