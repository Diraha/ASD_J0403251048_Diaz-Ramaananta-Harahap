#====================================================
# Nama: Diaz Ramaananta Harahap
# NIM: J0403251048
# Kelas: A/P1
#====================================================

#====================================================
# Selection Sort : Ascending
#====================================================

def selectionSortAscending(data):
    for i in range(len(data)-1,0,-1):
        indexMax = 0
        for j in range(1, i+1):
            if data[j] > data[indexMax]:
                indexMax = j
        
        temp = data[j]
        data[j] = data[indexMax]
        data[indexMax] = temp

data = [48, 18, 87, 11, 71, 25, 38, 49, 14]
selectionSortAscending(data)
print(data)