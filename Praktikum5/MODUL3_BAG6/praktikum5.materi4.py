#===============================================
# Nama: Diaz Ramaananta Harahap
# NIM: J0403251048
# Kelas: A/P1
#===============================================

#===============================================
# Materi 4 = Kombinasi Biner - Backtracking 1
#===============================================

def biner(n, hasil=""): #Membuat fungsi backtracking
    #Base case: Jika panjang string sudah sama dengan nilai n, maka print hasilnya
    if len(hasil) == n: 
        print(hasil) 
        return 
    
    #Choose + Explore: tambah '0' 
    biner(n, hasil + "0") 
  
    #Choose + Explore: tambah '1'
    biner(n, hasil + "1") 
 
#Memanggil fungsi biner
biner(3) 
#Output:
'''
    000
    001
    010
    011
    100
    101
    110
    111
'''