#====================================================
# Nama: Diaz Ramaananta Harahap
# NIM: J0403251048
# Kelas: A/P1
#====================================================

#====================================================
# Insertion Sort : Descending
#====================================================

def insertionSortDescending(data):
    for i in range(1, len(data)):
        currentValue = data[i]
        position = i

        while position > 0 and data[position - 1] < currentValue:
            data[position] = data[position - 1]
            position = position - 1
            data[position] = currentValue

data = [56, 28, 95, 19, 79, 33, 46, 57, 22]
insertionSortDescending(data)
print(data)