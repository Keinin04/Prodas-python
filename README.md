Program Perpustakaan
# Tanggal Update 
    06/12/2022
    - memperbarui lokasi file buku dan pinjaman

    05/12/2022
    - update

    04/12/2022
    - menambahkan fungsi tambah buku
    - memperbarui isi buku.txt
    - menambahkan fungsi peminjaman buku
    - menempatkan fungsi pada class nya masing masing
    - pembaruan tampilan menggunakan pandas

    03/12/2022
    - Penambahan input buku

    02/12/2022 
    - Fungsi menu ditampilkan pertama

# Masalah

1. Dibuatnya sebuah konstruktor di dalam class untuk data buku tersebut. Agar lebih memudahkan pemanggilan fungsi nya langsung dari class nya, bukan harus dipanggil fungsi lain(listBuku) 

2. Di fungsi yang di dalamnya membuka(with open) file buku dan file usernya dibuka secara seminimal mungkin, tidak selalu berulang2 (with open terus2an)

3. Di dalam fungsi kembalikanBuku() diganti lama lewat peminjaman tersebut jangan manual, tetapi otomatis dilihat dari jarak lama minjam nya, dicek di file Peminjaman-user tersebut.  