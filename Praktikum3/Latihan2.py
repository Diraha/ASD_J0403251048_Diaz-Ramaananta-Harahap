class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head 
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("List is empty")
            return

        print("Circular Linked List Traversal:")
        temp = self.head

        print(temp.data, end=" -> ")
        temp = temp.next

        while temp != self.head:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("... (back to head)")

    def search(self, key): 
        temp = self.head 
        while temp: 
            if temp.data == key:
                print(f"Elemen	{key} ditemukan	dalam	Circular	Linked	List.")
                return True 
            temp = temp.next 

            if temp == self.head:
                break

        print(f"Elemen {key} tidak ditemukan dalam	Circular Linked	List.")
        return False

cll = CircularSinglyLinkedList()
cll.append(3)
cll.append(7)
cll.append(12)
cll.append(19)
cll.append(25)

cll.display()

cll.search(30)
