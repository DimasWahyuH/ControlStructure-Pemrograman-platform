# Meminta input dari pengguna untuk menentukan nilai n
n = int(input("Enter a value for n: "))  

# Menggunakan loop untuk mencetak desain sesuai dengan nilai n
for i in range(1, n + 1):  # Mengiterasi dari 1 hingga n (inklusif)
    print((str(i) + " ") * i)  # Mencetak angka i, diulang sebanyak i kali