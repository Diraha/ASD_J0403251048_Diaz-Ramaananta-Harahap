#====================================================
# Nama: Diaz Ramaananta Harahap
# NIM: J0403251048
# Kelas: A/P1
#====================================================

#====================================================
# Quick Sort : Descending
#====================================================

def partition(data, first, last):
    pivotValue = data[first]

    leftMark = first + 1
    rightMark = last

    done = False

    while not done:
        while leftMark <= rightMark and data[leftMark] >= pivotValue:
            leftMark = leftMark + 1

        while data[rightMark] <= pivotValue and rightMark >= leftMark:
            rightMark = rightMark - 1

        if rightMark < leftMark:
            done = True
        else:
            temp = data[leftMark]
            data[leftMark] = data[rightMark]
            data[rightMark] = temp
    
    temp = data[first]
    data[first] = data[rightMark]
    data[rightMark] = temp

    return rightMark

def quickSortHelper(data, first, last):
    if first < last:
        splitPoint = partition(data, first, last)
        quickSortHelper(data, first, splitPoint-1)
        quickSortHelper(data, splitPoint+1, last)

def quickSortDescending(data):
    quickSortHelper(data, 0, len(data)-1)

data = [59, 29, 98, 22, 82, 36, 49, 60, 25]
quickSortDescending(data)
print(data)