#===============================================
# Nama: Diaz Ramaananta Harahap
# NIM: J0403251048
# Kelas: A/P1
#===============================================

#============================
# Latihan 2: Tracking Rekursi 
#============================

def countdown(n): #Membuat fungsi tracking rekursi
    #Base case: Jika nilai n sudah mencapai 0, maka program selesai lalu keluar
    if n == 0: 
        print("Selesai") 
        return 
 
    print("Masuk:", n) #Fase stacking
    
    #Recursive call: Nilai n saat ini dikurang dengan 1
    countdown(n - 1) 
 
    print("Keluar:", n) #Fase unwilding
 
#Memanggil fungsi countdown
countdown(3)
#Output:
'''
    Masuk: 3
    Masuk: 2 
    Masuk: 1 
    Selesai  
    Keluar: 1
    Keluar: 2
    Keluar: 3
'''

#=================================================================================================================
# Pertanyaan: Mengapa output 'keluar' muncul terbailk?
'''
    Jawaban: Saat countdown(3) dijalankan, program mencetak "masuk" sambil terus memanggil dirinya sendiri dengan nilai yang lebih kecil hingga mencapai 0. Setelah sampai pada kondisi berhenti, barulah fungsi mulai kembali ke pemanggilan sebelumnya. Karena rekursi bekerja seperti tumpukan, maka bagian “keluar” dicetak dari pemanggilan terakhir ke awal.
'''
#=================================================================================================================
