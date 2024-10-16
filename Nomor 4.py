# Meminta input dari pengguna untuk menentukan batas maksimum n
n = int(input("Masukkan angka maksimum: "))  

# Menampilkan pesan untuk memulai pencetakan bilangan ganjil
print("Bilangan ganjil hingga", n, "adalah:")

# Menggunakan loop untuk mencetak bilangan ganjil
for i in range(1, n + 1):  # Mengiterasi dari 1 hingga n 
    if i % 2 != 0:  # Memeriksa apakah i adalah bilangan ganjil
        print(i, end="[]")  # Mencetak bilangan ganjil dengan [] di antara