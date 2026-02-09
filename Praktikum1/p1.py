#==============================================
#Praktikum 1: Konsep file ADT dan file handling
#Latihan Dasar 1: Membaca seluruh isi file data
#==============================================

print("=== Membuka file dalam satu string ===")
with open("data.txt", "r", encoding="utf-8") as file:
    isi_file = print(file.read())
print(isi_file)
print("=== Hasil Read ===")
print("Tipe data: ", type(isi_file))

#==============================================
#Praktikum 1: Konsep file ADT dan file handling
#Latihan Dasar 2: Membaca file per baris
#==============================================

print("=== Membuka file per baris ===")
jumlah_baris = 0 #INISIALISASI VARIABEL UNTUK MENGHITUNG JUMLAH BARIS
with open("data.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #MENGHILANGKAN BARIS BARU
        print("Baris ke- ", jumlah_baris)
        print("Isinya: ", baris)

#================================================
#Praktikum 1: Konsep file ADT dan file handling
#Latihan Dasar 3: Menampilkan list dengan parsing
#================================================

data_list = [] #INISIALISASI LIST UNTUK MENAMPUNG DATA

#PARSING BARIS MENJADI DATA SATUAN DAN MENAMPILKANNYA DALAM BENTUK KOLOM-KOLOM DATA
with open("data.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        print("NIM: ", nim, "| Nama: ", nama, "| Nilai: ", nilai)
        data_list.append([nim,nama,int(nilai)])

print("=== Menampilkan list ===")
print(data_list)
print("Contoh record ke 1:", data_list[0])
print("Contoh record ke 2:", data_list[1])
print("Jumlah record", len(data_list))

#====================================================
#Praktikum 1: Konsep file ADT dan file handling
#Latihan Dasar 4: Menampilkan dictionary dengan slice
#====================================================

data_dict = {}
with open("data.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #MENGHILANGKAN KARAKTER BARIS BARU
        nim, nama, nilai = baris.split(",") #PECAH MENJADI DATA SATUAN DAN SIMPAN KE VARIABEL
        #SIMPAN DATA DALAM DICTIONARY {KEY, VALUE}
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai)
        }

print("=== Menampilkan Data Dictionary ===")
print(data_dict)