print()
nama = "Dilanisa Novesy Triananda"
nim = 2310432012
shift = "1"
print("Nama     : " + nama)
print("NIM      :",nim)
print("Shift    : " + shift)
print()
print("==============================================================")
print("Program Menentukan Bilangan Sempurna dan Bilangan Genap/Ganjil")
print("==============================================================")
n = int(input("Masukkan angka: "))
print("Apakah angka tersebut merupakan bilangan sempurna?")
jumlah_variabel = 0
for i in range(1,n):
    if n % i == 0:
        jumlah_variabel += i
if jumlah_variabel == n:
     print(f"\n{n} adalah bilangan sempurna")
else:
    print(f"\n{n} bukan bilangan sempurna")
print(" ")
print("Angka tersebut merupakan bilangan genap atau ganjil?")
if n % 2 == 0:
    print(f"{n} adalah bilangan genap\n")
else : 
    print(f"{n} adalah bilangan ganjil\n")


