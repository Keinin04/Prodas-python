#   Applikasi perpustakaan

import os

def clear_screen():
    os.system('cls')

def kembali():
    print("\n")
    input("Tekan tombol apa saja untuk kembali...")
    clear_screen()

buku = ['Henry book', 'Harry potter 1', 'buku cerdas cermat']

def show_data():
    if len(buku) <= 0 :
        print("Tidak ada Buku")
    else:
        for i in range(len(buku)):
            print('%i %s' %(i, buku[i]))


class Menu:
    def menu_pertama():
        while(True):
            print("     Menu Perpustakaan   ")
            print('------------------------------------')
            print(" 1 Untuk Tampilkan Buku")
            print(" 2 Untuk Pinjamkan Buku")
            print(" 3 Untuk Kembalikan Buku")  
            print(" 4 Untuk Tambahkan Buku")
            print(" 5 Untuk Keluar") 
            try:
                p=int(input('pilih menu 1-5: '))
                print()
                if p == 1:
                    clear_screen()
                    show_data()
                    kembali()
                else:
                    print('Masukkan angka')
                    kembali()
                    continue
            except ValueError:
                print('Masukan pilihan sesuai nomor !')
                kembali()
                continue

Menu.menu_pertama()