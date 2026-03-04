#----------------------------------------------#
#Baytul Rafli
#J0403251027
#TPL B1
#----------------------------------------------#
#Latihan 1 . Memahami Kode Program (Insertion Sort)
#----------------------------------------------#
def insertion_sort(data):  
    for i in range(1, len(data)):  
        key = data[i]  
        j = i - 1  
         
        while j >= 0 and data[j] > key:  
            data[j + 1] = data[j]  
            j -= 1  
         
        data[j + 1] = key  
     
    return data  

angka = [7, 8, 5, 2, 4, 6]
print("Hasil dari insertion sort:", insertion_sort(angka))


'''
#1. Mengapa perulangan dimulai dari indeks 1?
# Karena elemen pertama (indeks 0) dianggap sudah terurut, 
# sehingga proses penyisipan dimulai dari elemen kedua.
'''

'''
#2. Apa fungsi variabel key?
# Variabel key menyimpan nilai elemen yang sedang diproses 
# agar bisa digeserkan elemen lain tanpa kehilangan nilai aslinya.
'''

'''
#3. Mengapa digunakan while, bukan for?
# Karena jumlah pergeseran tidak pasti. While lebih fleksibel 
# untuk kondisi (selama elemen di kiri lebih besar dari key, terus geser).
'''

'''
#4. Operasi apa yang terjadi di dalam while?
# Elemen yang lebih besar dari key digeser ke kanan (data[j+1] = data[j]), 
# lalu indeks j dikurangi (j -= 1). Setelah selesai, key ditempatkan di posisi yang benar.
'''