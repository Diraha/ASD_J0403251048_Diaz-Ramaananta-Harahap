#========================================================
# Nama : Diaz Ramaananta Harahap
# NIM : J0403251048
# Kelas : A/P1
#========================================================

#========================================================
# Implementasi Dasar : Queue
#========================================================
class Node:
    #Konstruktor adalah fungsi yang dijalankan secara otomatis ketika class node dipanggil/diinstantiasi
    def __init__(self, data):
        self.data = data #Menyimpan nilai Atau data dalam list
        self.next = None #Pointer ini menunjuk ke node berikutnya (Awal=None)

class Queue:
    #Buat konstruktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang

    def is_empty(self):
        return self.front is None

    #Membuat fungsi untuk menambah data baru pada bagian paling belakang
    def enqueue(self, data):
        nodeBaru = Node(data)

        #Jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        #Jika queue tidak kosong, maka letakkan data baru ke setelah rear, dan jalankan data baru sebagai rear
        self.rear.next = nodeBaru #Letakkan data baru pada setelah rear
        self.rear = nodeBaru #Jadikan data baru sebagai rear

    def dequeue(self):
        #Menghapus data dari depan/front
        data_terhapus = self.front.data #Lihat data paling depan

        #Geser front ke node berikutnya
        self.front = self.front.next

        #Jika setelah geser front menjadi None, maka queue kosong
        #Rear juga harus jadi None
        if self.front is None:
            self.rear = None

    def tampilkan(self):
        current = self.front
        print("Front ->", end=" ")
        while current is not None:
            print(current.data, end="-> ")
            current = current.next
        print("Rear")

#Instantiasi Class Queue
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
