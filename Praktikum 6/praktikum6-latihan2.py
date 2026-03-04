#----------------------------------------------#
#Baytul Rafli
#J0403251027
#TPL B1
#----------------------------------------------#
#Latihan 2 . Melengkapi Potongan Kode 
#----------------------------------------------#
def insertion_sort(data): 
    for i in range(1, len(data)): 
        key = data[i] 
        j = i - 1 
         
        # ASCENDING: selama elemen di kiri lebih besar dari key, geser ke kanan
        while j >= 0 and data[j] > key:  
            data[j + 1] = data[j]  
            j -= 1  
         
        # sisipkan key di posisi yang benar
        data[j + 1] = key  
     
    return data 

angka = [7, 8, 5, 2, 4, 6]
print("Hasil ascending:", insertion_sort(angka))

'''
#1. Lengkapi kondisi agar menjadi sorting ascending.
#   while j >= 0 and data[j] > key:
#   artinya selama elemen di kiri lebih besar dari key, geser ke kanan.
'''

'''
#2. Ubah agar menjadi descending.
#   while j >= 0 and data[j] < key:
#   artinya selama elemen di kiri lebih kecil dari key, geser ke kanan.
'''