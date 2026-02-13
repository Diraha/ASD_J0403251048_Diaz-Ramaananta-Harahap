class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_data = Node(data)

        if not self.head:
            self.head = new_data
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_data

    def display(self): 
        temp = self.head 
        while temp: 
            print(temp.data, end=" -> ") 
            temp = temp.next 
        print("null") 

    def	delete_node(self, key):	
        temp = self.head	
        if temp	and	temp.data == key:	
            self.head =	temp.next	
            temp = None	
            return	
        prev = None	
        while temp and temp.data !=	key:	
            prev = temp	
            temp = temp.next	
        if temp	is None:	
            return	
        prev.next =	temp.next	
        temp = None

ll = LinkedList() 
ll.append(1) 
ll.append(2) 
ll.append(3) 
ll.append(4) 
ll.display()
ll.delete_node(4)
ll.display()