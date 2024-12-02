import numpy as np
import matplotlib.pyplot as plt

# Konstanta pegas
k = 60  # N/m

# Rentang regangan pegas dari 0 m hingga 0.5 m dengan langkah 0.02 m
x = np.arange(0, 0.51, 0.02)  # Menambahkan 0.51 untuk menyertakan 0.5

# Menghitung gaya F(x) menggunakan Hukum Hooke
F = -k * x  # Gaya negatif sesuai dengan Hukum Hooke

# Menampilkan hasil perhitungan
for posisi, gaya in zip(x, F):
    print(f"Posisi x = {posisi:.2f} m, Gaya F(x) = {gaya:.2f} N")

# b) Visualisasi grafik gaya F(x) terhadap posisi x
plt.plot(x, F, color='b', linestyle='-', marker='o', label='Gaya F(x)')
plt.xlabel('Posisi x (m)')
plt.ylabel('Gaya F(x) (N)')
plt.title('Grafik Gaya F(x) terhadap Posisi x')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Garis horizontal di y=0
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Garis vertikal di x=0
plt.grid(True)
plt.legend()
plt.xlim(0, 0.5)  # Mengatur batas sumbu x
plt.ylim(-35, 0)  # Mengatur batas sumbu y
plt.show()