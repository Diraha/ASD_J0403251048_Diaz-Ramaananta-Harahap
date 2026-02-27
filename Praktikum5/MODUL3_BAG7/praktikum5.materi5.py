#===============================================
# Nama: Diaz Ramaananta Harahap
# NIM: J0403251048
# Kelas: A/P1
#===============================================

#===========================
# Studi Kasus: Generator PIN 
#===========================
 
def buat_pin(panjang, hasil=""): #Membuat fungsi generator pin
 
    #Base case: Jika panjang string hasil sama dengan nilai variabel panjang, maka tampilkan hasil pin-nya
    if len(hasil) == panjang: 
        print("PIN:", hasil) 
        return 
    
    for angka in ["0", "1", "2"]: #Looping list yang berisi 3 angka
        #Recursive case: Memanggil kembali fungsi buat_pin dengan mengirimkan nilai panjang saat ini dan hasil string + angka
        buat_pin(panjang, hasil + angka) 
 
#Memanggil fungsi buat_pin
buat_pin(3)
#Output:
'''
    PIN: 000
    PIN: 001
    PIN: 002
    PIN: 010
    PIN: 011
    PIN: 012
    PIN: 020
    PIN: 021
    PIN: 022
    PIN: 100
    PIN: 101
    PIN: 102
    PIN: 110
    PIN: 111
    PIN: 112
    PIN: 120
    PIN: 121
    PIN: 122
    PIN: 200
    PIN: 201
    PIN: 202
    PIN: 210
    PIN: 211
    PIN: 212
    PIN: 220
    PIN: 221
    PIN: 222
'''

#=================================================================================================================
# Pertanyaan: Bagaimana cara mencegah angka yang sama muncul berulang?
'''
    Jawaban: Untuk mencegah pengulangan, sebelum menambahkan angka, cukup pastikan angka tersebut belum ada di hasil. Artinya, hanya tambahkan angka jika belum pernah dipakai. Dengan cara ini, setiap digit dalam satu PIN akan unik dan tidak ada angka yang berulang.
'''
#=================================================================================================================