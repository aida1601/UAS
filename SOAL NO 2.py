import numpy as np
import matplotlib.pyplot as plt

# Parameter gerak harmonis sederhana
T = 10  # periode dalam detik
A = 5 / 100  # amplitudo dalam meter (5 cm = 0.05 m)

# Menghitung frekuensi sudut
omega = 2 * np.pi / T  # rad/s

# Waktu dari 0 hingga 50 detik
t = np.arange(0, 51, 0.1)  # Menggunakan langkah 0.1 detik

# Menghitung posisi x(t)
x = A * np.cos(omega * t)  # Persamaan posisi

# Menampilkan hasil perhitungan
for time, position in zip(t, x):
    print(f"Waktu t = {time:.1f} detik, Posisi x(t) = {position:.4f} m")

# Visualisasi grafik posisi terhadap waktu
plt.plot(t, x, color='b', linestyle='-', label='Posisi x(t)')
plt.xlabel('Waktu (detik)')
plt.ylabel('Posisi x(t) (meter)')
plt.title('Gerak Harmonis Sederhana')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Garis horizontal di y=0
plt.grid(True)
plt.legend()
plt.xlim(0, 50)  # Mengatur batas sumbu x
plt.ylim(-0.06, 0.06)  # Mengatur batas sumbu y
plt.show()