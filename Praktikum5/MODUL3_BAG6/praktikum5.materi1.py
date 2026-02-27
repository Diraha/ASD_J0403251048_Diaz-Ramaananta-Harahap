#===============================================
# Nama: Diaz Ramaananta Harahap
# NIM: J0403251048
# Kelas: A/P1
#===============================================

#===============================================
# Materi 1 = Faktorial
#===============================================

def faktorial(n): #Membuat fungsi untuk menghitung nilai faktorial
    #Base case: Jika nilai n sudah 0, maka kembalikan nilai 1
    if n == 0: 
        return 1
    #Recursive case: Memanggil kembali fungsi dengan nilai n - 1 untuk membuat efek perhitungan faktorial
    return n * faktorial(n - 1) 

#Memanggil fungsi faktorial
print(faktorial(5))
#Output: 120