#====================================================
# Nama: Diaz Ramaananta Harahap
# NIM: J0403251048
# Kelas: A/P1
#====================================================

#====================================================
# Shell Sort : Ascending
#====================================================

def gapInsertionSort(data, start, gap):
    for i in range(start+gap, len(data), gap):
        currentValue = data[i]
        position = i

        while position >= gap and data[position - gap] > currentValue:
            data[position] = data[position - gap]
            position = position - gap

        data[position] = currentValue

def shellSortAscending(data):
    sublistcount = len(data) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(data, startposition, sublistcount)

        print(f"After increments of size {sublistcount} The list is {data}")

        sublistcount = sublistcount // 2

data = [47, 17, 86, 10, 70, 24, 37, 48, 13]
shellSortAscending(data)
print(data)