#===============================================
# Nama: Diaz Ramaananta Harahap
# NIM: J0403251048
# Kelas: A/P1
#===============================================

#===========================================================
# Materi 5 = Kombinasi Biner dengan Pruning - Backtracking 2
#===========================================================

def biner_batas(n, batas, hasil="", jumlah_1=0): #Membuat fungsi backtracking dengan pruning
    #Pruning: Jika jumlah_1 sudah melewati batas, berhenti/keluar dari fungsi
    if jumlah_1 > batas: 
        return
    
    #Base case
    if len(hasil) == n:
        print(hasil)
        return

    #Pilih '0'
    biner_batas(n, batas, hasil + "0", jumlah_1)

    #Pilih '1'
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

#Memanggil fungsi biner_batas
biner_batas(4, 2) 
'''
    0000
    0001
    0010
    0011
    0100
    0101
    0110
    1000
    1001
    1010
    1100
'''