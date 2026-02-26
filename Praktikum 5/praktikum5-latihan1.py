#----------------------------------------------#
#Baytul Rafli
#J0403251027
#TPL B1
#----------------------------------------------#
# ========================================================== 
# Latihan 1: Rekursi Pangkat 
# ========================================================== 
def pangkat(a, n):  # a^n = a * a^(n-1)
# Base case 
 if n == 0: 
      return 1 
 
# Recursive case 
 return a * pangkat(a, n - 1) 

print(pangkat(2, 4))  # Output: 16 

#Alur Eksekusi Program (Langkah demi Langkah)

#1.) Pemanggilan Awal: pangkat(2, 4) dipanggil.
# Apakah n == 0? (4 == 0) -> Salah.
# Masuk ke recursive case: return 2 * pangkat(2, 3)
# Fungsi ini ditunda (paused) karena harus menunggu hasil dari pangkat(2, 3).

#2) Pemanggilan Rekursif ke-1: pangkat(2, 3) dipanggil.
# Apakah n == 0? (3 == 0) -> Salah.
# Masuk ke recursive case: return 2 * pangkat(2, 2)
# Fungsi ini ditunda.

#3) Pemanggilan Rekursif ke-2: pangkat(2, 2) dipanggil.
# Apakah n == 0? (2 == 0) -> Salah.
# Masuk ke recursive case: return 2 * pangkat(2, 1)
# Fungsi ini ditunda.

#4) Pemanggilan Rekursif ke-3: pangkat(2, 1) dipanggil.
# Apakah n == 0? (1 == 0) -> Salah.
# Masuk ke recursive case: return 2 * pangkat(2, 0)
# Fungsi ini ditunda.

#5) Pemanggilan Rekursif ke-4 (Mencapai Base Case): pangkat(2, 0) dipanggil.
# Apakah n == 0? (0 == 0) -> BENAR.
# Masuk ke base case: return 1
# Fungsi ini selesai dan mengembalikan nilai 1.