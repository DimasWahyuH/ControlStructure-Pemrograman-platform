# Meminta input dari pengguna
n = int(input("Masukkan angka maksimum: "))

# Inisialisasi dua angka pertama deret Fibonacci
a, b = 0, 1

# Cetak angka Fibonacci selama tidak melebihi n
print("Deret Fibonacci hingga", n, "adalah:")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b