import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

plt.plot(x, x, label="Linear: f(x) = x")
plt.plot(x, x**2, label="Kuadrat: f(x) = x^2")
plt.plot(x, x**3, label="Kubik: f(x) = x^3")
plt.plot(x, 2*x + 1, label="Affine: f(x) = 2x + 1")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Perbandingan Visualisasi Grafik Fungsi")
plt.legend()
plt.grid()
plt.show()