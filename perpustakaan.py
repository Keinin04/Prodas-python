#   Applikasi perpustakaan

import os
import datetime
import pandas as pd


class Menu():
    def clear_screen(): # untuk menghapus tampilan
        os.system('cls')

    def kembali(): # fungsi untuk kembali
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
            print('     Menu Perpustakaan   ')
            print('------------------------------------')
            print(' 1 Untuk Tampilkan Buku')
            print(' 2 Untuk Pinjamkan Buku')
            print(' 3 Untuk Kembalikan Buku')  
            print(' 4 Untuk Tambahkan Buku')
            print(' 5 Untuk Keluar')
            try:
                p=int(input('pilih menu 1-5: '))
                print()
                if p == 1:
                    Menu.clear_screen()
                    Buku.listBuku()
                    Buku.menampilkan_buku()
                    Menu.kembali()
                elif p == 2:
                    Menu.clear_screen()
                    Buku.listBuku()
                    Buku.minjam()
                elif p == 3:
                    Menu.clear_screen()
                    Buku.listBuku()
                    Buku.kembalikanBuku()
                elif p == 4:
                    Menu.clear_screen()
                    Buku.tambah_buku()
                elif p == 5:
                    print('Keluar..')
                    break
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

        with open(r'buku.txt','r+') as f:

            lines = f.readlines() # membaca baris dan dimasukan ke list 
            lines = [x.strip('\n') for x in lines] # menghapus newline di baris
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
            if firstName.isalpha(): # akan dijalankan jika type datanya str
                break
            print('Masukkan huruf')
        while(True):
            lastName= input('Masukkan nama belakang peminjam: ')
            if lastName.isalpha(): # akan dijalankan jika type datanya str
                break
            print('Masukkan huruf')
        Buku.menampilkan_buku()

        t = 'Pinjaman-'+firstName+'.txt'
        with open(t,'w+') as f:
            f.write('           Perpustakaan \n')
            f.write('       Dipinjam oleh: '+ firstName + ' ' + lastName + '\n')
            f.write('    Tanggal: ' + Menu.getDate()+'    Waktu:'+ Menu.getTime()+'\n\n')
            f.write('S.N. \t\t Judul buku \t      Pengarang \n' )

        while success == False:
            print('Pilih menu di diatas :')
            try:
                a=int(input())
                try:
                    if (int(jumlah_stok[a])>0):
                        print('Buku Tersedia')
                        with open(t,'a') as f:
                            f.write('1. \t\t'+ judul_buku[a]+'\t\t  '+pengarang[a]+'\n')
                        
                        jumlah_stok[a] = int(jumlah_stok[a]) - 1
                        with open(r'buku.txt', 'r+') as f:
                            for i in range(8):
                                f.write(judul_buku[i]+','+pengarang[i]+','+str(jumlah_stok[i])+','+'Rp'+harga[i] + '\n')
                                continue
                        

                        # untuk buku yang dipinjam lebih dari 1
                        loop = True
                        count = 1
                        while loop == True:
                            choice = str(input('Apakah ingin meminjam buku lagi ? [y/n] '))

                            if choice == 'y':
                                count += 1
                                Buku.menampilkan_buku()
                                print('Pilih menu di atas :')
                                
                                a = int(input())
                                if(int(jumlah_stok[a])>0):
                                    print('Buku Tersedia')
                                    with open(t,'a') as f:
                                        f.write(str(count) + '. \t\t' + judul_buku[a], + '\t\t ' + pengarang[a] + '\n')

                                        jumlah_stok[a] = int(judul_buku[a]) - 1
                                        with open(r'buku.txt', 'r+') as f:
                                            for i in range(8):
                                                f.write(judul_buku[i]+','+pengarang[i]+','+str(jumlah_stok[i]+','+'Rp'+harga[i]))
                                                success=False
                                                continue
                                else:
                                    loop = False
                                    continue
                            elif choice == 'n':
                                print('Keluar')
                                print('')
                                loop = False
                                success = True
                            else:
                                print('Masukkan sesuai y/n')
                    else:
                        print('Buku tidak tersedia')
                        Buku.minjam()
                        success = False
                        continue
                except IndexError:
                    print('')
                    print('pilih buku sesuai nomor')
            except ValueError:
                print('')
                print('Pilih sesuai nomor')

    def kembalikanBuku():
        name = input('Masukkan nama peminjam: ')
        a = 'Pinjaman-' + name + '.txt'
        try:
            with open(a,'r') as f:
                lines = f.readlines()
                lines = [a.strip('Rp') for a in lines]

            with open(a, 'r') as f:
                data = f.read()
                print(data)
        except:
            print('Nama peminjam salah')
            Buku.kembalikanBuku()
        
        b = 'Pengembalian-' + name + '.txt'
        with open(b, 'w+'):
            f.write('               Program Perpustakaan\n')
            f.write('                   Dikembalikan oleh:' + name + '\n')
            f.write('   Tanggal: ' + Menu.getDate() + '  Waktu:' + Menu.getTime() + '\n\n')
            f.write('S.N.\t\tJudul Buku\t\tTotal\n')


        total = 0.0
        for i in range(8):
            if judul_buku[i] in data:
                with open(b,'a') as f:
                    f.write(str(i+1) + '\t\t' + judul_buku[i] + '\t\tRp' + harga[i] + '\n')
                    jumlah_stok[i] = int(jumlah_stok[i]) + 1
                total += float(harga[i])
        
        print('\t\t\t\t\t\t\t' + 'Rp' + str(total))
        print('Apakah buku melewati batas peminjaman ?')
        print('Masukkan y atau n')
        option = input()
        if option == 'y':
            print('Berapa hari keterlambatan')
            hari = int(input())
            denda = 2000 * hari
            with open(b, 'a+') as f:
                f.write('\t\t\t\t\tTotal: Rp' + str(total))

            with open('Buku.txt') as f:
                for i in range(8):
                    f.write(judul_buku[i] + ',' + pengarang[i] + ',' + str(jumlah_stok[i]) + ',' + 'Rp' + harga[i] + '\n')
    
    def tambah_buku():
        with open(r'buku.txt', 'a+') as f:
            judul_buku = input('Judul = ')
            pengarang = input('Pengarang = ')
            stok = input('stok = ')
            harga = input('harga = Rp ')
            f.write('\n' + judul_buku + ',' + pengarang + ',' + stok + 'Rp' + harga)


os.system('cls')
Menu.menu_pertama()
