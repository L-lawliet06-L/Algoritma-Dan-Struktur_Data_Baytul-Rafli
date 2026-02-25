#----------------------------------------------#
#Baytul Rafli
#J0403251027
#TPL B1
#----------------------------------------------#

# studi kasus = sistem antrian layanan pendidikan
# implentasi queue >>
# Enqueue : memindahkan pointer rear (nambah data baru dari belakang)
# dequeue : memindahkan pointer front (menghapus data dari depan)
# stack ==> front > c > b > a > none
# front > A > B > C > rear
#-----------------------------------------------#

#1) mendefinisikan node (unit dasar linked list)
class Node:
    def __init__(self, nim, nama):
        self.nim = nim  #menimpan nim mahasiswa
        self.nama = nama #menyimpan nama mahasiswa
        self.next = None #pointer ke node berikutnya 

#2) mendefinisikan class queue, terdiri fari front, rear,
class queueakademik:
    def __init__(self):
        self.front = None #pointer ke depan antrian    
        self.rear = None  #pointer ke belakang antrian

    def is__empty(self):
        #front = rear = None, maka antrian kosong
        return self.front is None #mengembalikan true jika antrian kosong
    
    def enqueue(self, nim, nama):
        new_node = Node(nim, nama) #membuat node baru dengan nim dan nama
        if self.is__empty(): #jika antrian kosong data baru = front = rear
            self.front = new_node #front dan rear menunjuk ke node baru
            self.rear = new_node
        else:
            self.rear.next = new_node #rear.next menunjuk ke node baru
            self.rear = new_node #rear sekarang menunjuk ke node baru


    #menghapus data paling depan (memberikan layanan akademik)
    def dequeue(self):      

        if self.is__empty(): #jika antrian kosong, tidak ada yang bisa dilayani
            print("Antrian kosong, tidak ada mahasiswa yang bisa dilayani.")
            return None

        #lihat bagian front, simpan di variabel data yang akan dihapus (dilayani)
        node_dilayani = self.front #menyimpan node yang akan dilayani (front)

        self.front = self.front.next #memindahkan front ke node berikutnya (menghapus node depan)

        #jika front menjadi none (data antrian terakhir yang dilayani), maka front = rear = None
        if self.front is None:
            self.rear = None

        return node_dilayani
    
    def tampilkan(self):

        
      
        print ("daftar antrian mahasiswa (front -> rear): ")
        current = self.front #mulai dari front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}") #menampilkan nim dan nama mahasiswa
            current = current.next #lanjut ke node berikutnya
            no += 1
    

#- program utama 

def main():

    #instantiasi queue
    q = queueakademik()

    while True:
        print("==== sistem antrian layanan akademik ====")
        print("1. Tambah mahasiswa ke antrian")
        print("2. Layani mahasiswa ")
        print("3. Tampilkan antrian")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == '1':
            nim = input("Masukkan NIM mahasiswa: ").strip()
            nama = input("Masukkan nama mahasiswa: ").strip()
            
            q.enqueue(nim, nama)
            print(f"Mahasiswa {nama} dengan NIM {nim} telah ditambahkan ke antrian.")
        
        elif pilihan == '2':
            mahasiswa_dilayani = q.dequeue()
            if mahasiswa_dilayani:
                print(f"Mahasiswa {mahasiswa_dilayani.nama} dengan NIM {mahasiswa_dilayani.nim} telah dilayani.")

        elif pilihan == '3':
            q.tampilkan()

        elif pilihan == '4':
            print("Terima kasih telah menggunakan sistem antrian layanan akademik.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu 1-4.")

# menjalankan program utama
if __name__ == "__main__":
    main()