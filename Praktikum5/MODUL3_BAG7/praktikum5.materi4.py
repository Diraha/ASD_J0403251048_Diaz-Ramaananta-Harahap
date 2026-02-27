#===============================================
# Nama: Diaz Ramaananta Harahap
# NIM: J0403251048
# Kelas: A/P1
#===============================================

#===========================
# Latihan 4: Kombinasi Huruf 
#===========================
 
def kombinasi(n, hasil=""): #Membuat fungsi kombinasi huruf
 
    #Base case: Jika panjang string sudah sama dengan nilai n, maka tampilkan isi hasil dan program selesai
    if len(hasil) == n: 
        print(hasil) 
        return 
 
    #Recursive case: Choose + Explore: tambah 'A'
    kombinasi(n, hasil + "A") 
    #Recursive case: Choose + Explore: tambah 'B'
 
#Memanggil fungsi kombinasi
kombinasi(2)
#Output: AA

#=================================================================================================================
# Pertanyaan: Bagaimana jumlah kombinasi yang dihasilkan?
'''
    Jawaban: Fungsi kombinasi(n, hasil="") bekerja dengan cara menambahkan huruf secara bertahap ke dalam string hasil sampai panjangnya sama dengan n. Setiap kali panjang hasil sudah mencapai n, string tersebut dicetak sebagai satu kombinasi. Pada setiap langkah rekursi ada dua kemungkinan pilihan, yaitu menambahkan "A" atau "B".Untuk pemanggilan kombinasi(2), panjang string yang diinginkan adalah 2, dan setiap posisi bisa diisi 2 pilihan huruf. Jadi total kombinasi yang dihasilkan adalah 2^2 = 4.
'''
#=================================================================================================================