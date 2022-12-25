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



    def menu_pertama():
        while(True):
            print('     Menu Perpustakaan   ')
            print('------------------------------------')
            print(' 1  Data Buku')
            print(' 2  Data Peminjaman')
            print(' 3  Data Pengembalian')  
            print(' q  Keluar')
            try:
                print('')
                p = input('pilih menu 1-3 atau q: ')
                if p == 'q':
                    Menu.clear_screen()
                    break
                else:
                    p = int(p)

                if p == 1:
                    Menu.clear_screen()
                    Menu.menu_data_buku()
                elif p == 2:
                    Menu.clear_screen()
                    Menu.menu_data_peminjaman()
                elif p == 3:
                    Menu.clear_screen()
                    Buku.listBuku()
                    Buku.listPeminjam()
                    Buku.kembalikanBuku()
                else:
                    print('Masukkan pilihan sesuai perintah !')
                    Menu.kembali()
                    continue
            except ValueError:
                print('Hanya Masukan angka saja')
                Menu.kembali()
                continue
    
    def menu_data_buku():
        while(True):
            print('     Menu Perpustakaan > Data Buku >')
            print('---------------------------------------')
            print(' 1  Menampilkan Data buku')
            print(' 2  Menambahkan Data buku')
            print(' 3  Mengubah Data buku')
            print(' q  Untuk Balik kebelakang')
            try:
                print('')
                p = input('pilih menu 1-3 atau q: ')
                if p == 'q':
                    Menu.clear_screen()
                    break
                else:
                    p = int(p)

                    if p == 1:
                        Menu.clear_screen()
                        Buku.listBuku()
                        print('     Menu Perpustakaan > Data Buku > Menampilkan Data Buku')
                        print('--------------------------------------------------------------')
                        Buku.menampilkan_buku()
                        Menu.kembali()
                    elif p == 2:
                        Menu.clear_screen()
                        Buku.tambah()
                    elif p == 3:
                        Menu.clear_screen()
                        Buku.listBuku()
                        Buku.ubah()
            except ValueError:
                print('Masukan sesuai perintah')
                Menu.kembali()

    
    def menu_data_peminjaman():
        while(True):
            Menu.clear_screen()
            print('     Menu Perpustakaan > Data Peminjaman >  ')
            print('----------------------------------------------')
            print(' 1  Menampilkan Data Peminjaman')
            print(' 2  Menambahkan Data Peminjaman')
            print(' q  Untuk Balik kebelakang')
            try:
                print('')
                p = input('pilih menu 1-2 atau q: ')
                if p == 'q':
                    Menu.clear_screen()
                    break
                else:
                    p = int(p)

                    if p == 1:
                        Menu.clear_screen()
                        Buku.listPeminjam()
                        print('     Menu Perpustakaan > Data Peminjaman >  Menampilkan Data Peminjaman')
                        print('--------------------------------------------------------------------------')
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
        # menyimpan identitas buku
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
        # Menyimpan data peminjam
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
                        buku_dipinjam.append(a.split(','))
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
            'Buku dipinjam' : [','.join(map(str,book)) for book in buku_dipinjam],
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
                print('--------------------------------------------------------------------------')
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
                print('--------------------------------------------------------------------------')
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
            print('---------------------------------------------------------------------------')
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
                                print('---------------------------------------------------------------------------')
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

                                    with open(d, 'a+') as f: # Mencatat Data Peminjaman
                                        f.write(Name +  '.' + ','.join(str(x) for x in buku_dipinjam) + '.' + Menu.getDate() + '\n')

                                    with open(r'buku.txt', 'r+') as f: # Memperbarui isi file buku.txt pada listBuku
                                        for i in range(len(judul_buku)):
                                            if i != len(judul_buku) - 1:
                                                f.write(judul_buku[i] + ',' + pengarang[i] + ',' + str(jumlah_stok[i]) + '\n')
                                            else:
                                                f.write(judul_buku[i] + ',' + pengarang[i] + ',' + str(jumlah_stok[i]))

                                    print('Data Peminjaman ' + Name + ' sudah tersimpan')
                                    print('     Menu Perpustakaan > Data Pengembalian > ', nama)
                                    print('------------------------------------------------------------------------')
                                    print('====================================================================================================')
                                    print('Data Peminjaman ' + Name + ' sudah tersimpan')
                                    print('====================================================================================================')

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
        done = False
        while done == False: # Memasukkan nama depan peminjam
            print('     Menu Perpustakaan > Data Pengembalian > ')
            print('----------------------------------------------')
            if Buku.menampilkan_peminjam() == 'kosong':
                print('Tidak bisa melanjutkan karena data peminjaman kosong')
                Menu.kembali()
                break
            else:
                print('Masukkan q Untuk Balik Kebelakang')
                print('Pilih salah satu menu di diatas (masukkan nomor urutan):')

                try:
                    k = input('')
                    if k == 'q':
                        Menu.clear_screen()
                        break
                    else:
                        k = int(k)

                    nama = nama_peminjam[k] # Cek

                    # Denda
                    tgl_peminjam = datetime.datetime.strptime(tanggal_dipinjam[k], '%Y-%m-%d')
                    dua_minggu = tgl_peminjam + datetime.timedelta(weeks=2)
                    today = datetime.datetime.strptime(Menu.getDate(), '%Y-%m-%d')
                    if dua_minggu < today:
                        denda = True
                        diff = today - dua_minggu
                        hari_keterlambatan = diff.days
                        byr_denda = 500 * hari_keterlambatan
                    else:
                        denda = False


                    while type(k) == int:
                        Menu.clear_screen()
                        print('     Menu Perpustakaan > Data Pengembalian > ', nama)
                        print('------------------------------------------------------------------------')
                        print('====================================================================================================')
                        print('Nama Peminjam        : ', nama_peminjam[k])
                        print('Buku dipinjam        : ',  ','.join(str(book) for book in buku_dipinjam[k]))
                        print('Tanggal Peminjaman   : ', tanggal_dipinjam[k])
                        print('Tanggal Pengembalian : ', Menu.getDate())
                        print('====================================================================================================')
                        print('Masukkan y untuk mengembalikkan buku')
                        print('Masukkan q untuk balik kebelakang')
                        u = str(input('Masukkan input : '))

                        if u == 'y': # untuk melanjutkan pengembalian
                            if denda == True: # tampilan denda
                                while(True):
                                    Menu.clear_screen()
                                    print('     Menu Perpustakaan > Data Pengembalian > ', nama)
                                    print('----------------------------------------------------------------')
                                    print('====================================================================================================')
                                    print('Nama Peminjam        : ', nama_peminjam[k])
                                    print('Buku dipinjam        : ',  ','.join(str(book) for book in buku_dipinjam[k]))
                                    print('Tanggal Peminjaman   : ', tanggal_dipinjam[k])
                                    print('Tanggal Pengembalian : ', Menu.getDate())
                                    print('Terlambat            : ', str(hari_keterlambatan), ' Hari')
                                    print('Terkena Denda        : ', 'Rp',str(byr_denda))
                                    print('====================================================================================================')
                                    print('Masukkan q untuk balik kebelakang')
                                    try:
                                        byr = input('Masukkan nominal pembayaran : ')
                                        if byr == 'q':
                                            Menu.clear_screen()
                                            break
                                        else:
                                            byr = int(byr)
                                            if byr < byr_denda:
                                                print('Nominal uang kurang !')
                                                Menu.kembali()
                                            else:
                                                Menu.clear_screen()
                                                total = byr_denda - byr
                                                print('     Menu Perpustakaan > Data Pengembalian > ', nama)
                                                print('----------------------------------------------------------------')
                                                print('====================================================================================================')
                                                print('Nama Peminjam        : ', nama_peminjam[k])
                                                print('Buku dipinjam        : ',  ','.join(str(book) for book in buku_dipinjam[k]))
                                                print('Tanggal Peminjaman   : ', tanggal_dipinjam[k])
                                                print('Tanggal Pengembalian : ', Menu.getDate())
                                                print('Terlambat            : ', str(hari_keterlambatan), ' Hari')
                                                print('Terkena Denda        : ', 'Rp',str(byr_denda))
                                                print('Dibayar sebesar      : ', 'Rp',str(byr))
                                                print('Sisa                 : ', 'Rp',str(total))
                                                print('====================================================================================================')
                                                denda = None
                                                success = True
                                                input('Masukkan apa saja untuk melanjutkan pengembalian buku')
                                    except ValueError:
                                        print('Masukkan sesuai perintah!')
                                        Menu.kembali()
                            else:
                                Menu.clear_screen()
                                success = True
                            
                        elif u == 'q': # untuk keluar
                            Menu.clear_screen()
                            break
                        else:
                            print('Masukkan sesuai perintah !')
                            Menu.kembali()



                        while success == True:
                            # Mengembalikan buku ke list stok
                            for y in range(len(buku_dipinjam[k])):
                                for i in range(len(judul_buku)):
                                    if buku_dipinjam[k][y] == judul_buku[i]:
                                        jumlah_stok[i] = int(jumlah_stok[i]) + 1
                                        jumlah_stok[i] = str(jumlah_stok[i])
                                        break

                            nama_peminjam.remove(nama_peminjam[k]) # Menghapus nama peminjam di data list
                            buku_dipinjam.remove(buku_dipinjam[k]) # Menghpaus buku dari peminjam
                            tanggal_dipinjam.remove(tanggal_dipinjam[k]) # Menghapus tanggal peminjam di data list

                            with open(r'Data-Peminjaman.txt', 'r') as f: # Mencatat Data Peminjaman
                                lines = f.readlines()
                            del lines[k]

                            with open(r'Data-Peminjaman.txt', 'w') as f: # Mencatat Data Peminjaman
                                f.writelines(lines)
                            f.close()
                            os.truncate('Data-Peminjaman.txt', os.path.getsize('Data-Peminjaman.txt'))


                            with open(r'Buku.txt', 'r+') as f: # Memperbarui isi file buku.txt pada listBuku
                                for i in range(len(judul_buku)):
                                    if i != len(judul_buku) - 1:
                                        f.write(judul_buku[i] + ',' + pengarang[i] + ',' + str(jumlah_stok[i]) + '\n')
                                    else:
                                        f.write(judul_buku[i] + ',' + pengarang[i] + ',' + str(jumlah_stok[i]))

                            print('     Menu Perpustakaan > Data Pengembalian > ', nama)
                            print('------------------------------------------------------------------------')
                            print('====================================================================================================')
                            print('Pengembalian atas nama ' , nama, ' berhasil dilakukan.')
                            print('====================================================================================================')
                            
                            Menu.kembali()
                            success = None
                            k = None

                except IndexError:
                    print('Pilih salah satu nomor diatas')
                    Menu.kembali()
                except ValueError:
                    print('Masukkan nomor dari daftar Peminjam')
                    Menu.kembali()

        
    def tambah():# Untuk menambah data Buku
        loop_judul = False
        loop_pengarang = False
        loop_stok = False
        success = False

        judul = None
        pengarang = None
        stok = None
        while success == False:# perulangan identifikasi data
            while loop_judul == False:# Memasukan data judul buku
                    
                print('     Menu Perpustakaan > Data Buku > Menambahkan Data Buku')
                print('--------------------------------------------------------------')
                print('====================================================================================================')
                print('Judul buku : ', judul)
                print('Pengarang  : ', pengarang)
                print('Stok       : ', stok)
                print('====================================================================================================')
                judul = input("Masukkan judul Buku : ")

                Menu.clear_screen()

                while(True):# Menanyakan apakah yang di input sudah benar
                    print('     Menu Perpustakaan > Data Buku > Menambahkan Data Buku')
                    print('--------------------------------------------------------------')
                    print('====================================================================================================')
                    print('Judul buku : ', judul)
                    print('Pengarang  : ', pengarang)
                    print('Stok       : ', stok)
                    print('====================================================================================================')
                    print('Apakah nama Judul ' + judul + ' sudah benar?')
                    q = input('y atau n ? : ')
                    if q == 'y':
                        loop_judul = True
                        Menu.clear_screen()
                        break
                    elif q == 'n':
                        judul = None
                        Menu.clear_screen()
                        break
                    else:
                        print('Masukan y atau n saja')
                        Menu.kembali()
                        continue

            while loop_pengarang== False:# Memasukan data buku si pengarang
                print('     Menu Perpustakaan > Data Buku > Menambahkan Data Buku')
                print('--------------------------------------------------------------')
                print('====================================================================================================')
                print('Judul buku : ', judul)
                print('Pengarang  : ', pengarang)
                print('Stok       : ', stok)
                print('====================================================================================================')
                pengarang = input("Masukkan nama Pengarang : ")
                Menu.clear_screen()

                while(True):# Menanyakan apakah memasukan pengarang itu sudah benar  
                    print('     Menu Perpustakaan > Data Buku > Menambahkan Data Buku')
                    print('-----------------------------------------------------------')
                    print('====================================================================================================')
                    print('Judul buku : ', judul)
                    print('Pengarang  : ', pengarang)
                    print('Stok       : ', stok)
                    print('====================================================================================================')
                    print('Apakah nama Pengarang ' + pengarang + ' sudah benar?')
                    q = input('y atau n ? : ')
                    if q == 'y':
                        loop_pengarang = True
                        Menu.clear_screen()
                        break
                    elif q == 'n':
                        pengarang = None
                        Menu.clear_screen()
                        break
                    else:
                        print('Masukan y atau n saja')
                        Menu.kembali()
                        continue

            while loop_stok == False:# Memasukkan data buku stok
                print('     Menu Perpustakaan > Data Buku > Menambahkan Data Buku')
                print('--------------------------------------------------------------')
                print('====================================================================================================')
                print('Judul buku : ', judul)
                print('Pengarang  : ', pengarang)
                print('Stok       : ', stok)
                print('====================================================================================================')
                try:
                    stok = int(input("Masukkan jumlah Stok : "))
                    Menu.clear_screen()
                except ValueError:
                    print('')
                    print('Masukan nominal Stok!')
                    Menu.kembali()
                    continue


                while(True):
                    print('     Menu Perpustakaan > Data Buku > Menambahkan Data Buku')
                    print('--------------------------------------------------------------')
                    print('====================================================================================================')
                    print('Judul buku : ', judul)
                    print('Pengarang  : ', pengarang)
                    print('Stok       : ', stok)
                    print('====================================================================================================')
                    print('Apakah pemasukan data dengan stok ' + str(stok) + ' sudah benar?')
                    q = input('y atau n ? : ')
                    if q == 'y':
                        loop_stok= True
                        Menu.clear_screen()
                        break
                    elif q == 'n':
                        stok = None
                        Menu.clear_screen()
                        break
                    else:
                        print('Masukan y atau n saja')
                        Menu.kembali()
                        continue
            
            
            while(True): # Bertanya apakah data yang dimasukan sudah benar?
                Menu.clear_screen()
                print('     Menu Perpustakaan > Data Buku > Menambahkan Data Buku')
                print('--------------------------------------------------------------')
                print('====================================================================================================')
                print('Judul buku : ', judul)
                print('Pengarang  : ', pengarang)
                print('Stok       : ', stok)
                print('====================================================================================================')
                print('Apakah Data Buku yang di masukkan tersebut sudah benar?')
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
                print('     Menu Perpustakaan > Data Buku > Menambahkan Data Buku')
                print('--------------------------------------------------------------')
                print('====================================================================================================')
                print('Apa yang salah?')
                print('Masukan j untuk Judul     : ' + judul)
                print('Masukan p untuk Pengarang : ' + pengarang)
                print('Masukan s untuk stok      : ' + str(stok))
                print('====================================================================================================')
                ask = input('Masukkan input [j/p/s] ? : ')
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
                print('     Menu Perpustakaan > Data Buku > Mengubah Data Buku')
                print('-----------------------------------------------------------')
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
                        print('     Menu Perpustakaan > Data Buku > Mengubah Data Buku')
                        print('-----------------------------------------------------------')
                        print('====================================================================================================')
                        print('Masukan j untuk Judul       : ' + judul_buku[data])
                        print('Masukan p untuk Pengarang   : ' + pengarang[data])
                        print('Masukan s untuk jumlah stok : ' + str(jumlah_stok[data]))
                        print('====================================================================================================')
                        print('Masukan q jika ingin balik ke belakang')
                        ubah = str(input('Pilih apa yang diubah ?  : '))

                        if ubah == 'q':
                            loop_ubah = True
                            Menu.clear_screen()
                            break

                        elif ubah == 'j':

                            while ubah == 'j':# Mengganti nama judul
                                Menu.clear_screen()
                                print('     Menu Perpustakaan > Data Buku > Mengubah Data Buku')
                                print('-----------------------------------------------------------')
                                print('====================================================================================================')
                                print('Masukan j untuk Judul       : ' + judul_buku[data])
                                print('Masukan p untuk Pengarang   : ' + pengarang[data])
                                print('Masukan s untuk jumlah stok : ' + str(jumlah_stok[data]))
                                print('====================================================================================================')
                                print('Masukan q jika ingin balik ke menu awal')
                                menjadi = input('Masukan nama judul baru : ')

                                if menjadi == 'q':
                                    ubah = None
                                    Menu.clear_screen()
                                    break

                                while(True): # Menanya benar atau tidak
                                    Menu.clear_screen()
                                    print('     Menu Perpustakaan > Data Buku > Mengubah Data Buku')
                                    print('-----------------------------------------------------------')
                                    print('====================================================================================================')
                                    print('Masukan j untuk Judul       : ' + judul_buku[data])
                                    print('Masukan p untuk Pengarang   : ' + pengarang[data])
                                    print('Masukan s untuk jumlah stok : ' + str(jumlah_stok[data]))
                                    print('====================================================================================================')
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
                                print('     Menu Perpustakaan > Data Buku > Mengubah Data Buku')
                                print('-----------------------------------------------------------')
                                print('====================================================================================================')
                                print('Masukan j untuk Judul       : ' + judul_buku[data])
                                print('Masukan p untuk Pengarang   : ' + pengarang[data])
                                print('Masukan s untuk jumlah stok : ' + str(jumlah_stok[data]))
                                print('====================================================================================================')
                                print('Masukan q jika ingin balik ke menu awal')
                                menjadi = input('Masukan nama pengarang baru : ')

                                if menjadi == 'q':
                                    ubah = None
                                    Menu.clear_screen()
                                    break

                                while(True): # Menanya benar atau tidak
                                    Menu.clear_screen()
                                    print('     Menu Perpustakaan > Data Buku > Mengubah Data Buku')
                                    print('-----------------------------------------------------------')
                                    print('====================================================================================================')
                                    print('Masukan j untuk Judul       : ' + judul_buku[data])
                                    print('Masukan p untuk Pengarang   : ' + pengarang[data])
                                    print('Masukan s untuk jumlah stok : ' + str(jumlah_stok[data]))
                                    print('====================================================================================================')
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
                                print('     Menu Perpustakaan > Data Buku > Mengubah Data Buku')
                                print('-----------------------------------------------------------')
                                print('====================================================================================================')
                                print('Masukan j untuk Judul       : ' + judul_buku[data])
                                print('Masukan p untuk Pengarang   : ' + pengarang[data])
                                print('Masukan s untuk jumlah stok : ' + str(jumlah_stok[data]))
                                print('====================================================================================================')
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
                                    print('     Menu Perpustakaan > Data Buku > Mengubah Data Buku')
                                    print('-----------------------------------------------------------')
                                    print('====================================================================================================')
                                    print('Masukan j untuk Judul       : ' + judul_buku[data])
                                    print('Masukan p untuk Pengarang   : ' + pengarang[data])
                                    print('Masukan s untuk jumlah stok : ' + str(jumlah_stok[data]))
                                    print('====================================================================================================')
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
