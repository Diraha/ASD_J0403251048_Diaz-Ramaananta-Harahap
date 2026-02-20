#========================================================
# Nama : Diaz Ramaananta Harahap
# NIM : J0403251048
# Kelas : A/P1
#========================================================

#========================================================
# Implementasi Dasar : Stack
#========================================================
#Konstruktor adalah fungsi yang dijalankan secara otomatis ketika class node dipanggil/diinstantiasi
class Node:
    def __init__(self, data):
        self.data = data #Menyimpan nilai Atau data dalam list
        self.next = None #Pointer ini menunjuk ke node berikutnya (Awal=None)

class Stack:
    def __init__(self):
        self.top = None #Top Menunjuk ke Node Paling Atas (Awalnya Kosong)

    def is_empty(self): #Stack Kosong Jika Top None
        return self.top is None

    def push(self, data): #Memasukkan Data Baru
        #Membuat Node Baru
        nodeBaru = Node(data)

        #Node Harus Menunjuk ke Top Yang Lama (Head Lama)
        nodeBaru.next = self.top

        #Geser Top Pindah ke Node Baru
        self.top = nodeBaru
    
    def tampilkan(self):
        current = self.top
        print("Top ->", end=" ")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")

    def peek(self):
        # Melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data

    def pop(self): #Mengambil/menghapus node paling atas (head/top)
        if self.is_empty():
            print("Stack Kosong, Tidak Bisa Pop!")
            return None

        data_terhapus = self.top.data
        self.top = self.top.next
        return data_terhapus

# Instantiasi Class Stack
s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peak (Lihat Top): ", s.peek())
s.pop()
s.tampilkan()