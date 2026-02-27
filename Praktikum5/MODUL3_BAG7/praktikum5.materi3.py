#===============================================
# Nama: Diaz Ramaananta Harahap
# NIM: J0403251048
# Kelas: A/P1
#===============================================

#==================================
# Latihan 3: Mencari Nilai Maksimum 
#==================================
 
def cari_maks(data, index=0): #Membuat fungsi untuk mencari nilai maksimum
    # Base case: Jika index sama dengan panjang data dikurang 1, maka kembalikan nilai data yang sesuai dengan index saat itu
    if index == len(data) - 1: 
        return data[index] 
 
    # Recursive case: Memanggil kembali fungsi casi_maks dengan mengirimkan data saat ini dan index-nya dikurangi 1, lalu simpan ke dalam variabel maks_sisa
    maks_sisa = cari_maks(data, index + 1) 
 
    if data[index] > maks_sisa: #Jika data dengan index tertentu nilainya sudah lebih dari maks_sisa, maka kembalikan nilai saat itu
        return data[index] 
    else: #Jika data dengan index tertentu nilainya kurang dari maks_sisa, maka kembalikan nilai dari maks_sisa
        return maks_sisa 
 

angka = [3, 7, 2, 9, 5] #Menyiapkan data list yang berisi 5 angka

#Memanggil fungsi cari_maks dengan parameter list tadi lalu cetak ke layar
print("Nilai maksimum:", cari_maks(angka))
#Output: Nilai maksimum = 9
