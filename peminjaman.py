from datetime import date, timedelta

class Peminjaman:
    LAMA_PINJAM = 7  # hari

    def __init__(self, id_pinjam, anggota, buku):
        self.__id = id_pinjam
        self.__anggota = anggota          # relasi ke objek Anggota
        self.__buku = buku                # relasi ke objek Buku (bisa Fiksi/NonFiksi)
        self.__tgl_pinjam = date.today()
        self.__tgl_kembali = None         # None = belum dikembalikan

    def get_id(self):
        return self.__id

    def get_anggota(self):
        return self.__anggota

    def get_buku(self):
        return self.__buku

    def get_tgl_pinjam(self):
        return self.__tgl_pinjam

    def get_tgl_kembali(self):
        return self.__tgl_kembali

    def batas_kembali(self):
        return self.__tgl_pinjam + timedelta(days=Peminjaman.LAMA_PINJAM)

    def sudah_kembali(self):
        return self.__tgl_kembali is not None

    def hitung_denda(self, tgl_acuan=None):
        acuan = self.__tgl_kembali or tgl_acuan or date.today()
        telat = (acuan - self.batas_kembali()).days
        return telat * self.__buku.denda_per_hari() if telat > 0 else 0

    def kembalikan(self, tgl=None):
        """Proses pengembalian: update status peminjaman, stok buku, dan anggota."""
        if self.sudah_kembali():
            return False
        self.__tgl_kembali = tgl or date.today()
        self.__buku.tambah_stok()
        self.__anggota.kurangi_pinjaman()
        return True

    def status(self):
        if self.sudah_kembali():
            return "Sudah dikembalikan"
        if date.today() > self.batas_kembali():
            return "TERLAMBAT"
        return "Sedang dipinjam"

    def info(self):
        return (f"[{self.__id}] {self.__anggota.get_nama()} meminjam "
                f"'{self.__buku.get_judul()}'" 
                f"Pinjam: {self.__tgl_pinjam}"
                f"Batas: {self.batas_kembali()}"
                f"Status: {self.status()}"
                f"Denda: Rp{self.hitung_denda():,}")
