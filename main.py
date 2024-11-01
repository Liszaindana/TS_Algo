import modul
while True:
   print('''
    pilih penjumlah
    1. Penjumlahan
    2. Pengurangan
    3. Perkalian
            ''')
   option = int(input('Masukan Pilihan Anda 1/2/3:'))
   bil1 = int(input('Masukan Bilangan 1 :'))
   bil2 = int(input('Masukan Bilangan 2 :'))  

   if option == 1:
      modul.penjumlahan(bil1,bil2)
      print('-----selesai-----')
   elif option == 2:
      modul.pengurangan(bil1,bil2)
      print('-----selesai-----')
   elif option == 13:
      modul.perkalian(bil1,bil2)
      print('-----selesai-----')
   else:
      print('Maaf Bilangan Yang Anda Inputkan Gagal')
