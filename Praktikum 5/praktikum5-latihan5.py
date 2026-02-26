# =========================================================
#Baytul Rafli
#J0403251027
#TPL B1
# ==========================================================
# ========================================================== 
# Studi Kasus: Generator PIN 
# ========================================================== 
 
def buat_pin(panjang, hasil=""): # Fungsi rekursif untuk membuat kombinasi PIN dengan panjang tertentu

    if len(hasil) == panjang: # Base case: jika panjang hasil sudah sesuai, cetak PIN dan kembali
        print("PIN:", hasil) # Output: PIN dengan kombinasi angka sesuai panjang yang ditentukan
        return # Kembali ke pemanggil sebelumnya (keluar dari fungsi)
 
    for angka in ["0", "1", "2"]: # Loop untuk memilih angka dari 0, 1, dan 2
        buat_pin(panjang, hasil + angka) # Pilih angka dan lanjutkan eksplorasi dengan menambahkan angka tersebut ke hasil
 
 
buat_pin(3) # Memulai pembuatan PIN dengan panjang 3

# Diskusi dan Penjelasan: Bagaimana cara mencegah angka yang sama muncul berulang?
# Saat ini, kode menghasilkan kombinasi dengan pengulangan (misalnya 000, 111, 222, dll.), 
# karena setiap posisi dapat memilih angka yang sama dari list ["0", "1", "2"].
# Untuk mencegah angka yang sama muncul berulang (yaitu setiap angka hanya muncul sekali dalam PIN), 
# kita perlu memodifikasi fungsi agar menggunakan kombinasi tanpa pengulangan.

# Cara melakukannya:
# 1. Ubah fungsi agar menerima list angka yang tersedia (available_digits) sebagai parameter tambahan.
# 2. Pada setiap pemanggilan rekursif, buat salinan list available_digits dan hapus angka yang dipilih dari salinan tersebut.
# 3. Hanya panggil rekursi jika masih ada angka tersedia dan panjang belum mencapai panjang.
# 4. Jika panjang hasil == panjang, cetak PIN.

# Contoh modifikasi kode (tidak dijalankan di sini, hanya untuk ilustrasi):
# def buat_pin_tanpa_ulang(panjang, hasil="", available_digits=None):
#     if available_digits is None:
#         available_digits = ["0", "1", "2"]
#     if len(hasil) == panjang:
#         print("PIN:", hasil)