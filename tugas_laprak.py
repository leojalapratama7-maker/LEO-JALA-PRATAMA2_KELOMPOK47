# ==========================================
# PROGRAM PENDATAAN TIKET KAI DAOP 4 TAWANG
# WATERMARK: Kelompok 47
# ==========================================

# ==========================================
# PROGRAM PENDATAAN TIKET KAI DAOP 4 TAWANG
# WATERMARK: Kelompok 47
# ==========================================

# ---------------------------------------------------------
# IMPLEMENTASI FUNCTION (RETURN TYPE)
# ---------------------------------------------------------

# 1. Function Return Type Tanpa Parameter
def get_kode_daop():
    """Mengembalikan string kode stasiun secara statis."""
    return "DAOP 4 SMG - TAWANG"

# 2. Function Return Type Berparameter
def hitung_harga_final(harga_dasar, biaya_admin, umur):
    """Mengkalkulasi harga akhir dengan implementasi Nested If."""
    total = harga_dasar + biaya_admin
    
    # Pengkondisian Nested If: Cek rentang usia untuk diskon
    if umur >= 60:
        if umur > 80:
            return total * 0.5  # Diskon 50% lansia prioritas
        else:
            return total * 0.8  # Diskon 20% lansia
    elif umur <= 3:
        return total * 0.1      # Diskon 90% infant
    else:
        return total

# ---------------------------------------------------------
# IMPLEMENTASI CLASS & METHOD (NON-RETURN / VOID TYPE)
# ---------------------------------------------------------

class SistemKAI:
    def __init__(self, nama_petugas):
        self.petugas = nama_petugas
        # Array 1 Dimensi (List)
        self.kelas_kereta = ["Ekonomi", "Bisnis", "Eksekutif"]
        
        # Array 2 Dimensi (Daftar Kereta: Nama, Tujuan, Harga Dasar)
        self.jadwal_kereta = [
            ["Argo Sindoro", "Semarang - Jakarta", 400000],
            ["Joglosemarkerto", "Semarang - Solo", 100000],
            ["Ciremai", "Semarang - Bandung", 250000]
        ]
        
        # Array 2 Dimensi kosong untuk menampung riwayat penumpang
        self.data_penumpang = [] 

    # 1. Method Non-Return Type Tanpa Parameter
    def tampilkan_header(self):
        """Mencetak antarmuka sistem KAI (Void)."""
        print("\n" + "="*65)
        print("   SISTEM PENDATAAN TIKET KAI STASIUN TAWANG - Kelompok 47   ")
        print("="*65)
        print(f"Petugas Loket : {self.petugas}")
        print(f"Kode Stasiun  : {get_kode_daop()}")
        print("-" * 65)
        print("JADWAL KERETA TERSEDIA (DARI ARRAY 2 DIMENSI):")
        
        # Perulangan Nested Loop untuk mencetak Array 2 Dimensi
        for i in range(len(self.jadwal_kereta)):
            print(f"[{i + 1}] ", end="")
            for j in range(len(self.jadwal_kereta[i])):
                print(f"{self.jadwal_kereta[i][j]:<20}", end=" | ")
            print()
        print("-" * 65)

    # 2. Method Non-Return Type Berparameter
    def simpan_data_penumpang(self, nama, umur, kereta, kelas, harga):
        """Menyimpan data penumpang ke dalam Array 2D riwayat (Void)."""
        self.data_penumpang.append([nama, umur, kereta, kelas, harga])
        print("\n[BERHASIL] Data penumpang berhasil dimasukkan ke database KAI.")

    # 3. Method Non-Return Type Tanpa Parameter
    def cetak_laporan(self):
        """Mencetak seluruh data penumpang dari Array 2D secara rapi."""
        print("\n" + "="*70)
        print("            LAPORAN DATA PENUMPANG (ARRAY 2 DIMENSI)            ")
        print("="*70)
        
        # Pengkondisian If tunggal
        if len(self.data_penumpang) == 0:
            print("Belum ada data penumpang yang diinput.")
        else:
            print(f"{'NO':<3} | {'NAMA':<15} | {'UMUR':<4} | {'KERETA':<16} | {'KELAS':<10} | {'HARGA'}")
            print("-" * 70)
            
            # Perulangan For untuk mencetak baris Array 2 Dimensi
            for i in range(len(self.data_penumpang)):
                nama = self.data_penumpang[i][0]
                umur = self.data_penumpang[i][1]
                kereta = self.data_penumpang[i][2]
                kelas = self.data_penumpang[i][3]
                harga = self.data_penumpang[i][4]
                print(f"{i+1:<3} | {nama:<15} | {umur:<4} | {kereta:<16} | {kelas:<10} | Rp {harga:,.0f}")

# ---------------------------------------------------------
# EKSEKUSI PROGRAM UTAMA
# ---------------------------------------------------------
def main():
    print("Selamat datang di Portal Petugas KAI Stasiun Tawang")
    
    # Implementasi Do-While di Python (menjamin minimal eksekusi 1 kali)
    while True:
        nama_petugas = input("Masukkan ID/Nama Petugas (Kelompok 47): ")
        if nama_petugas.strip() != "":
            break
        else:
            print("[ERROR] Nama petugas tidak boleh kosong!")

    # Instansiasi objek
    sistem_kai = SistemKAI(nama_petugas)

    # Perulangan While untuk menu utama
    while True:
        sistem_kai.tampilkan_header()
        print("Menu Sistem:")
        print("1. Input Data Penumpang Baru")
        print("2. Cetak Laporan Penumpang")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")

        # Pengkondisian If-Elif-Else
        if pilihan == '1':
            nama_penumpang = input("Masukkan Nama Penumpang: ")
            try:
                umur_penumpang = int(input("Masukkan Umur: "))
                pilihan_kereta = int(input("Pilih Nomor Kereta (1-3): ")) - 1
                
                # Pengkondisian If-Else memvalidasi jangkauan indeks array
                if 0 <= pilihan_kereta < len(sistem_kai.jadwal_kereta):
                    nama_kereta_dipilih = sistem_kai.jadwal_kereta[pilihan_kereta][0]
                    harga_dasar = sistem_kai.jadwal_kereta[pilihan_kereta][2]
                    
                    print("\nPilihan Kelas (DARI ARRAY 1 DIMENSI):")
                    for i in range(len(sistem_kai.kelas_kereta)):
                        print(f"{i+1}. {sistem_kai.kelas_kereta[i]}")
                    
                    pilihan_kelas = int(input("Pilih Kelas (1/2/3): "))
                    
                    # Pengkondisian Switch Case (Menggunakan Match-Case di Python)
                    match pilihan_kelas:
                        case 1:
                            kelas_dipilih = sistem_kai.kelas_kereta[0]
                            biaya_admin = 2000
                        case 2:
                            kelas_dipilih = sistem_kai.kelas_kereta[1]
                            biaya_admin = 5000
                        case 3:
                            kelas_dipilih = sistem_kai.kelas_kereta[2]
                            biaya_admin = 15000
                        case _:
                            print("[INFO] Pilihan tidak valid, otomatis dialihkan ke kelas Ekonomi.")
                            kelas_dipilih = sistem_kai.kelas_kereta[0]
                            biaya_admin = 2000
                    
                    # Memanggil Function Return Type
                    harga_final = hitung_harga_final(harga_dasar, biaya_admin, umur_penumpang)
                    
                    # Memanggil Method Non-Return Type
                    sistem_kai.simpan_data_penumpang(nama_penumpang, umur_penumpang, nama_kereta_dipilih, kelas_dipilih, harga_final)
                    
                else:
                    print("\n[ERROR] Nomor kereta tidak valid!")
            except ValueError:
                print("\n[ERROR] Harap masukkan data angka yang benar!")

        elif pilihan == '2':
            # Memanggil Method pencetakan tabel
            sistem_kai.cetak_laporan()

        elif pilihan == '3':
            print(f"\nSistem ditutup. Selamat bertugas, {sistem_kai.petugas} dari Kelompok 47.")
            break
            
