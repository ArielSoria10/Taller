import matplotlib.pyplot as plt
import numpy as np


def taylor_ln(x, n):
  suma = 0
  for k in range(1, n + 1):
    suma = suma + ((-1) ** (k + 1) / k) * (x - 1) ** k
  return suma


print(f"P_3(1.5)  = {taylor_ln(1.5, 3):.6f}")
print(f"P_10(1.5) = {taylor_ln(1.5, 10):.6f}")
print(f"P_10(2.5) = {taylor_ln(2.5, 10):.6f}")

x = np.linspace(0.1, 3, 400)

plt.figure(figsize=(8, 5))
plt.plot(x, np.log(x), label=r"$\ln(x)$", color="black", linewidth=2)
plt.plot(x, taylor_ln(x, 1), linestyle="--", label=r"$P_1(x)$")
plt.plot(x, taylor_ln(x, 2), linestyle="--", label=r"$P_2(x)$")
plt.plot(x, taylor_ln(x, 3), linestyle="--", label=r"$P_3(x)$")
plt.plot(x, taylor_ln(x, 6), linestyle="--", label=r"$P_6(x)$")

plt.scatter([1], [0], color="red", zorder=5, label="Centro (1, 0)")
plt.ylim(-3, 2)
plt.xlabel("x")
plt.ylabel("y")
plt.title(r"Polinomios de Taylor de $\ln(x)$ alrededor de $x_0 = 1$")
plt.legend()
plt.grid(True)
plt.show()

grados = np.arange(1, 31)
error_15 = np.abs(np.log(1.5) - np.vectorize(taylor_ln)(1.5, grados))
error_25 = np.abs(np.log(2.5) - np.vectorize(taylor_ln)(2.5, grados))
cota_15 = (0.5 ** (grados + 1)) / (grados + 1)

plt.figure(figsize=(8, 5))
plt.semilogy(grados, error_15, "o-", label=r"Error en $x = 1.5$")
plt.semilogy(grados, error_25, "s-", label=r"Error en $x = 2.5$")
plt.semilogy(
    grados, cota_15, "--", color="green", label=r"Cota en $x = 1.5$: $0.5^{n+1}/(n+1)$"
)

plt.xlabel("Grado n")
plt.ylabel("Error absoluto (escala logarítmica)")
plt.title(r"Error de aproximación $|\ln(x) - P_n(x)|$")
plt.legend()
plt.grid(True, which="both")
plt.show()