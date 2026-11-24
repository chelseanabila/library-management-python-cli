class Buku:
    """Superclass: merepresentasikan sebuah buku di perpustakaan."""

    #Constructor berparameter
    def __init__(self, kode, judul, penulis, stok):
        # Atribut private (Encapsulation)
        self.__kode = kode
        self.__judul = judul
        self.__penulis = penulis
        self.__stok = stok

    #Getter
    def get_kode(self):
        return self.__kode

    def get_judul(self):
        return self.__judul

    def get_penulis(self):
        return self.__penulis

    def get_stok(self):
        return self.__stok

    #Method khusus untuk mengubah data (pengganti setter)
    def ubah_data(self, judul=None, penulis=None, stok=None):
        # Hanya ubah field yang diisi
        if judul:
            self.__judul = judul
        if penulis:
            self.__penulis = penulis
        if stok is not None:
            self.__stok = stok

    #Method tambahan
    def kurangi_stok(self):
        """Dipanggil saat buku dipinjam. Return True jika berhasil."""
        if self.__stok > 0:
            self.__stok -= 1
            return True
        return False

    def tambah_stok(self):
        """Dipanggil saat buku dikembalikan."""
        self.__stok += 1

    def tersedia(self):
        return self.__stok > 0

    def get_jenis(self):
        return "Umum"

    def denda_per_hari(self):
        """Denda keterlambatan per hari (di-override oleh subclass)."""
        return 1000

    def info(self):
        status = "Tersedia" if self.tersedia() else "Habis"
        return (f"[{self.__kode}] {self.__judul} - {self.__penulis}"
                f"Jenis: {self.get_jenis()}"
                f"Stok: {self.__stok} ({status})")


class BukuFiksi(Buku):
    """Subclass 1: buku fiksi (novel, cerpen, dll)."""

    def __init__(self, kode, judul, penulis, stok, genre, tokoh_utama, jumlah_bab):
        super().__init__(kode, judul, penulis, stok)  # panggil constructor superclass
        self.__genre = genre
        self.__tokoh_utama = tokoh_utama
        self.__jumlah_bab = jumlah_bab

    def get_genre(self):
        return self.__genre

    def get_tokoh_utama(self):
        return self.__tokoh_utama

    def get_jumlah_bab(self):
        return self.__jumlah_bab

    # Override method superclass (polimorfisme)
    def get_jenis(self):
        return "Fiksi"

    def denda_per_hari(self):
        return 1000

    def info(self):
        return (super().info() +
                f"\nGenre: {self.__genre}"
                f"\nTokoh utama: {self.__tokoh_utama}"
                f"\nJumlah bab: {self.__jumlah_bab}")


class BukuNonFiksi(Buku):
    """Subclass 2: buku non-fiksi (referensi, pelajaran, biografi, dll)."""

    def __init__(self, kode, judul, penulis, stok, bidang, tingkat, edisi):
        super().__init__(kode, judul, penulis, stok)
        self.__bidang = bidang
        self.__tingkat = tingkat
        self.__edisi = edisi

    def get_bidang(self):
        return self.__bidang

    def get_tingkat(self):
        return self.__tingkat

    def get_edisi(self):
        return self.__edisi

    def get_jenis(self):
        return "Non-Fiksi"

    #Buku non-fiksi dendanya lebih besar
    def denda_per_hari(self):
        return 2000

    def info(self):
        return (super().info() +
                f"\nBidang: {self.__bidang}"
                f"\nTingkat: {self.__tingkat}"
                f"\nEdisi: {self.__edisi}")