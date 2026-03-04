#----------------------------------------------#
#Baytul Rafli
#J0403251027
#TPL B1
#----------------------------------------------#
#Latihan 4 . Memahami Kode Program (Merge Sort) 
#----------------------------------------------#

def merge_sort(data): 
    if len(data) <= 1: 
        return data   # base case: jika panjang list <= 1, langsung kembalikan (sudah terurut)
     
    mid = len(data) // 2 
    left = data[:mid] 
    right = data[mid:] 
     
    left_sorted = merge_sort(left)   # fungsi memanggil dirinya sendiri untuk membagi bagian kiri
    right_sorted = merge_sort(right) # fungsi memanggil dirinya sendiri untuk membagi bagian kanan
     
    return merge(left_sorted, right_sorted)  # gabungkan hasil kiri dan kanan dengan merge()

'''
#==================================================================================================
#soal yang di atas, tetapi di soal nya merge nya tidak ter defined jadi code yg saya bikin di bawah
#==================================================================================================
'''

def merge_sort(data): 
    if len(data) <= 1: 
        return data   # base case: jika panjang list <= 1, langsung kembalikan (sudah terurut)
     
    mid = len(data) // 2 
    left = data[:mid] 
    right = data[mid:] 
     
    left_sorted = merge_sort(left)   # fungsi memanggil dirinya sendiri untuk membagi bagian kiri
    right_sorted = merge_sort(right) # fungsi memanggil dirinya sendiri untuk membagi bagian kanan
     
    return merge(left_sorted, right_sorted)  # gabungkan hasil kiri dan kanan dengan merge()


def merge(left, right):
    result = []
    i = 0
    j = 0

    # bandingkan elemen kiri dan kanan, masukkan yang lebih kecil dulu
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # tambahkan sisa elemen jika ada
    result.extend(left[i:])
    result.extend(right[j:])
    return result


angka = [13, 7, 28, 5, 19, 36, 4]
print("Hasil Sorting:", merge_sort(angka))

'''
# Soal:
#1. Apa yang dimaksud dengan base case?
#   Base case adalah kondisi berhenti pada rekursif, yaitu ketika panjang list <= 1.
#   Pada kondisi ini, list dianggap sudah terurut sehingga langsung dikembalikan.
'''

'''
#2. Mengapa fungsi memanggil dirinya sendiri?
#   Karena merge sort menggunakan konsep rekursif (divide and conquer).
#   List dibagi terus menjadi bagian kecil sampai mencapai base case, lalu digabung kembali.
'''

'''
#3. Apa tujuan fungsi merge()?
#   Fungsi merge() bertugas menggabungkan dua list yang sudah terurut (left dan right)
#   menjadi satu list besar yang terurut secara ascending.
'''