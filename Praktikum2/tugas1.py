# ========================================================== 
# TUGAS HANDS-ON MODUL 1 
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt) 
# 
# Nama  : Diaz Ramaananta Harahap
# NIM   : J0403251048
# Kelas : A/A1
# ========================================================== 

# ------------------------------- 
# Konstanta nama file 
# ------------------------------- 
NAMA_FILE = "stok_barang.txt" 

# ------------------------------- 
# Fungsi: Membaca data dari file 
# ------------------------------- 
def baca_stok(nama_file): 
    """ 
    Membaca data stok dari file teks. 
    Format per baris: KodeBarang,NamaBarang,Stok 
    Output: - stok_dict (dictionary) 
    key   = kode_barang 
    value = {"nama": nama_barang, "stok": stok_int} 
    """ 
    stok_dict = {} 

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()
                if baris == "":
                    continue

                kode_barang, nama_barang, stok_int = baris.split(",")
                stok_dict[kode_barang] = {
                    "nama": nama_barang,
                    "stok": int(stok_int)
                }
    except FileNotFoundError:
        print("File tidak ditemukan!")

    return stok_dict 

# ------------------------------- 
# Fungsi: Menyimpan data ke file 
# ------------------------------- 
def simpan_stok(nama_file, stok_dict): 
    """ 
    Menyimpan seluruh data stok ke file teks. 
    Format per baris: KodeBarang,NamaBarang,Stok 
    """ 
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode_barang in stok_dict:
            nama_barang = stok_dict[kode_barang]["nama"]
            stok = stok_dict[kode_barang]["stok"]
            file.write(f"{kode_barang},{nama_barang},{stok}\n")

# ------------------------------- 
# Fungsi: Menampilkan semua data 
# ------------------------------- 
def tampilkan_semua(stok_dict): 
    """ 
    Menampilkan semua barang di stok_dict. 
    """ 
    if not stok_dict:
        print("Stok barang tidak tersedia!")
        return

    print("\n============== DAFTAR BARANG ==============")
    print(f"{'Kode Barang':<8} | {'Nama Barang':<15} | {'Stok Barang':>5}")
    print("-" * 43)

    for kode_barang in stok_dict:
        print(f"{kode_barang:<11} | {stok_dict[kode_barang]['nama']:<15} | {stok_dict[kode_barang]['stok']}")

    print("-" * 43)

# ------------------------------- 
# Fungsi: Cari barang berdasarkan kode 
# ------------------------------- 
def cari_barang(stok_dict): 
    """ 
    Mencari barang berdasarkan kode barang. 
    """ 
    kode_barang = input("Masukkan kode barang: ").strip() 

    if kode_barang in stok_dict:
        data = stok_dict[kode_barang]
        print("\n=== BARANG DITEMUKAN ===")
        print("Kode Barang :", kode_barang)
        print("Nama Barang :", data["nama"])
        print("Stok :", data["stok"])
    else:
        print("Barang tidak ditemukan!")


# ------------------------------- 
# Fungsi: Tambah barang baru 
# ------------------------------- 
def tambah_barang(stok_dict): 
    """ 
    Menambah barang baru ke stok_dict. 
    """ 
    kode_barang = input("Masukkan kode barang baru: ").strip() 

    if kode_barang in stok_dict:
        print("Kode sudah tersedia!")
        return

    nama_barang = input("Masukkan nama barang: ").strip()

    try:
        stok_awal = int(input("Masukkan stok awal: "))
    except ValueError:
        print("Stok harus berupa angka!")
        return

    if stok_awal < 0:
        print("Stok tidak boleh negatif!")
        return

    stok_dict[kode_barang] = {
        "nama": nama_barang,
        "stok": stok_awal
    }

    print("Barang baru berhasil ditambahkan!")

# ------------------------------- 
# Fungsi: Update stok barang 
# ------------------------------- 
def update_stok(stok_dict): 
    """ 
    Mengubah stok barang (tambah atau kurangi). 
    Stok tidak boleh menjadi negatif. 
    """ 
    kode_barang = input("Masukkan kode barang yang ingin diupdate: ").strip()

    if kode_barang not in stok_dict:
        print("Barang tidak ditemukan!")
        return

    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")

    pilihan = input("Masukkan pilihan (1/2): ").strip()

    try:
        jumlah = int(input("Masukkan jumlah: "))
    except ValueError:
        print("Jumlah harus berupa angka!")
        return

    if jumlah < 0:
        print("Jumlah tidak boleh negatif!")
        return

    if pilihan == "1":
        stok_dict[kode_barang]["stok"] += jumlah
        print("Stok berhasil ditambahkan!")

    elif pilihan == "2":
        if stok_dict[kode_barang]["stok"] - jumlah < 0:
            print("Stok tidak boleh menjadi negatif!")
            return
        stok_dict[kode_barang]["stok"] -= jumlah
        print("Stok berhasil dikurangi!")

    else:
        print("Pilihan tidak valid!")
 
 
# ------------------------------- 
# Program Utama 
# ------------------------------- 
def main(): 
    # Membaca data dari file saat program mulai 
    stok_barang = baca_stok(NAMA_FILE) 
 
    while True: 
        print("\n======= MENU STOK KANTIN =======") 
        print("1. Tampilkan semua barang") 
        print("2. Cari barang berdasarkan kode") 
        print("3. Tambah barang baru") 
        print("4. Update stok barang") 
        print("5. Simpan ke file") 
        print("0. Keluar") 
 
        pilihan = input("Pilih menu: ").strip() 
 
        if pilihan == "1": 
            tampilkan_semua(stok_barang) 
 
        elif pilihan == "2": 
            cari_barang(stok_barang) 
 
        elif pilihan == "3": 
            tambah_barang(stok_barang) 
 
        elif pilihan == "4": 
            update_stok(stok_barang) 
 
        elif pilihan == "5": 
            simpan_stok(NAMA_FILE, stok_barang) 
            print("Data berhasil disimpan!") 
 
        elif pilihan == "0": 
            print("Program selesai!") 
            break 
        else: 
            print("Pilihan tidak valid. Silakan coba lagi!") 

# Menjalankan program utama 
if __name__ == "__main__":
    main()