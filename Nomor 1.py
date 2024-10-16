# Meminta input dari pengguna untuk persentase nilai siswa dan mengonversinya ke float
persentase = float(input("Masukkan persentase nilai siswa: "))

# Menggunakan kondisi untuk mengevaluasi kinerja siswa berdasarkan persentase
if persentase >= 90:  # Memeriksa apakah persentase >= 90
    kinerja = "Excellent performance"  # Jika ya, kinerja adalah "Excellent performance"
elif persentase >= 80:  # Memeriksa apakah persentase >= 80
    kinerja = "Very good performance"  # Jika ya, kinerja adalah "Very good performance"
elif persentase >= 70:  # Memeriksa apakah persentase >= 70
    kinerja = "Good performance"  # Jika ya, kinerja adalah "Good performance"
elif persentase >= 60:  # Memeriksa apakah persentase >= 60
    kinerja = "Average performance"  # Jika ya, kinerja adalah "Average performance"
else:  # Jika persentase kurang dari 60
    kinerja = "Below average performance"  # Kinerja adalah "Below average performance"

# Mencetak hasil evaluasi kinerja siswa
print("Evaluate Student Performance:", kinerja)