#NAMA  : Baytul Rafli
#NIM   : J040351027
#Kelas : TPL B1

#==========================================#
#Implementasi dasar : queue berbasis linked list
#==========================================#

#membuat class node (merupakan bagian dari linked list)
class Node:
    def __init__(self,data):  #konstruktor untuk membuat node
        self.data = data #menyimpan data
        self.next = None #poimter untuk node selanjutnya (awal=None)

#queue dengan 2 pointer : head dan tail
class QueueLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):  # fungsi untuk mengecek apakah queue kosong
        return self.head is None

    def enqueue(self, data):
        nodebaru = Node(data)
        if self.is_empty():  # cek apakah queue kosong
            self.head = nodebaru
            self.tail = nodebaru
            return
        self.tail.next = nodebaru
        self.tail = nodebaru

    def dequeue(self):
        #1) pilih data yang paling depan
        data_terhapus = self.head.data
        #2) geserkann head ke node berikutnya
        self.head = self.head.next
        #3) jika head menjadi None, berarti queue kosong, maka tail juga harus diatur ke None
        if self.head is None:
            self.tail = None

        return data_terhapus


    def tampilkan(self):
        current = self.head
        print("head -> ", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("none - tail di node terakhir")

#instnsiasi objek class QueueLL
q = QueueLL() #membuat objek queue dari class QueueLL
q.enqueue("A") #menambahkan data 10 ke queue
q.enqueue("B") #menambahkan data 20 ke queue
q.enqueue("C") #menambahkan data 30 ke queue
q.tampilkan() #menampilkan isi queue

q.dequeue() #menghapus data paling depan (A)
q.tampilkan() #menampilkan isi queue setelah dequeue