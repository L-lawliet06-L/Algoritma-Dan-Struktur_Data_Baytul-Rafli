# =========================================================
#Baytul Rafli
#J0403251027
#TPL B1
# ==========================================================
# ========================================================== 
# Latihan 3: Kombinasi huruf
# ========================================================== 

def kombinasi(n, hasil=""): # Fungsi rekursif untuk menghasilkan semua kombinasi huruf 'A' dan 'B' dengan panjang n
 
    if len(hasil) == n: # Base case: jika panjang string hasil sudah n, cetak hasil dan kembali
        print(hasil) # Output: kombinasi huruf 'A' dan 'B' dengan panjang n
        return # Kembali ke pemanggil sebelumnya (keluar dari fungsi)
 
    kombinasi(n, hasil + "A") # Pilih 'A' dan lanjutkan eksplorasi dengan menambahkan 'A' ke hasil
    kombinasi(n, hasil + "B") # Pilih 'B' dan lanjutkan eksplorasi dengan menambahkan 'B' ke hasil
 
 
kombinasi(2) # Memulai kombinasi dengan panjang 2

# Alur Eksekusi Program (Langkah demi Langkah untuk kombinasi(2))

# 1) Pemanggilan Awal: kombinasi(2, "") dipanggil (hasil kosong).
# Panjang hasil (0) != 2, masuk ke recursive case.
# Panggil kombinasi(2, "A") dan kombinasi(2, "B").

# 2) Pemanggilan Rekursif ke-1: kombinasi(2, "A") dipanggil.
# Panjang hasil (1) != 2, masuk ke recursive case.
# Panggil kombinasi(2, "AA") dan kombinasi(2, "AB").

# 3) Pemanggilan Rekursif ke-2: kombinasi(2, "AA") dipanggil.
# Panjang hasil (2) == 2, masuk ke base case: cetak "AA" dan return.

# 4) Kembali ke Pemanggilan Rekursif ke-1: setelah "AA", panggil kombinasi(2, "AB").
# Panjang hasil (2) == 2, masuk ke base case: cetak "AB" dan return.

# 5) Kembali ke Pemanggilan Awal: setelah "A", panggil kombinasi(2, "B").
# Panjang hasil (1) != 2, masuk ke recursive case.
# Panggil kombinasi(2, "BA") dan kombinasi(2, "BB").

# 6) Pemanggilan Rekursif ke-3: kombinasi(2, "BA") dipanggil.
# Panjang hasil (2) == 2, masuk ke base case: cetak "BA" dan return.

# 7) Pemanggilan Rekursif ke-4: kombinasi(2, "BB") dipanggil.
# Panjang hasil (2) == 2, masuk ke base case: cetak "BB" dan return.

# 8) Fungsi selesai, semua kombinasi (AA, AB, BA, BB) telah dicetak.