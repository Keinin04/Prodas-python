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
        return str(now().strftime('%H:%M:%S'))

    def menu_pertama():
        while(True):
            print('     Menu Perpustakaan   ')
            print('------------------------------------')
            print(' 1  Data Buku')
            print(' 2  Data Peminjaman')
            print(' 3  Data Pengembalian')  
            print(' 4  Penambahan Buku')  
            print(' 5  Ubah Data Buku')
            print(' 6  Keluar')
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
                    Buku.listBuku()
                    Buku.ubah()
                elif p == 6:
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
        u = 'Pinjaman-'+firstName+lastName+'.txt'

        
        d = 'Data-Peminjaman-'+Menu.getDate()+'.txt'




        # Memulai mencari buku untuk di pinjam
        success = False
        count = 0
        buku_dipinjam = []
        while success == False: # Perulangan meminjam buku
            Buku.menampilkan_buku() # Menampilkan daftar buku
            print('Buku yang dipinjam = ' + ','.join(str(x) for x in buku_dipinjam))
            print('Pilih salah satu menu di diatas (masukkan nomor urutan):')
            try:
                a = int(input())
                try:
                    if (int(jumlah_stok[a])>0): # Mengecek apakah stok tersebut tersedia
                        print('Buku Tersedia')
                        
                        if judul_buku[a]  not in buku_dipinjam: # Mengecek apakah buku tersebut belum minjam, jika lebih dari 1 maka tidak bisa
                            buku_dipinjam.append(judul_buku[a])
                            
                            jumlah_stok[a] = int(jumlah_stok[a]) - 1
                            jumlah_stok[a] = str(jumlah_stok[a])

                            
                            while(True): # menanyakan apakah ingin meminjam buku lain lagi
                                Menu.clear_screen()
                                Buku.menampilkan_buku() # Menampilkan daftar buku
                                print('Buku yang dipinjam = ' + ','.join(str(x) for x in buku_dipinjam))
                                option_buku = input('Apakah ingin meminjam buku lain lagi ? [y/n] ')
                                if option_buku == 'y':
                                    Menu.clear_screen()
                                    success = False
                                    break
                                elif option_buku == 'n':
                                    Menu.clear_screen() 

                                    with open(d, 'a+') as f: # Mencatat Data Peminjaman
                                        f.write(Menu.getTime() + ' - ' + firstName + ' ' + lastName + ' ' + ' telah meminjam Buku : ' + ','.join(str(x) for x in buku_dipinjam) + '\n')

                                    with open(u,'w+') as f: # Mulai mencatat header si peminjam
                                        f.write('           Program Perpustakaan \n')
                                        f.write('       Dipinjam oleh: '+ firstName + ' ' + lastName + '\n')
                                        f.write('    Tanggal: ' + Menu.getDate()+'    Waktu:'+ Menu.getTime()+'\n\n')
                                        f.write('S.N. \t\t Judul buku \t      Pengarang \n' )


                                    with open(u,'a') as f: # Memasukkannya kedalam file txt si peminjam
                                        for p in range(len(buku_dipinjam)):
                                            count += 1
                                            f.write(str(count) + '. \t\t'+ buku_dipinjam[p] +'\t\t'+buku_dipinjam[p]+'\n')

                                    with open(r'buku.txt', 'r+') as f: # Memperbarui isi file buku.txt pada listBuku
                                        for i in range(len(judul_buku)):
                                            if i != len(judul_buku) - 1:
                                                f.write(judul_buku[i] + ',' + pengarang[i] + ',' + str(jumlah_stok[i]) + '\n')
                                            else:
                                                f.write(judul_buku[i] + ',' + pengarang[i] + ',' + str(jumlah_stok[i]))

                                    with open(u, 'r') as f: # Menampilkan hasil peminjaman
                                        pinjaman = f.read()
                                        print(pinjaman)
                                        Menu.kembali()

                                    success = True
                                    break
                                else:
                                    print('Masukan y atau n saja')
                                    Menu.kembali()
                        else:
                            print('Maaf tidak bisa meminjam lebih dari 1 buku yang sama')
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

        a = 'Pinjaman-' + firstName+lastName+ '.txt'
        try:
            with open(a,'r') as f:
                data = f.read()

        except:
            print('Nama tersebut tidak ada')
            Menu.kembali()
            Buku.kembalikanBuku()
        
        b = 'Pengembalian-' + firstName+lastName + '.txt'
        with open(b, 'w+') as f:
            f.write('               Program Perpustakaan\n')
            f.write('             Dikembalikan oleh:' + firstName+' '+ lastName + '\n')
            f.write('   Tanggal: ' + Menu.getDate() + '  Waktu: ' + Menu.getTime() + '\n\n')
            f.write('S.N.\t\tJudul Buku\n')
        
        d = 'Data-Pengembalian-'+Menu.getDate()+'.txt'

        count = 1
        buku = 0
        buku_dikembali = []
        for i in range(len(judul_buku)): # Menghitung buku yang dipinjam 
            if judul_buku[i] in data:
                buku_dikembali.append(judul_buku[i])
                with open(b,'a') as f:
                    f.write(str(count)+ '.' + '\t\t' + judul_buku[i] + '\n')
                    count+=1
                buku += 1
            
        with open(b,'a') as f:# Menulis banyaknya buku dipinjam ke file pengembalian
            f.write("\nBanyak buku dipinjam: "+ str(buku)) 
        
        with open(b,'r') as f:# Menampilkan file Pengembalian
            peminjaman = f.read()
        
        lewat = True
        while lewat == True: # untuk menanyakan apakah ada denda 
            Menu.clear_screen()
            print(peminjaman)
            success = False
            denda = input('Apakah buku melewati batas peminjaman? [y/n]: ')

            if denda == 'y':# Jika terkena denda
                with open(b, 'a') as f:
                    f.write('\nTerkena denda : ya')

                while denda == 'y':# Melanjutkan menanyakan pertanyaan lain berapa hari keterlambatan
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
                                    total = bayar - jumlah
                                    with open(b, 'a') as f:
                                        f.write('\nDibayar sebesar : Rp' + str(bayar))
                                        f.write('\nKembalian : Rp' + str(total))

                                    denda = None
                                    lewat = False
                                    success = True
                                    break
                            except ValueError:
                                print('Masukan nominal pembayaran sesuai angka')
                                Menu.kembali()
                    except ValueError:
                        print('Masukan jumlah hari dalam angka saja')
                        Menu.kembali()

            elif denda == 'n':# Jika tidak terkena denda
                with open(b, 'a') as f:
                    f.write('\nTerkena denda : Tidak')
                lewat = False
                success = True
            else:
                print('Masukan y atau n saja')
                Menu.kembali()




        while(success == True):# Dijalankan ketika sudah memenuhi
            Menu.clear_screen()
            for p in range(len(judul_buku)): # Memperbarui stok di list 
                if judul_buku[p] in data:
                    jumlah_stok[p] = int(jumlah_stok[p]) + 1 
                    jumlah_stok[p] = str(jumlah_stok[p])

            with open(r'Buku.txt', 'r+') as f: # Memperbarui isi file buku.txt pada listBuku
                for i in range(len(judul_buku)):
                    if i != len(judul_buku) - 1:
                        f.write(judul_buku[i] + ',' + pengarang[i] + ',' + str(jumlah_stok[i]) + '\n')
                    else:
                        f.write(judul_buku[i] + ',' + pengarang[i] + ',' + str(jumlah_stok[i]))

            with open(d, 'a+') as f: # Mencatat Data Pengembalian
                f.write(Menu.getTime() + ' - ' + firstName + ' ' + lastName + ' ' + ' telah mengembalikan Buku : ' + ','.join(str(x) for x in buku_dikembali) + '\n')
            
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
    
    def ubah(): # untuk mengubah data
        success = False
        loop_data = False
        while success == False:

            while loop_data == False: # Pilih data yang ingin di ubah
                Buku.menampilkan_buku()
                try:
                    print('Masukan q untuk balik ke menu awal')
                    data = input('Pilih data keberapa yang ingin diubah ? : ')
                    if data == 'q':
                        loop_data = True
                        success = True
                        Menu.clear_screen()
                        break
                    else:
                        data = int(data)
                        judul_buku[data]
                        loop_ubah = False

                    while loop_ubah == False:
                        Menu.clear_screen()
                        print('Apa yang ingin diubah ?')
                        print('Masukan j untuk Judul : ' + judul_buku[data])
                        print('Masukan p untuk Pengarang : ' + pengarang[data])
                        print('Masukan s untuk jumlah stok : ' + str(jumlah_stok[data]))
                        print('Masukan q jika ingin balik ke menu awal')
                        ubah = str(input('Pilih apa yang diubah ?  : '))

                        if ubah == 'q':
                            loop_ubah = True
                            Menu.clear_screen()
                            break

                        elif ubah == 'j':

                            while ubah == 'j':# Mengganti nama judul
                                Menu.clear_screen()
                                print('Masukan q jika ingin balik ke menu awal')
                                menjadi = input('Masukan nama judul baru : ')

                                if menjadi == 'q':
                                    ubah = None
                                    Menu.clear_screen()
                                    break

                                while(True): # Menanya benar atau tidak
                                    Menu.clear_screen()
                                    print('Apakah benar ingin nama judul ', judul_buku[data], ' ini menjadi ', menjadi,' ?')
                                    ask = input('y atau n : ')
                                    if ask == 'y':
                                        judul_buku[data] = menjadi
                                        with open(r'buku.txt', 'r+') as f: # Memperbarui isi file buku.txt pada listBuku
                                            for i in range(len(judul_buku)):
                                                if i != len(judul_buku) - 1:
                                                    f.write(judul_buku[i] + ',' + pengarang[i] + ',' + str(jumlah_stok[i]) + '\n')
                                                else:
                                                    f.write(judul_buku[i] + ',' + pengarang[i] + ',' + str(jumlah_stok[i]))
                                        ubah = None
                                        break
                                    elif ask == 'n':
                                        Menu.clear_screen()
                                        break
                                    else:
                                        print('Masukan y atau n saja')
                                        Menu.kembali()

                        elif ubah == 'p':

                            while ubah == 'p':# Mengganti nama pengarang
                                Menu.clear_screen()
                                print('Masukan q jika ingin balik ke menu awal')
                                menjadi = input('Masukan nama pengarang baru : ')

                                if menjadi == 'q':
                                    ubah = None
                                    Menu.clear_screen()
                                    break

                                while(True): # Menanya benar atau tidak
                                    Menu.clear_screen()
                                    print('Apakah benar ingin nama pengarang ', pengarang[data], ' ini menjadi ', menjadi,' ?')
                                    ask = input('y atau n : ')
                                    if ask == 'y':
                                        pengarang[data] = menjadi
                                        with open(r'buku.txt', 'r+') as f: # Memperbarui isi file buku.txt pada listBuku
                                            for i in range(len(judul_buku)):
                                                if i != len(judul_buku) - 1:
                                                    f.write(judul_buku[i] + ',' + pengarang[i] + ',' + str(jumlah_stok[i]) + '\n')
                                                else:
                                                    f.write(judul_buku[i] + ',' + pengarang[i] + ',' + str(jumlah_stok[i]))
                                        ubah = None
                                        break
                                    elif ask == 'n':
                                        Menu.clear_screen()
                                        break
                                    else:
                                        print('Masukan y atau n saja')
                                        Menu.kembali()
                                    
                        elif ubah == 's':

                            while ubah == 's':# Mengganti jumlah stok
                                Menu.clear_screen()
                                try:
                                    print('Masukan q jika ingin balik ke menu awal')
                                    menjadi = input('Masukan jumlah stok baru : ')
                                    if menjadi == 'q':
                                        ubah = None
                                        Menu.clear_screen()
                                        break
                                    else:
                                        menjadi = int(menjadi)

                                except ValueError:
                                    print('Masukan jumlah stok dalam angka saja')
                                    Menu.kembali()
                                    continue

                                while(True): # Menanya benar atau tidak
                                    Menu.clear_screen()
                                    print('Apakah benar ingin jumlah stok buku ',judul_buku[data],' dari ', jumlah_stok[data], ' ini menjadi ', menjadi,' ?')
                                    ask = input('y atau n : ')
                                    if ask == 'y':
                                        jumlah_stok[data] = str(menjadi)
                                        with open(r'buku.txt', 'r+') as f: # Memperbarui isi file buku.txt pada listBuku
                                            for i in range(len(judul_buku)):
                                                if i != len(judul_buku) - 1:
                                                    f.write(judul_buku[i] + ',' + pengarang[i] + ',' + str(jumlah_stok[i]) + '\n')
                                                else:
                                                    f.write(judul_buku[i] + ',' + pengarang[i] + ',' + str(jumlah_stok[i]))
                                        ubah = None
                                        break
                                    elif ask == 'n':
                                        Menu.clear_screen()
                                        break
                                    else:
                                        print('Masukan y atau n saja')
                                        Menu.kembali()

                        else:
                            print('')
                            print('Pilih sesuai perintah di atas')
                            Menu.kembali()

                except ValueError:
                    print('')
                    print('Masukan nomor untuk memilih buku')
                    Menu.kembali()
                except IndexError:
                    print('')
                    print('Pilih buku sesuai nomor')
                    Menu.kembali()



















os.system('cls')
Menu.menu_pertama()
