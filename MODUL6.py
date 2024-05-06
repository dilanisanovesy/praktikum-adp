print()
nama = "Dilanisa Novesy Triananda"
nim = 2310432012
shift = "1"
print("Nama     : " + nama)
print("NIM      :",nim)
print("Shift    : " + shift)
print()
print("==========================================================")
print("             Jadwal Penerbangan Aethers")
print("==========================================================")


jadwal = [["KOTA ASAL     "  , "     KOTA TUJUAN     ", " BERANGKAT     ", "TIBA    "],
          ["Jakarta     ", "       Jambi      ","     ", 15.45,    "        " ,       17.05],
          ["Medan       ", "       Jakarta       ", "  ", 11.45, "        ", 13.55],
          ["Yogyakarta  ", "       Banjarmasin     ", "", 10.35, "        ", 11.05],
          ["Bandung     ", "       Jakarta     ", "    ", 14.45, "        ", 15.35]]

for r in jadwal:
    for c in r:
        print(c, end= " ")
    print()
print("==========================================================")
print()
#menentukan rute tercepat antara dua kota
print("Menentukan Rute Tercepat Antara Dua Kota")
print("Pilihan Rute     :  \n1. Medan, Jakarta \n2. Jakarta, Jambi \n3. Bandung, Jakarta \n4. Yogyakarta, Banjarmasin")
pilih_a = int(input("Pilih rute pertama    : "))
pilih_b = int(input("Pilih rute kedua      : "))
pilih_1 = ["Medan","Jakarta"]
pilih_2 = ["Jakarta","Jambi"]
pilih_3 = ["Bandung","Jakarta"]
pilih_4 = ["Yogyakarta","Banjarmasin"]

if pilih_a == 1 and pilih_b == 2 :
    print("Rute tercepat antara", pilih_1, "dan", pilih_2, "adalah rute", pilih_2)
if pilih_a == 1 and pilih_b == 3 :
    print("Rute tercepat antara", pilih_1, "dan", pilih_3, "adalah rute", pilih_3)
if pilih_a == 1 and pilih_b == 4 :
    print("Rute tercepat antara", pilih_1, "dan", pilih_4, "adalah rute", pilih_4)
if pilih_a == 2 and pilih_b == 1 :
    print("Rute tercepat antara", pilih_2, "dan", pilih_1, "adalah rute", pilih_2)
if pilih_a == 2 and pilih_b == 3 :
    print("Rute tercepat antara", pilih_2, "dan", pilih_3, "adalah rute", pilih_3)
if pilih_a == 2 and pilih_b == 4 :
    print("Rute tercepat antara", pilih_2, "dan", pilih_4, "adalah rute", pilih_4)
if pilih_a == 3 and pilih_b == 1 :
    print("Rute tercepat antara", pilih_3, "dan", pilih_1, "adalah rute", pilih_3)
if pilih_a == 3 and pilih_b == 2 :
    print("Rute tercepat antara", pilih_3, "dan", pilih_2, "adalah rute", pilih_3)
if pilih_a == 3 and pilih_b == 4 :
    print("Rute tercepat antara", pilih_3, "dan", pilih_4, "adalah rute", pilih_4)
if pilih_a == 4 and pilih_b == 1 :
    print("Rute tercepat antara", pilih_4, "dan", pilih_1, "adalah rute", pilih_4)
if pilih_a == 4 and pilih_b == 2 :
    print("Rute tercepat antara", pilih_4, "dan", pilih_2, "adalah rute", pilih_4)
if pilih_a == 4 and pilih_b == 3 :
    print("Rute tercepat antara", pilih_4, "dan", pilih_3, "adalah rute", pilih_4)

              