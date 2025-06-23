# Impor library numpy
import numpy as np

# Membuat array dengan numpy
nilai_siswa_1 = np.array([75, 65, 45, 80])
nilai_siswa_2 = np.array([[85, 55, 40], [50, 40, 99]])

# Cara akses elemen array
print(nilai_siswa_1[0])       # Output: 75
print(nilai_siswa_2[1][1])    # Output: 40

# Mengubah nilai elemen array
nilai_siswa_1[0] = 88
nilai_siswa_2[1][1] = 70

# Cek perubahannya dengan akses elemen array
print(nilai_siswa_1[0])       # Output: 88
print(nilai_siswa_2[1][1])    # Output: 70

# Cek ukuran dan dimensi array
print("Ukuran array nilai_siswa_1:", nilai_siswa_1.shape)   # Output: (4,)
print("Ukuran array nilai_siswa_2:", nilai_siswa_2.shape)   # Output: (2, 3)
print("Dimensi array nilai_siswa_2:", nilai_siswa_2.ndim)   # Output: 2
