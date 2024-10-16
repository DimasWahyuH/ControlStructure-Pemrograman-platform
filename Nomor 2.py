# Meminta input dari pengguna untuk bilangan pertama dan mengonversinya ke integer
a = int(input("Masukkan bilangan pertama: "))

# Meminta input dari pengguna untuk bilangan kedua dan mengonversinya ke integer
b = int(input("Masukkan bilangan kedua: "))

# Meminta input dari pengguna untuk bilangan ketiga dan mengonversinya ke integer
c = int(input("Masukkan bilangan ketiga: "))

# Menggunakan kondisi untuk menentukan bilangan terbesar
if a >= b and a >= c:  # Memeriksa apakah 'a' lebih besar atau sama dengan 'b' dan 'c'
    terbesar = a  # Jika ya, maka 'a' adalah bilangan terbesar
elif b >= a and b >= c:  # Memeriksa apakah 'b' lebih besar atau sama dengan 'a' dan 'c'
    terbesar = b  # Jika ya, maka 'b' adalah bilangan terbesar
else:  # Jika kedua kondisi sebelumnya tidak terpenuhi
    terbesar = c  # Maka 'c' adalah bilangan terbesar

# Mencetak bilangan terbesar yang ditemukan
print("Bilangan terbesar adalah:", terbesar)