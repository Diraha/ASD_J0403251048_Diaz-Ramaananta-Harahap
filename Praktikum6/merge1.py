#====================================================
# Nama: Diaz Ramaananta Harahap
# NIM: J0403251048
# Kelas: A/P1
#====================================================

#====================================================
# Merge Sort : Ascending
#====================================================

def mergeSortAscending(data):
    print(f"Splitting {data}")
    if len(data) > 1:
        mid = len(data) // 2
        leftHalf = data[:mid]
        rightHalf = data[mid:]

        mergeSortAscending(leftHalf)
        mergeSortAscending(rightHalf)

        i = 0
        j = 0
        k = 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] <= rightHalf[j]:
                data[k] = leftHalf[i]
                i = i + 1
            else:
                data[k] = rightHalf[j]
                j = j + 1
            k = k + 1

        while i < len(leftHalf):
            data[k] = leftHalf[i]
            i = i + 1
            k = k + 1

        while j < len(rightHalf):
            data[k] = rightHalf[j]
            j = j + 1
            k = k + 1
    
    print(f"Merging {data}")

data = [49, 19, 88, 12, 72, 26, 39, 50, 15]
mergeSortAscending(data)
print(data)