import numpy as np
import matplotlib.pyplot as plt

# Definisikan fungsi gaya F(x)
def F(x):
    return 2 * x**2 + 4 * x + 2

# Rentang posisi dari 0 hingga 30 meter
x = np.linspace(0, 30, 100)  # 100 titik dari 0 hingga 30

# Menghitung gaya untuk setiap posisi x
F_values = F(x)

# Menampilkan hasil perhitungan
for position, force in zip(x, F_values):
    print(f"Posisi x = {position:.2f} m, Gaya F(x) = {force:.2f} N")

# Visualisasi grafik gaya F(x) terhadap posisi x
plt.plot(x, F_values, color='b', linestyle='-', label='Gaya F(x)')
plt.xlabel('Posisi x (m)')
plt.ylabel('Gaya F(x) (N)')
plt.title('Grafik Gaya F(x) terhadap Posisi x')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Garis horizontal di y=0
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Garis vertikal di x=0
plt.grid(True)
plt.legend()
plt.xlim(0, 30)  # Mengatur batas sumbu x
plt.ylim(min(F_values) - 10, max(F_values) + 10)  # Mengatur batas sumbu y
plt.show()