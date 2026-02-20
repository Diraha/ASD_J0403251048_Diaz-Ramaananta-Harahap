#========================================================
# Nama : Diaz Ramaananta Harahap
# NIM : J0403251048
# Kelas : A/P1
#========================================================

#========================================================
# Implementasi Dasar : Linked List
#========================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

current = head

while current is not None:
    print(current.data)
    current = current.next