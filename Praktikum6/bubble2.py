#====================================================
# Nama: Diaz Ramaananta Harahap
# NIM: J0403251048
# Kelas: A/P1
#====================================================

#====================================================
# Bubble Sort : Descending
#====================================================

def bubbleSortDescending(data):
    for i in range(len(data)-1,0,-1):
        for j in range(i):
            if data[j] < data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp

data = [51, 23, 90, 14, 74, 28, 41, 52, 17]
bubbleSortDescending(data)
print(data)