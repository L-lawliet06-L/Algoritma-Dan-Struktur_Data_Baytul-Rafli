# =========================================================
#Baytul Rafli
#J0403251027
#TPL B1
# ==========================================================
# ========================================================== 
# Latihan 3: Mencari Nilai Maksimum 
# ========================================================== 

def cari_maks(data, index=0): # Fungsi rekursif untuk mencari nilai maksimum dalam list
 
    # Base case 
    if index == len(data) - 1: # Jika sudah mencapai elemen terakhir, kembalikan nilai tersebut
        return data[index] # memanggil elemen terakhir sebagai nilai maksimum sementara
 
    # Recursive case 
    maks_sisa = cari_maks(data, index + 1) # Panggil fungsi untuk mencari maksimum di sisa list (dari index + 1 hingga akhir)
 
    if data[index] > maks_sisa:    # Bandingkan elemen saat ini dengan maksimum yang ditemukan di sisa list
        return data[index] # Jika elemen saat ini lebih besar, kembalikan elemen tersebut sebagai maksimum
    else: 
        return maks_sisa # Jika maksimum di sisa list lebih besar atau sama, kembalikan nilai tersebut sebagai maksimum
 
 
angka = [3, 7, 2, 9, 5] # List angka yang akan dicari nilai maksimumnya
print("Nilai maksimum:", cari_maks(angka)) 

#Alur Eksekusi Program (Langkah demi Langkah)

#1) Pemanggilan Awal: cari_maks([3, 7, 2, 9, 5]) dipanggil dengan index default 0.
# Apakah index == len(data) - 1? (0 == 4) -> Salah.
# Masuk ke recursive case: cari_maks([3, 7, 2, 9, 5], index=1) dipanggil.

#2) Pemanggilan Rekursif ke-1: cari_maks([3, 7, 2, 9, 5], index=1) dipanggil.
# Apakah index == len(data) - 1? (1 == 4) -> Salah.
# Masuk ke recursive case: cari_maks([3, 7, 2, 9, 5], index=2) dipanggil.

#3) Pemanggilan Rekursif ke-2: cari_maks([3, 7, 2, 9, 5], index=2) dipanggil.
# Apakah index == len(data) - 1? (2 == 4) -> Salah.
# Masuk ke recursive case: cari_maks([3, 7, 2, 9, 5], index=3) dipanggil.

#4) Pemanggilan Rekursif ke-3: cari_maks([3, 7, 2, 9, 5], index=3) dipanggil.
# Apakah index == len(data) - 1? (3 == 4) -> Salah.
# Masuk ke recursive case: cari_maks([3, 7, 2, 9, 5], index=4) dipanggil.

#5) Pemanggilan Rekursif ke-4: cari_maks([3, 7, 2, 9, 5], index=4) dipanggil.
# Apakah index == len(data) - 1? (4 == 4) -> Benar.
# Masuk ke base case: return data[4] yaitu 5.

#6) Kembali ke Pemanggilan Rekursif ke-3 (index=3): maks_sisa = 5.
# Bandingkan data[3] = 9 > 5? Ya, return 9.

#7) Kembali ke Pemanggilan Rekursif ke-2 (index=2): maks_sisa = 9.
# Bandingkan data[2] = 2 > 9? Tidak, return 9.

#8) Kembali ke Pemanggilan Rekursif ke-1 (index=1): maks_sisa = 9.
# Bandingkan data[1] = 7 > 9? Tidak, return 9.

#9) Kembali ke Pemanggilan Awal (index=0): maks_sisa = 9.
# Bandingkan data[0] = 3 > 9? Tidak, return 9.

#10) Fungsi selesai, nilai maksimum adalah 9, dicetak ke layar.