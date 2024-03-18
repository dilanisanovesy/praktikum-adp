print(' ')
nama = 'Dilanisa Novesy Triananda'
nim = 2310432012
shift = '1'
print('Nama     : '+ nama)
print('NIM      :', nim)
print('Shift    : ' + shift)
print(' ')
print('=========================================')
print('        WELCOME TO WARMINDO BUENO        ')
print('=========================================')
print('''Jenis Pesanan :
       1. Makanan
       2. Minuman
       3. Makanan dan Minuman''')
pesan = int(input('Pilih jenis pesanan : '))
print('Menu yang tersedia : ')
if pesan==1:
    print("""    ================MENU MAKANAN=============
    -----------------------------------------
    | KODE |   NAMA MAKANAN   |    HARGA    |
    -----------------------------------------
    |  1  | INDOMIE BIASA     | Rp. 7.000   |
    |  2  | INDOMIE TELUR     | Rp. 10.000  |                        
    |  3  | INDOMIE CARBONARA | Rp. 15.000  |
    |  4  | INDOMIE KORNET    | Rp. 15.000  |
    -----------------------------------------         """)
    
    kode = int(input('Kode menu : '))
    jumlah = int(input('Jumlah pesanan : '))
    
    if kode==1:
      harga = int(7000*jumlah)
      print('Total harga : Rp.', harga)

    elif kode==2:
       harga = int(10000*jumlah)
       print('Total harga : Rp.', harga)

    elif kode==3:
       harga = int(15000*jumlah)
       print('Total harga : Rp.', harga)

    elif kode==4:
       harga = int(15000*jumlah)
       print('Total harga : Rp.', harga)

elif pesan==2:
    print("""    ================MENU MINUMAN=============
    -----------------------------------------
    | KODE |   NAMA MINUMAN   |    HARGA    |
    -----------------------------------------
    |  1  | TEH ES            | Rp. 5.000   |
    |  2  | ES JERUK          | Rp. 7.000   |                        
    |  3  | LEMON TEA         | Rp. 6.000   |
    |  4  | AIR MINERAL       | Rp. 4.000   |   
    -----------------------------------------                """)
    kode = int(input('Kode menu : '))
    jumlah = int(input('Jumlah pesanan : '))
    
    if kode==1:
      harga = int(5000*jumlah)
      print('Total harga : Rp.', harga)
      
    elif kode==2:
       harga = int(7000*jumlah)
       print('Total harga : Rp.', harga)

    elif kode==3:
       harga = int(6000*jumlah)
       print('Total harga : Rp.', harga)

    elif kode==4:
       harga = int(4000*jumlah)
       print('Total harga : Rp.', harga)

elif pesan==3:
   print("""    ================MENU MAKANAN DAN MINUMAN==============
    -----------------------------------------------------
    | KODE |   NAMA MAKANAN DAN MINUMAN   |    HARGA    |
    -----------------------------------------------------
    |  1  | INDOMIE BIASA                 | Rp. 7.000   |
    |  2  | INDOMIE TELUR                 | Rp. 10.000  |                        
    |  3  | INDOMIE CARBONARA             | Rp. 15.000  |            
    |  4  | INDOMIE KORNET                | Rp. 15.0000 |           
    |  5  | TEH ES                        | Rp. 5.000   |          
    |  6  | ES JERUK                      | Rp. 7.000   |                                
    |  7  | LEMON TEA                     | Rp. 6.000   |         
    |  8  | AIR MINERAL                   | Rp. 4.000   |  
    -----------------------------------------------------                            """)
   
   kode = int(input('Kode menu : '))
   jumlah = int(input('Jumlah pesanan : '))

   if kode==1:
      harga = int(7000*jumlah)
      print('Total harga : Rp.', harga)
      
   elif kode==2:
       harga = int(10000*jumlah)
       print('Total harga : Rp.', harga)
       
   elif kode==3:
      harga = int(15000*jumlah)
      print('Total harga : Rp.', harga)
       
   elif kode==4:
    harga = int(15000*jumlah)
    print('Total harga : Rp.', harga)

   elif kode==5:
      harga = int(5000*jumlah)
      print('Total harga : Rp.', harga)
      
   elif kode==6:
       harga = int(7000*jumlah)
       print('Total harga : Rp.', harga)
       
   elif kode==7:
      harga = int(6000*jumlah)
      print('Total harga : Rp.', harga)
          
   elif kode==8:
      harga = int(4000*jumlah)
      print('Total harga : Rp.', harga)
else:
   print('Kode Pesanan Tidak Valid')

print('    ================TERIMA KASIH==============')


 

    
   







    

    
