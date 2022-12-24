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
                p=int(input('pilih menu 1-6: '))
                print()
                if p == 1:
                    Menu.clear_screen()
                    Buku.listBuku()
                    Buku.menampilkan_buku()
                    Menu.kembali()
                elif p == 2:
                    Menu.clear_screen()
                    Menu.menu_data_peminjaman()
                elif p == 3:
                    Menu.clear_screen()
                    Buku.listBuku()
                    Buku.listPeminjam()
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
    
    def menu_data_peminjaman():
        while(True):
            Menu.clear_screen()
            print('     Menu Perpustakaan > Data Peminjaman >  ')
            print('------------------------------------------')
            print(' 1  Menampilkan Data Peminjaman')
            print(' 2  Menambahkan Data Peminjaman')
            print(' q  Untuk Balik kebelakang')
            try:
                print('')
                p = input('pilih menu 1-2: ')
                if p == 'q':
                    Menu.clear_screen()
                    break
                else:
                    p = int(p)

                    if p == 1:
                        Menu.clear_screen()
                        Buku.listPeminjam()
                        print('     Menu Perpustakaan > Data Peminjaman >  Menampilkan Data Peminjaman')
                        print('-----------------------------------------------------------------------')
                        Buku.menampilkan_peminjam()
                        Menu.kembali()
                    elif p == 2:
                        Menu.clear_screen()
                        Buku.listBuku()
                        Buku.minjam()
            except ValueError:
                print('Masukan sesuai perintah')
                Menu.kembali()





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
        
    def listPeminjam():
        # Menyimpan identitas
        global nama_peminjam
        global buku_dipinjam
        global tanggal_dipinjam

        nama_peminjam = []
        buku_dipinjam = []
        tanggal_dipinjam = []
        with open(r'Data-Peminjaman.txt', 'r+') as f:
            lines = f.readlines()
            lines = [x.strip('\n') for x in lines]

            for i in range(len(lines)):
                ind = 0
                for a in lines[i].split('.'):
                    if ind == 0:
                        nama_peminjam.append(a)
                    if ind == 1:
                        buku_dipinjam.append(a)
                    if ind == 2:
                        tanggal_dipinjam.append(a)
                    ind+=1
        


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
    
    def menampilkan_peminjam():
        peminjam = {
            'Nama Peminjam' : nama_peminjam,
            'Buku dipinjam' : buku_dipinjam,
            'Tanggal' : tanggal_dipinjam
        }

        daftar_peminjam = pd.DataFrame(peminjam)
        if daftar_peminjam.empty:
            print('====================================================================================================')
            print('Data Peminjaman kosong.')
            print('Pergi ke menu Menambahkan Data Peminjaman untuk memasukan Data.')
            print('====================================================================================================')
            return 'kosong'
        else:
            print('====================================================================================================')
            print(daftar_peminjam)
            print('====================================================================================================')



    def minjam(): # peminjaman buku 

        # Memulai memasukkan nama peminjam
        loopName = False
        while loopName == False: # Memulai menginput nama

            while(True): # Memasukkan nama depan peminjam
                print('     Menu Perpustakaan > Data Peminjaman >  Menambahkan Data Peminjaman')
                print('-----------------------------------------------------------------------')
                Name = input('Masukkan nama peminjam: ')
                check_name = Name.replace(' ', '')
                if check_name.isalpha(): # akan dijalankan jika type datanya str huruf alphabet
                    Menu.clear_screen()
                    break
                else:
                    print('')
                    print('Masukkan huruf alphabet')
                    Menu.kembali()

            while(True):
                Menu.clear_screen
                print('     Menu Perpustakaan > Data Peminjaman >  Menambahkan Data Peminjaman')
                print('-----------------------------------------------------------------------')
                print('Apakah nama ' + Name +  ' ini sudah benar?')
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

        # Memasukkan nama peminjam ke file data peminjaman txt
        d = 'Data-Peminjaman.txt'




        # Memulai mencari buku untuk di pinjam
        success = False
        buku_dipinjam = []
        while success == False: # Perulangan meminjam buku
            print('     Menu Perpustakaan > Data Peminjaman >  Menambahkan Data Peminjaman')
            print('-----------------------------------------------------------------------')
            print('====================================================================================================')
            print('     Nama Peminjam : ' + Name)
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
                                print('     Menu Perpustakaan > Data Peminjaman >  Menambahkan Data Peminjaman')
                                print('-----------------------------------------------------------------------')
                                print('====================================================================================================')
                                print('     Nama Peminjam : ' + Name)
                                Buku.menampilkan_buku() # Menampilkan daftar buku
                                print('Buku yang dipinjam = ' + ','.join(str(x) for x in buku_dipinjam))
                                option_buku = input('Apakah ingin meminjam buku lain lagi ? [y/n] ')
                                if option_buku == 'y':
                                    Menu.clear_screen()
                                    success = False
                                    break
                                elif option_buku == 'n':
                                    Menu.clear_screen() 
                                    Menu.kembali()

                                    with open(d, 'r+') as f: # Mencatat Data Peminjaman
                                        f.write(Name +  '.' + ','.join(str(x) for x in buku_dipinjam) + '.' + Menu.getDate() + '\n')

                                    with open(r'buku.txt', 'r+') as f: # Memperbarui isi file buku.txt pada listBuku
                                        for i in range(len(judul_buku)):
                                            if i != len(judul_buku) - 1:
                                                f.write(judul_buku[i] + ',' + pengarang[i] + ',' + str(jumlah_stok[i]) + '\n')
                                            else:
                                                f.write(judul_buku[i] + ',' + pengarang[i] + ',' + str(jumlah_stok[i]))

                                    print('Data Peminjaman ' + Name + ' sudah tersimpan')


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
            if Buku.menampilkan_peminjam() == 'kosong':
                print('Tidak bisa melanjutkan karena data peminjaman kosong')
                Menu.kembali()
                break
            else:
                print('Masukkan q  Untuk Balik Kebelakang')
                print('Pilih salah satu menu di diatas (masukkan nomor urutan):')

                try:
                    k = int(input(''))
                    # MASIH BLM DI LANJUTIN
                    nama_peminjam[k]

                    nama_peminjam.remove(nama_peminjam[k])

                    daftar_buku_dipinjam = buku_dipinjam[k].split(',') 
                    for b in range(len(daftar_buku_dipinjam)):
                        for i in range(len(judul_buku)):
                            if daftar_buku_dipinjam[b] == judul_buku[i]:
                                jumlah_stok[i] = int(jumlah_stok[i]) + 1
                                jumlah_stok[i] = str(jumlah_stok[i])
                                break



                except IndexError:
                    print('Pilih salah satu nomor diatas')
                    Menu.kembali()

                


            
            
        try:
            with open(a,'r') as f:
                data = f.read()

        except:
            print('Nama tersebut tidak ada')
            Menu.kembali()
            Buku.kembalikanBuku()
        
        
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
