#===============================================
# Nama: Diaz Ramaananta Harahap
# NIM: J0403251048
# Kelas: A/P1
#===============================================

#===============================================
# Latihan 1 = Rekursi Pangkat
#===============================================
 
def pangkat(a, n): #Membuat fungsi pangkat 
    #Base case: Jika index mencapai 0, maka kembalikan nilai 1
    if n == 0: 
        return 1 
    #Recursive case: Elemen sekarang dikali dengan elemen itu sendiri sampai n sudah mencapai 0
    return a * pangkat(a, n - 1) 

#Memanggil fungsi pangkat
print(pangkat(2, 4))
#Output: 16