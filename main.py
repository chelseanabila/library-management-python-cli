from buku import Buku, BukuFiksi, BukuNonFiksi
from anggota import Anggota
from peminjaman import Peminjaman

# Penyimpanan data sementara (list of object)
daftar_buku = []
daftar_anggota = []
daftar_pinjam = []


def data_awal():
    """Data contoh agar program langsung bisa dicoba."""
    daftar_buku.append(BukuFiksi("B001", "Laskar Pelangi", "Andrea Hirata", 3,
                                 "Novel", "Ikal", 26))
    daftar_buku.append(BukuNonFiksi("B002", "Algoritma dan Pemrograman", "Rinaldi Munir", 2,
                                    "Informatika", "Kuliah", "Ke-6"))
    daftar_anggota.append(Anggota("A001", "Budi", "Teknik Informatika"))


def input_angka(pesan):
    """Validasi input angka agar program tidak crash."""
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Masukkan angka yang valid.")


def cari_buku(kode):
    for b in daftar_buku:
        if b.get_kode().lower() == kode.lower():
            return b
    return None


def cari_anggota(id_anggota):
    for a in daftar_anggota:
        if a.get_id().lower() == id_anggota.lower():
            return a
    return None


#TAMBAH DATA
def tambah_data():
    print("\n-- TAMBAH DATA --")
    print("1. Buku Fiksi\n2. Buku Non-Fiksi\n3. Anggota\n4. Peminjaman")
    pilih = input("Pilih: ")

    if pilih in ("1", "2"):
        kode = input("Kode buku : ")
        if cari_buku(kode):
            print("Kode buku sudah ada.")
            return
        judul = input("Judul     : ")
        penulis = input("Penulis   : ")
        stok = input_angka("Stok      : ")
        if pilih == "1":
            genre = input("Genre       : ")
            tokoh = input("Tokoh utama : ")
            bab = input_angka("Jumlah bab  : ")
            daftar_buku.append(BukuFiksi(kode, judul, penulis, stok, genre, tokoh, bab))
        else:
            bidang = input("Bidang  : ")
            tingkat = input("Tingkat : ")
            edisi = input("Edisi   : ")
            daftar_buku.append(BukuNonFiksi(kode, judul, penulis, stok, bidang, tingkat, edisi))
        print("  Buku berhasil ditambahkan.")

    elif pilih == "3":
        id_a = input("ID anggota : ")
        if cari_anggota(id_a):
            print("ID anggota sudah ada.")
            return
        nama = input("Nama       : ")
        prodi = input("Prodi      : ")
        daftar_anggota.append(Anggota(id_a, nama, prodi))
        print("Anggota berhasil ditambahkan.")

    elif pilih == "4":
        anggota = cari_anggota(input("ID anggota : "))
        buku = cari_buku(input("Kode buku  : "))
        if anggota is None or buku is None:
            print("Anggota atau buku tidak ditemukan.")
        elif not anggota.boleh_meminjam():
            print("Anggota sudah meminjam 3 buku (batas maksimal).")
        elif not buku.kurangi_stok():
            print("Stok buku habis.")
        else:
            anggota.tambah_pinjaman()
            id_p = f"P{len(daftar_pinjam) + 1:03d}"
            daftar_pinjam.append(Peminjaman(id_p, anggota, buku))
            print(f"  Peminjaman {id_p} berhasil dicatat.")
    else:
        print("Pilihan tidak valid.")


#TAMPILKAN DATA 
def tampilkan_data():
    print("\n== DAFTAR BUKU ==")
    for b in daftar_buku:
        print(" ", b.info()) 
    print("\n== DAFTAR ANGGOTA ==")
    for a in daftar_anggota:
        print(" ", a.info())
    print("\n== DAFTAR PEMINJAMAN ==")
    if not daftar_pinjam:
        print("  (belum ada peminjaman)")
    for p in daftar_pinjam:
        print(" ", p.info())


#CARI DATA
def cari_data():
    print("\n-- CARI DATA --")
    kata = input("Kata kunci (judul/penulis buku atau nama anggota): ").lower()
    ketemu = False
    for b in daftar_buku:
        if kata in b.get_judul().lower() or kata in b.get_penulis().lower():
            print(" ", b.info())
            ketemu = True
    for a in daftar_anggota:
        if kata in a.get_nama().lower():
            print(" ", a.info())
            ketemu = True
    if not ketemu:
        print("  Data tidak ditemukan.")


#UBAH DATA
def ubah_data():
    print("\n-- UBAH DATA --")
    print("1. Buku\n2. Anggota")
    pilih = input("Pilih: ")
    if pilih == "1":
        b = cari_buku(input("Kode buku : "))
        if b is None:
            print("Buku tidak ditemukan.")
            return
        print("  (kosongkan jika tidak ingin diubah)")
        judul = input("Judul baru   : ")
        penulis = input("Penulis baru : ")
        stok_txt = input("Stok baru    : ")
        stok = int(stok_txt) if stok_txt.isdigit() else None
        b.ubah_data(judul, penulis, stok)
        print("Data buku diperbarui.")
    elif pilih == "2":
        a = cari_anggota(input("ID anggota : "))
        if a is None:
            print("Anggota tidak ditemukan.")
            return
        print("  (kosongkan jika tidak ingin diubah)")
        a.ubah_data(input("Nama baru  : "), input("Prodi baru : "))
        print("Data anggota diperbarui.")
    else:
        print("Pilihan tidak valid.")


#CEK STATUS DATA
def cek_status():
    print("\n--CEK STATUS--")
    print("1.Status ketersediaan buku\n2.Status peminjaman")
    pilih = input("Pilih: ")
    if pilih == "1":
        b = cari_buku(input("Kode buku : "))
        if b:
            print("Buku", "TERSEDIA" if b.tersedia() else "HABIS", "-", b.get_judul(),
                  f"(stok {b.get_stok()})")
        else:
            print("Buku tidak ditemukan.")
    elif pilih == "2":
        kode = input("ID peminjaman : ").lower()
        for p in daftar_pinjam:
            if p.get_id().lower() == kode:
                print(" ", p.info())
                return
        print("Peminjaman tidak ditemukan.")
    else:
        print("Pilihan tidak valid.")


#PENGEMBALIAN
def kembalikan_buku():
    print("\n-- PENGEMBALIAN BUKU --")
    kode = input("ID peminjaman : ").lower()
    for p in daftar_pinjam:
        if p.get_id().lower() == kode:
            if p.kembalikan():
                print("Buku dikembalikan. Denda: Rp{:,}".format(p.hitung_denda()))
            else:
                print("Buku sudah pernah dikembalikan.")
            return
    print("Peminjaman tidak ditemukan.")


#MENU UTAMA 
def main():
    data_awal()
    while True:
        print("\n===== APLIKASI MANAJEMEN PERPUSTAKAAN =====")
        print("1. Tambah data")
        print("2. Tampilkan data")
        print("3. Cari data")
        print("4. Ubah data")
        print("5. Cek status data")
        print("6. Pengembalian buku")
        print("0. Keluar")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            tambah_data()
        elif pilih == "2":
            tampilkan_data()
        elif pilih == "3":
            cari_data()
        elif pilih == "4":
            ubah_data()
        elif pilih == "5":
            cek_status()
        elif pilih == "6":
            kembalikan_buku()
        elif pilih == "0":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Menu tidak valid.")


if __name__ == "__main__":
    main()