#===============================================
# Nama: Diaz Ramaananta Harahap
# NIM: J0403251048
# Kelas: A/P1
#===============================================

#===============================================
# Materi 3 = Menjumlahkan Elemen List
#===============================================

def jumlah_list(data, index=0): #Mmebuat fungsi untuk menghitung jumlah list
    #Base case: Jika index-nya sudah mencapai panjang data, maka kembalikan nilai 0
    if index == len(data): 
        return 0

    #Recursive case: Elemen sekarang + jumlah elemen setelahnya
    return data[index] + jumlah_list(data, index + 1) 

#Memanggil fungsi jumlah_list dan mengirimkan parameter berupa list angka
print(jumlah_list([2, 4, 6, 8]))
#Output: 20