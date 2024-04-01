print()
nama = "Dilanisa Novesy Triananda"
nim = 2310432012
shift = "1"
print("Nama     : " + nama)
print("NIM      :",nim)
print("Shift    : " + shift)
print()
print("===============================")
print("Program Mencetak Segitiga Angka")
print("===============================")
tinggi = int(input("Masukkan tinggi segitiga: "))
if not isinstance(tinggi,int) or tinggi <=0:
    print("\nTinggi harus bilangan bulat positif. Silahkan ulang kembali.\n")
for i in range(1, tinggi + 1):
    for j in range(1, i + 1):
        print(j,' ',end='',sep='')
    print()
