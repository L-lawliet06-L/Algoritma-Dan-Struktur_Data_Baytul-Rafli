#----------------------------------------------#
#Baytul Rafli
#J0403251027
#TPL B1
#----------------------------------------------#

# studi kasus = sistem antrian layanan servis bengkel motor
# implentasi queue >>
# Enqueue : memindahkan pointer rear (nambah data baru dari belakang)
# dequeue : memindahkan pointer front (menghapus data dari depan)
# stack ==> front > c > b > a > none
# front > A > B > C > rear
#-----------------------------------------------#

#1) mendefinisikan node (unit dasar linked list)
class Node:
    def __init__(self, motor, nama):
        self.motor = motor  #menyimpan jenis motor pelanggan
        self.nama = nama #menyimpan nama pelanggan
        self.next = None #pointer ke node berikutnya 

#2) mendefinisikan class queue, terdiri fari front, rear,
class queuebengkel:
    def __init__(self):
        self.front = None #pointer ke depan antrian    
        self.rear = None  #pointer ke belakang antrian

    def is__empty(self):
        #front = rear = None, maka antrian kosong
        return self.front is None #mengembalikan true jika antrian kosong
    
    def enqueue(self, motor, nama):
        new_node = Node(motor, nama) #membuat node baru dengan motor dan nama
        if self.is__empty(): #jika antrian kosong data baru = front = rear
            self.front = new_node #front dan rear menunjuk ke node baru
            self.rear = new_node
        else:
            self.rear.next = new_node #rear.next menunjuk ke node baru
            self.rear = new_node #rear sekarang menunjuk ke node baru


    #menghapus data paling depan (memberikan layanan akademik)
    def dequeue(self):      

        if self.is__empty(): #jika antrian kosong, tidak ada yang bisa dilayani
            print("Antrian kosong, tidak ada pelanggan yang bisa dilayani.")
            return None

        #lihat bagian front, simpan di variabel data yang akan dihapus (dilayani)
        node_dilayani = self.front #menyimpan node yang akan dilayani (front)

        self.front = self.front.next #memindahkan front ke node berikutnya (menghapus node depan)

        #jika front menjadi none (data antrian terakhir yang dilayani), maka front = rear = None
        if self.front is None:
            self.rear = None

        return node_dilayani
    
    def tampilkan(self):

        
      
        print ("daftar antrian servis (front -> rear): ")
        current = self.front #mulai dari front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}") #menampilkan nim dan nama mahasiswa
            current = current.next #lanjut ke node berikutnya
            no += 1
    

#- program utama 

def main():

    #instantiasi queue
    q = queuebengkel()

    while True: #loop utama untuk menampilkan menu dan menangani pilihan pengguna
        print("==== sistem antrian servis bengkel Baytul ====")
        print("1. Tambah pelanggan ke antrian")
        print("2. Layani pelanggan ")
        print("3. Tampilkan antrian")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ").strip() #mengambil input pilihan menu dari pengguna

        if pilihan == '1':
            motor = input("Masukkan jenis motor pelanggan: ").strip() #mengambil input jenis motor pelanggan
            nama = input("Masukkan nama pelanggan: ").strip() #mengambil input nama pelanggan
            
            q.enqueue(motor, nama) #menambahkan pelanggan ke antrian dengan motor dan nama yang diinputkan
            print(f"Pelanggan {nama} dengan motor {motor} telah ditambahkan ke antrian.") #memberikan konfirmasi bahwa pelanggan telah ditambahkan ke antrian
        
        elif pilihan == '2':
            pelanggan_dilayani = q.dequeue() #menghapus pelanggan paling depan dari antrian (memberikan layanan kepada pelanggan tersebut)
            if pelanggan_dilayani: #jika ada pelanggan yang dilayani (antrian tidak kosong), tampilkan informasi pelanggan yang telah dilayani
                print(f"Mas/Mba {pelanggan_dilayani.nama} dengan motor {pelanggan_dilayani.motor} telah diservis bosku.") #memberikan konfirmasi bahwa pelanggan telah dilayani

        elif pilihan == '3':
            q.tampilkan() #menampilkan daftar antrian pelanggan yang sedang menunggu layanan (dari front ke rear)

        elif pilihan == '4':
            print("Terima kasih telah menggunakan sistem antrian servis bengkel Baytul.") #memberikan pesan perpisahan sebelum keluar dari program
            break #keluar dari loop utama dan mengakhiri program

        else:
            print("Pilihan tidak valid. Silakan pilih menu 1-4.") #memberikan pesan error jika pengguna memasukkan pilihan yang tidak valid (bukan 1-4)

# menjalankan program utama
if __name__ == "__main__":
    main()

    #thats all folks :)