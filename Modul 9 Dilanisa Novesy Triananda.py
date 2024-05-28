import os
os.system('cls')
nama = "Dilanisa Novesy Triananda"
nim = 2310432012
shift = "1"
print("Nama     : " + nama)
print("NIM      :",nim)
print("Shift    : " + shift)
print()
import os
from termcolor import colored, cprint

cprint("Program Membuat Bendera Merah Putih", "red", "on_white")
print()

for i in range(5):
    cprint("  "*1, "dark_grey", "on_dark_grey", end="")
    cprint("  "*15, "red", "on_red", end="")
    print()

for j in range(5):
    cprint("  "*1, "dark_grey", "on_dark_grey", end="")
    cprint("  "*15, "white", "on_white", end="")
    print()

for k in range(10):
    cprint("  "*1, "dark_grey", "on_dark_grey", end=" ")
    print()

print()