class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data_mahasiswa = []

    def tambah(self, nama, nilai):
        self.data_mahasiswa.append({'nama': nama, 'nilai': nilai})
        print("=" * 30)
        print(f"|    Data mahasiswa '{nama}' berhasil ditambahkan :)    |")
        print("=" * 30)

    def tampilkan(self):
        if not self.data_mahasiswa:
            print("Tidak ada data mahasiswa.")
        else:
            print("\nDaftar Nilai Mahasiswa:")
            for i, mhs in enumerate(self.data_mahasiswa, start=1):
                print(f"{i}. Nama: {mhs['nama']}, Nilai: {mhs['nilai']}")

    def hapus(self, nama):
        for mhs in self.data_mahasiswa:
            if mhs['nama'] == nama:
                self.data_mahasiswa.remove(mhs)
                print(f"Data mahasiswa '{nama}' berhasil dihapus.")
                return
        print(f"Data mahasiswa dengan nama '{nama}' tidak ditemukan.")

    def ubah(self, nama, nilai_baru):
        for mhs in self.data_mahasiswa:
            if mhs['nama'] == nama:
                mhs['nilai'] = nilai_baru
                print(f"Data mahasiswa '{nama}' berhasil diubah.")
                return
        print(f"Data mahasiswa dengan nama '{nama}' tidak ditemukan.")


if __name__ == "__main__":
    daftar = DaftarNilaiMahasiswa()

    while True:
        
        print("\n        MENU        ")
        print("=" * 20)
        print("| 1. Tambah data   |")
        print("| 2. Tampilkan data|")
        print("| 3. Hapus data    |")
        print("| 4. Ubah data     |")
        print("| 5. Keluar        |")
        print("=" * 20)
        
        pilihan = input("Pilih Nomor Menu (1 - 5): ")

        if pilihan == "1":
            nama = input("Masukkan nama: ")
            nilai = float(input("Masukkan nilai: "))
            daftar.tambah(nama, nilai)
        elif pilihan == "2":
            daftar.tampilkan()
        elif pilihan == "3":
            nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
            daftar.hapus(nama)
        elif pilihan == "4":
            nama = input("Masukkan nama mahasiswa yang akan diubah: ")
            nilai_baru = float(input("Masukkan nilai baru: "))
            daftar.ubah(nama, nilai_baru)
        elif pilihan == "5":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
