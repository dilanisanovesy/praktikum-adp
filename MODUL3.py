print(" ")
nama = "Dilanisa Novesy Triananda"
nim = 2310432012
shift = 1 
print("Nama     : " + nama)
print("NIM      :",nim)
print("Shift    :",shift)
print(" ")
print("--------------------------------------")
print("TABEL PERKALIAN ATAU PENJUMLAHAN n x n")
print("--------------------------------------")
n = int(input("Input n = "))
while n < 1 or n > 10:
        n = int(input("Input n = "))

pilih = 0
while pilih !=3:
         print("MENU : ")
         print(" 1. Tabel Perkalian ", n, "x", n)
         print(" 2. Tabel Penjumlahan ", n, "x", n)
         print(" 3. Keluar")
         pilih = int(input("Pilih menu : "))

         if pilih==1:
             print("TABEL PERKALIAN", n, "x", n)
             for i in range(1, n+1):
                 for j in range(1, n+1):
                     print(i*j, end="\t")
                 print(" ")

         elif pilih==2:
             print("TABEL PENJUMLAHAN", n, "x", n)
             for i in range(1, n+1):
                for j in range(1, n+1):
                     print(i+j, end="\t")
                print(" ")

         elif pilih==3:
          print("Keluar")
         

