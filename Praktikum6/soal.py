#====================================================
# Nama: Diaz Ramaananta Harahap
# NIM: J0403251048
# Kelas: A/P1
#====================================================

#====================================================
# Latihan
#====================================================

def bubbleSort(data):
    for i in range(len(data)-1,0,-1):
        for j in range(i):
            if data[j] < data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp

data_ordered = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
data_unordered = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
bubbleSort(data_ordered)

max_value = data_ordered[:5]

print(f"Hasil Pengurutan Keseluruhan Nilai: {data_ordered}")
print(f"5 Kandidat Dengan Nilai Tertinggi: {max_value}")

for i, value in enumerate(max_value):
    if max_value[i] in data_unordered:
        print(f"Kandidat {i+1} Dengan Nilai {value} Adalah Kandidat Ke-{data_unordered.index(value) + 1}")