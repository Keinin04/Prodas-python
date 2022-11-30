#   Applikasi perpustakaan

import os

def clear():
    os.system('cls')

class Menu:
    def __init__(self, daftar_buku):
        self.daftar_buku = daftar_buku