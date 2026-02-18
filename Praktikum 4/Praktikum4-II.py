#NAMA  : Baytul Rafli
#NIM   : J040351027
#Kelas : TPL B1

#==========================================#
#Implementasi dasar : node dengan linked list
#==========================================#

#membuat class node (merupakan bagian dari linked list)
class Node:
    def __init__(self,data):  #konstruktor untuk membuat node
        self.data = data #menyimpan data
        self.next = None #poimter untuk node selanjutnya (awal=None)

# 1} membuat node satu per satu
nodeA = Node("A") #membuat node dengan data "A"
nodeB = Node("B") #membuat node dengan data "B"
nodeC = Node("C") #membuat node dengan data "C"

# 2} menghubungkan node-node tersebut :A->B->C->None
nodeA.next = nodeB #nodeA menunjuk ke nodeB
nodeB.next = nodeC #nodeB menunjuk ke nodeC

# 3} node terakhir menunjuk ke None (head)
head = nodeA #head menunjuk ke nodeA (awal dari linked list)

# 4} traversal : menelusuri dari head sampe none
current = head #mulai dari head
while current is not None: #selama current tidak menunjuk ke None
    print(current.data) #cetak data pada node saat ini
    current = current.next #pindah ke node berikutnya

#========================================================#
#Implementasi dasar : linked list + insert awal 
#========================================================#

class linkedList: #class implementasi stack
    def __init__(self): #konstruktor untuk membuat linked list
        self.head = None #head awalnya menunjuk ke None (kosong)
    def insert_awal(self,data): #konstruktor untuk membuat linked list
        #1) buat node baru dengan data yang diberikan
        nodebaru = Node(data) 
        
        #2) node baru menunjuk ke head saat ini
        nodebaru.next = self.head

        #3) head sekarang menunjuk ke node baru
        self.head = nodebaru 

    def hapus_awal(self): #implentasi untuk menghapus node pertama
        data_terhapus = self.head.data #peek dalam stack
        #menggerakkan head ke node berikutnya (node kedua)
        self.head = self.head.next 
        print("node yang dihapus:", data_terhapus) #cetak data yang dihapus

    def tampilkan(self): #implentasi transversal untuk menampilkan isi linked list
        current = self.head #mulai dari head
        while current is not None: #selama current tidak menunjuk ke None
            print(current.data) #cetak data pada node saat ini
            current = current.next #pindah ke node berikutnya

print("======list baru======")
ll = linkedList() #instansiasi objek ke class linked list
ll.insert_awal("X") 
ll.insert_awal("Y") 
ll.insert_awal("Z") 
ll.tampilkan()
ll.hapus_awal() 
ll.tampilkan()

