#----------------------------------------------#
#Baytul Rafli
#J0403251027
#TPL B1
#----------------------------------------------#
#Latihan 3 . Tracing Insertion Sort 
#----------------------------------------------#

'''
#Buat program dengan menggunakan algoritma insertion sort 
#Tracing dengan  data = [5, 2, 4, 6, 1, 3]
'''

def insertion_sort(data):
    print("Data awal:", data)
    print("="*50)

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        print(f"Iterasi i = {i}, key = {key}")

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key
        print("Setelah penyisipan:", data)
        print("="*50)

    return data


angka = [5, 2, 4, 6, 1, 3]
print("Hasil akhir:", insertion_sort(angka))

'''
# Soal:
#1.Tuliskan isi list setelah iterasi i = 1.
#  Jawab: [2, 5, 4, 6, 1, 3]
'''

'''
#2.Tuliskan isi list setelah iterasi i = 3.
#  Jawab: [2, 4, 5, 6, 1, 3]
'''

'''
#3.Berapa kali pergeseran terjadi pada iterasi i = 4?
#  Jawab: 4 kali pergeseran (6 → 6, 5 → 6, 4 → 5, 2 → 4), 
#  sehingga list menjadi [1, 2, 4, 5, 6, 3].
'''