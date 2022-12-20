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
            print(' 1  Data Buku')
            print(' 2  Data Peminjaman')
            print(' 3  Data Pengembalian')  
            print(' 4  Penambahan Buku')  
            print(' 5  Keluar')
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
                    Buku.tambah()
                elif p == 5:
                    Menu.clear_screen()
                    break
                else:
                    print('Masukkan pilihan sesuai nomor !')
                    Menu.kembali()
                    continue
            except ValueError:
                print('Hanya Masukan angka saja')
                Menu.kembali()
                continue

class Buku():
    
    def listBuku():
        global judul_buku
        global pengarang
        global jumlah_stok

        judul_buku = []
        pengarang = []
        jumlah_stok = []

        f = open(r'buku.txt', 'r+')
        f = f

        lines = f.readlines() # membaca baris dan dimasukan ke list 
        lines = [x.strip('\n') for x in lines] # menghapus \n di lines
        for i in range(len(lines)):
            ind = 0
            for a in lines[i].split(','):
                if ind == 0:
                    judul_buku.append(a)
                if ind == 1:
                    pengarang.append(a)
                if ind == 2:
                    jumlah_stok.append(a)
                ind+= 1
        


    def menampilkan_buku(): # Menampilkan Data buku
        buku = {
            'Judul Buku' : judul_buku,
            'Nama Pengarang' : pengarang,
            'Jumlah stok' : jumlah_stok
        }

        daftar_buku = pd.DataFrame(buku)
        print('====================================================================================================')
        print(daftar_buku)
        print('====================================================================================================')

    def minjam(): # peminjaman buku 

        # Memulai memasukkan nama peminjam
        loopName = False
        while loopName == False: # Memulai menginput nama

            while(True): # Memasukkan nama depan peminjam
                firstName = input('Masukkan nama depan peminjam: ')
                if firstName.isalpha(): # akan dijalankan jika type datanya str huruf alphabet
                    Menu.clear_screen()
                    break
                else:
                    print('Masukkan huruf alphabet')
                    Menu.kembali()
            while(True): # Memasukkan nama belakang peminjam
                lastName= input('Masukkan nama belakang peminjam: ')
                if lastName.isalpha(): # akan dijalankan jika type datanya str huruf alphabet
                    Menu.clear_screen()
                    break
                else:
                    print('Masukkan huruf alphabet')
                    Menu.kembali()
            while(True): # Menanyakan apakah nama tersebut sudah benar
                Menu.clear_screen
                print('Apakah nama ' + firstName + ' ' + lastName + ' ini sudah benar?')
                option_name = input('y atau n ? ')
                if option_name  == 'y':
                    loopName = True
                    Menu.clear_screen()
                    break
                elif option_name == 'n':
                    Menu.clear_screen()
                    break
                else:
                    print('Masukkan y atau n saja')
                    Menu.kembali()

        # Memasukkan nama peminjam ke file txt
        u = 'Pinjaman-'+firstName+'.txt'
        with open(u,'w+') as f:
            f.write('           Program Perpustakaan \n')
            f.write('       Dipinjam oleh: '+ firstName + ' ' + lastName + '\n')
            f.write('    Tanggal: ' + Menu.getDate()+'    Waktu:'+ Menu.getTime()+'\n\n')
            f.write('S.N. \t\t Judul buku \t      Pengarang \n' )


        # Memulai mencari buku untuk di pinjam
        success = False
        count = 0
        while success == False: # Perulangan meminjam buku
            Buku.menampilkan_buku() # Menampilkan daftar buku
            print('Pilih salah satu menu di diatas (masukkan nomor urutan):')
            try:
                a = int(input())
                try:
                    if (int(jumlah_stok[a])>0): # Mengecek apakah stok tersebut tersedia
                        count += 1
                        print('Buku Tersedia')
                        with open(u,'a') as f: # Memasukkannya kedalam file txt si peminjam
                            f.write(str(count) + '. \t\t'+ judul_buku[a] +'\t\t'+pengarang[a]+'\n')
                        
                        jumlah_stok[a] = int(jumlah_stok[a]) - 1
                        with open(r'buku.txt', 'r+') as f: # Memperbarui isi file buku.txt pada listBuku
                            for i in range(len(judul_buku)):
                                if i != len(judul_buku) - 1:
                                    f.write(judul_buku[i] + ',' + pengarang[i] + ',' + str(jumlah_stok[i]) + '\n')
                                else:
                                    f.write(judul_buku[i] + ',' + pengarang[i] + ',' + str(jumlah_stok[i]))
                        
                        while(True): # menanyakan apakah ingin meminjam buku lagi
                            option_buku = input('Apakah ingin meminjam buku lagi ? [y/n] ')
                            if option_buku == 'y':
                                Menu.clear_screen()
                                success = False
                                break
                            elif option_buku == 'n':
                                Menu.clear_screen()
                                with open(u, 'r') as f:
                                    pinjaman = f.read()
                                    print(pinjaman)
                                    Menu.kembali()
                                success = True
                                break
                            else:
                                print('Masukan y atau n saja')
                                Menu.kembali()
                    else:
                        print('Buku tidak tersedia')
                        Menu.kembali()
                        continue
                
                except IndexError:
                    print('')
                    print('pilih buku sesuai nomor')
                    Menu.kembali()
            except ValueError:
                print('')
                print('Pilih sesuai nomor')
                Menu.kembali()

    def kembalikanBuku(): # fungsi untuk mengembalikan buku yang dipinjam
        name = input('Masukkan nama depan anda: ')
        a = 'Pinjaman-' + name + '.txt'
        try:
            with open(a,'r') as f:
                data = f.read()

        except:
            print('Nama tersebut tidak ada')
            Menu.kembali()
            Buku.kembalikanBuku()
        
        b = 'Pengembalian-' + name + '.txt'
        with open(b, 'w+') as f:
            f.write('               Program Perpustakaan\n')
            f.write('             Dikembalikan oleh:' + name + '\n')
            f.write('   Tanggal: ' + Menu.getDate() + '  Waktu: ' + Menu.getTime() + '\n\n')
            f.write('S.N.\t\tJudul Buku\n')

        count = 1
        buku = 0
        for i in range(len(judul_buku)): # Menghitung buku yang dipinjam 
            if judul_buku[i] in data:
                with open(b,'a') as f:
                    f.write(str(count)+ '.' + '\t\t' + judul_buku[i] + '\n')
                    count+=1
                buku += 1
            
        with open(b,'a') as f:# Menulis banyaknya buku dipinjam ke file pengembalian
            f.write("\nBanyak buku dipinjam: "+ str(buku)) 
        
        with open(b,'r') as f:# Menampilkan file Pengembalian
            peminjaman = f.read()
        
        while(True):# untuk menanyakan apakah ada denda 
            Menu.clear_screen()
            print(peminjaman)
            success = False
            denda = input('Apakah buku melewati batas peminjaman? [y/n]: ')

            if denda == 'y':# Jika terkena denda
                with open(b, 'a') as f:
                    f.write('\nTerkena denda : ya')

                while(True):# Melanjutkan menanyakan pertanyaan lain berapa hari keterlambatan
                    Menu.clear_screen()
                    with open(b, 'r') as f:
                        print(f.read())

                    print('Berapa hari keterlambatan ? [contoh masukan 1 untuk satu hari]')
                    try:
                        hari = int(input())
                        jumlah = (buku * 500)+(hari * 500) 
                        with open(b, 'a') as f:
                            f.write('\nBanyaknya hari dilewati : ' + str(hari))
                            f.write('\nDenda yang harus dibayar sebesar : Rp' + str(jumlah))

                        while(True): # Memasukan nominal pembayaran
                            Menu.clear_screen()
                            with open(b, 'r') as f:
                                print(f.read())
                            try:
                                bayar = int(input("Masukan nominal pembayaran : Rp"))
                                if bayar < jumlah:
                                    print('Maaf nominal anda kurang')
                                    Menu.kembali()
                                else:
                                    total = jumlah - bayar
                                    with open(b, 'a') as f:
                                        f.write('\nDibayar sebesar : Rp' + str(bayar))
                                        f.write('\nKembalian : Rp' + str(total))
                                    success = True
                                    break
                            except ValueError:
                                print('Masukan nominal pembayaran sesuai angka')
                                Menu.kembali()
                        break
                    except ValueError:
                        print('Masukan jumlah hari dalam angka saja')
                        Menu.kembali()
                break
            elif denda == 'n':# Jika tidak terkena denda
                with open(b, 'a') as f:
                    f.write('\nTerkena denda : Tidak')
                success = True
                break
            else:
                print('Masukan y atau n saja')
                Menu.kembali()




        while(success == True):# Dijalankan ketika sudah memenuhi
            Menu.clear_screen()
            jumlah_stok[i] = int(jumlah_stok[i]) + 1 # memperbarui stok 
            with open(r'Buku.txt', 'r+') as f: # Memperbarui isi file buku.txt pada listBuku
                for i in range(len(judul_buku)):
                    if i != len(judul_buku) - 1:
                        f.write(judul_buku[i] + ',' + pengarang[i] + ',' + str(jumlah_stok[i]) + '\n')
                    else:
                        f.write(judul_buku[i] + ',' + pengarang[i] + ',' + str(jumlah_stok[i]))
            
            with open(b, 'r') as f:# Menampilkan hasil pengembalian
                hasil = f.read()
                print(hasil)
                Menu.kembali()
                break
        
    def tambah():# Untuk menambah data Buku
        loop_judul = False
        loop_pengarang = False
        loop_stok = False
        success = False

        while success == False:# perulangan identifikasi data

            while loop_judul == False:# Memasukan data judul buku
                judul = input("judul Buku = ")
                Menu.clear_screen()

                while(True):# Menanyakan apakah yang di input sudah benar
                    print('Apakah nama Judul ' + judul + ' sudah benar?')
                    q = input('y atau n ? : ')
                    if q == 'y':
                        loop_judul = True
                        Menu.clear_screen()
                        break
                    elif q == 'n':
                        Menu.clear_screen()
                        break
                    else:
                        print('Masukan y atau n saja')
                        Menu.kembali()
                        continue

            while loop_pengarang== False:# Memasukan data buku si pengarang
                pengarang = input("Pengarang = ")
                Menu.clear_screen()

                while(True):# Menanyakan apakah memasukan pengarang itu sudah benar  
                    print('Apakah nama pengarang ' + pengarang + ' sudah benar?')
                    q = input('y atau n ? : ')
                    if q == 'y':
                        loop_pengarang = True
                        Menu.clear_screen()
                        break
                    elif q == 'n':
                        Menu.clear_screen()
                        break
                    else:
                        print('Masukan y atau n saja')
                        Menu.kembali()
                        continue

            while loop_stok == False:# Memasukkan data buku stok
                try:
                    stok = int(input("stok = "))
                    Menu.clear_screen()
                except ValueError:
                    print('')
                    print('Masukan nominal stok!')
                    Menu.kembali()
                    continue


                while(True):
                    print('Apakah pemasukan data dengan stok ' + str(stok) + ' sudah benar?')
                    q = input('y atau n ? : ')
                    if q == 'y':
                        loop_stok= True
                        Menu.clear_screen()
                        break
                    elif q == 'n':
                        Menu.clear_screen()
                        break
                    else:
                        print('Masukan y atau n saja')
                        Menu.kembali()
                        continue
            
            
            while(True): # Bertanya apakah data yang dimasukan sudah benar?
                Menu.clear_screen()
                print('Apakah nama judul ' + judul + ' nama pengarang ' + pengarang + ' dengan stok ' + str(stok) + ' sudah benar?')
                q = input('y atau n ? : ')
                if q == 'y':
                    with open(r'buku.txt', 'a') as f:
                        pembatas = ","
                        f.write('\n' + judul + pembatas + pengarang + pembatas + str(stok) )
                    success = True
                    wrong = False
                    Menu.clear_screen()
                    break
                elif q == 'n':
                    wrong = True
                    Menu.clear_screen()
                    break
                else:
                    print('y atau n saja')
                    Menu.kembali()
                    continue

            while wrong == True: # mengecek apa yang salah
                print('Apa yang salah?')
                print('Masukan j untuk Judul : ' + judul)
                print('Masukan p untuk Pengarang : ' + pengarang)
                print('Masukan s untuk stok : ' + str(stok))
                ask = input('[j/p/s] ? : ')
                if ask == 'j':
                    loop_judul = False
                    wrong = False
                    Menu.clear_screen()
                    break
                elif ask == 'p':
                    loop_pengarang = False
                    wrong = False
                    Menu.clear_screen()
                    break
                elif ask == 's':
                    loop_stok = False
                    wrong = False
                    Menu.clear_screen()
                    break
                else:
                    print('Masukan sesuai perintah')
                    Menu.kembali()
                    continue
















os.system('cls')
Menu.menu_pertama()
