#   Applikasi perpustakaan

import os
import datetime
import pandas as pd



class Menu ():
    def clear_screen(): # untuk menghapus tampilan
        os.system('cls')

    def kembali():
        print("\n")
        input("Tekan tombol apa saja untuk kembali...")
        Menu.clear_screen()

    def getDate(): # untuk mendapatkan tanggal
        now = datetime.datetime.now
        return str(now().date())

    def getTime(): # untuk mendapatkan waktu 
        now = datetime.datetime.now
        return str(now().time())

    def menu_pertama():
        while(True):
            print("     Menu Perpustakaan   ")
            print('------------------------------------')
            print(" 1 Untuk Tampilkan Buku")
            print(" 2 Untuk Pinjamkan Buku")
            print(" 3 Untuk Kembalikan Buku")  
            print(" 4 Untuk Tambahkan Buku")
            try:
                p=int(input('pilih menu 1-5: '))
                print()
                if p == 1:
                    Menu.clear_screen()
                    Buku.menampilkan_buku()
                    Menu.kembali()
                elif p == 2:
                    Menu.clear_screen()
                    Buku.listBuku()
                    Buku.minjam()
                elif p == 4:
                    Buku.listBuku()
                    Menu.clear_screen()
                else:
                    print('Masukkan angka')
                    Menu.kembali()
                    continue
            except ValueError:
                print('Masukan pilihan sesuai nomor !')
                Menu.kembali()
                continue

class Buku():

    def listBuku():
        global judul_buku
        global pengarang
        global jumlah_stok
        global harga

        judul_buku = []
        pengarang = []
        jumlah_stok = []
        harga = []

        with open(r'Prodas-python\buku.txt','r+') as f:

            lines = f.readlines() # membaca baris 
            lines = [x.strip('\n') for x in lines] # menghapus newline
            for i in range(len(lines)):
                ind = 0
                for a in lines[i].split(','):
                    if(ind==0):
                        judul_buku.append(a)
                    if(ind==1):
                        pengarang.append(a)
                    if(ind==2):
                        jumlah_stok.append(a)
                    if(ind==3):
                        harga.append(a)
                    ind+=1

    def menampilkan_buku(): # Menampilkan Data buku
        Buku.listBuku()
        buku = {
            'Judul Buku' : judul_buku,
            'Nama Pengarang' : pengarang,
            'Jumlah stok' : jumlah_stok,
            'harga' : harga,
        }

        daftar_buku = pd.DataFrame(buku)
        print('====================================================================================================')
        print(daftar_buku)
        print('====================================================================================================')
            

    def minjam(): # peminjaman buku 
        success = False
        while(True):
            firstName = input('Masukkan nama depan peminjam: ')
            if firstName.isalpha(): # akan dijalankan jika typedatanya str
                break
            print('Masukkan huruf')
        while(True):
            lastName= input('Masukkan nama belakang peminjam: ')
            if lastName.isalpha(): # akan dijalankan jika typedatanya str
                break
            print('Masukkan huruf')
        Buku.menampilkan_buku()

        t = 'Prodas-python' + '\\' + 'Pinjaman-'+firstName+'.txt'
        with open(t,'w+') as f:
            f.write('           Perpustakaan \n')
            f.write('       Dipinjam oleh: '+ firstName + ' ' + lastName + '\n')
            f.write('    Tanggal: ' + Menu.getDate()+'    Waktu:'+ Menu.getTime()+'\n\n')
            f.write('S.N. \t\t Judul buku \t      Pengarang \n' )

        while success == False:
            print('Pilih menu di bawah ini :')
            for i in range(len(judul_buku)):
                print('Masukkan', i, 'untuk meminjam buku', judul_buku[i])



    




Menu.menu_pertama()
