# =========================================================
#Baytul Rafli
#J0403251027
#TPL B1
# ==========================================================
# ========================================================== 
# Latihan 2: Tracing Rekursi 
# ========================================================== 
 
 
def countdown(n): # Fungsi untuk menghitung mundur dari n ke 0
 
    if n == 0: # Base case: jika n mencapai 0, cetak "Selesai" dan kembali
        print("Selesai") # Output: Selesai
        return # Kembali ke pemanggil sebelumnya (keluar dari fungsi)
 
    print("Masuk:", n)
 
    countdown(n - 1) # Recursive case: panggil countdown dengan n-1 (hitung mundur)
 
    print("Keluar:", n) # Setelah countdown(n - 1) selesai, cetak "Keluar:" diikuti nilai n
 
 
countdown(3) # Memulai countdown dari 3

#Alur Eksekusi Program (Langkah demi Langkah)

#1) Pemanggilan Awal: countdown(3) dipanggil.
# Apakah n == 0? (3 == 0) -> Salah.
# Masuk ke recursive case: print("Masuk:", 3) -> Output: Masuk: 3
# countdown(2) dipanggil.

#2) Pemanggilan Rekursif ke-1: countdown(2) dipanggil.
# Apakah n == 0? (2 == 0) -> Salah.
# Masuk ke recursive case: print("Masuk:", 2) -> Output: Masuk: 2
# countdown(1) dipanggil.

#3) Pemanggilan Rekursif ke-2: countdown(1) dipanggil.
# Apakah n == 0? (1 == 0) -> Salah.
# Masuk ke recursive case: print("Masuk:", 1) -> Output: Masuk: 1
# countdown(0) dipanggil.

#4) Pemanggilan Rekursif ke-3 (Mencapai Base Case): countdown(0) dipanggil.
# Apakah n == 0? (0 == 0) -> BENAR.
# Masuk ke base case: print("Selesai") -> Output: Selesai
# Fungsi ini selesai dan kembali ke countdown(1).

#5) Kembali ke countdown(1): Setelah countdown(0) selesai, eksekusi dilanjutkan di countdown(1).
# print("Keluar:", 1) -> Output: Keluar: 1
# countdown(1) selesai dan kembali ke countdown(2).

#6) Kembali ke countdown(2): Setelah countdown(1) selesai, eksekusi dilanjutkan di countdown(2).
# print("Keluar:", 2) -> Output: Keluar: 2
# countdown(2) selesai dan kembali ke countdown(3).

#7) Kembali ke countdown(3): Setelah countdown(2) selesai, eksekusi dilanjutkan di countdown(3).
# print("Keluar:", 3) -> Output: Keluar: 3
# countdown(3) selesai dan program berakhir.