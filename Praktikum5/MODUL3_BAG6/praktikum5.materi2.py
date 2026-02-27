#===============================================
# Nama: Diaz Ramaananta Harahap
# NIM: J0403251048
# Kelas: A/P1
#===============================================

#===============================================
# Materi 2 = Tracking Masuk/Keluar
#===============================================

def hitung(n): #Membuat fungsi untuk tracking masuk/keluar
    #Base case: Kondisi jika n sudah mencapai 0 maka tracking selesai
    if n == 0: 
        print("Selesai!")
        return
    
    print("Masuk", n) #Fase stacking
    hitung(n - 1) #Pemanggilan rekursif
    print("Keluar", n) #Fase unwilding

#Memanggila fungsi hitung
hitung(3) 
#Output: 
'''
    Masuk 3
    Masuk 2 
    Masuk 1 
    Selesai!
    Keluar 1
    Keluar 2
    Keluar 3
'''