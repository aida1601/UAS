import numpy as np
import matplotlib.pyplot as plt

# Parameter
v0 = 50  # kecepatan awal dalam m/s
g = 9.81  # percepatan gravitasi dalam m/s^2

# Waktu untuk mencapai tinggi maksimum
t_maks = v0 / g

# Waktu total perjalanan
t_total = 2 * t_maks

# Waktu dari 0 hingga t_total
t = np.linspace(0, t_total, num=100)  # 100 titik waktu

# Menghitung tinggi h(t) untuk seluruh perjalanan
h = v0 * t - 0.5 * g * t**2

# Menampilkan hasil perhitungan
for time, height in zip(t, h):
    print(f"Waktu t = {time:.2f} detik, Tinggi h(t) = {height:.2f} m")

# Visualisasi grafik tinggi terhadap waktu
plt.plot(t, h, color='r', linestyle='-', label='Tinggi h(t)')
plt.xlabel('Waktu (detik)')
plt.ylabel('Tinggi h(t) (meter)')
plt.title('Gerak Benda Vertikal ke Atas dan Kembali (NPM Genap)')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Garis horizontal di y=0
plt.grid(True)
plt.legend()
plt.xlim(0, t_total)  # Mengatur batas sumbu x
plt.ylim(min(h) - 10, max(h) + 10)  # Mengatur batas sumbu y
plt.show()