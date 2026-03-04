#----------------------------------------------#
#Baytul Rafli
#J0403251027
#TPL B1
#----------------------------------------------#
#Latihan 5 . Melengkapi Fungsi Merge 
#----------------------------------------------#
def merge(left, right): 
    result = [] 
    i = 0 
    j = 0 
     
    while i < len(left) and j < len(right): 
        # ASCENDING: pilih elemen terkecil dulu
        if left[i] <= right[j]:  
            result.append(left[i]) 
            i += 1 
        else: 
            result.append(right[j]) 
            j += 1 
     
    result.extend(left[i:]) 
    result.extend(right[j:]) 
     
    return result 

'''
# Soal:
#1. Lengkapi kondisi agar menjadi ascending.
#   Jawab: if left[i] <= right[j]:
#   artinya jika elemen kiri lebih kecil atau sama dengan elemen kanan,
#   maka elemen kiri dimasukkan dulu ke result.
'''


'''
#2. Jelaskan fungsi result.extend().
#   Jawab: result.extend() digunakan untuk menambahkan sisa elemen dari list lain ke result.
#   Misalnya result.extend(left[i:]) akan menambahkan semua elemen left mulai dari indeks i hingga akhir.
#   Jadi extend menambahkan banyak elemen sekaligus, bukan hanya satu seperti append().
'''