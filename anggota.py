class Anggota:
    def __init__(self, id_anggota, nama, prodi):
        self.__id = id_anggota
        self.__nama = nama
        self.__prodi = prodi
        self.__jumlah_pinjam = 0  # jumlah buku yang sedang dipinjam

    def get_id(self):
        return self.__id

    def get_nama(self):
        return self.__nama

    def get_prodi(self):
        return self.__prodi

    def get_jumlah_pinjam(self):
        return self.__jumlah_pinjam

    def ubah_data(self, nama=None, prodi=None):
        if nama:
            self.__nama = nama
        if prodi:
            self.__prodi = prodi

    def boleh_meminjam(self, batas=3):
        """Anggota maksimal meminjam 3 buku sekaligus."""
        return self.__jumlah_pinjam < batas

    def tambah_pinjaman(self):
        self.__jumlah_pinjam += 1

    def kurangi_pinjaman(self):
        if self.__jumlah_pinjam > 0:
            self.__jumlah_pinjam -= 1

    def info(self):
        return (f"[{self.__id}] {self.__nama} - {self.__prodi} "
                f"Sedang meminjam: {self.__jumlah_pinjam} buku")