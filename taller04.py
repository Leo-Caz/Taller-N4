import numpy as np
import matplotlib.pyplot as plt


def taylor_ln(x, n):
    """Polinomio de Taylor de grado n de ln(x) alrededor de x0 = 1."""
    suma = 0
    for k in range(1, n + 1):
        suma = suma + ((-1) ** (k + 1)) * (x - 1) ** k / k
    return suma


# Comprobaciones numéricas
print(f"P3(1.5) = {taylor_ln(1.5, 3):.6f}")
print(f"P10(1.5) = {taylor_ln(1.5, 10):.6f}")
print(f"P10(2.5) = {taylor_ln(2.5, 10):.6f}")
for grado in range(1, 31):
    error = abs(np.log(1.5) - taylor_ln(1.5, grado))
    if error < 1e-6:
        print(f"Menor grado con error < 1e-6 en 1.5: {grado}")
        break

# Gráfica 1: función logaritmo y aproximaciones de Taylor
valores_x = np.linspace(0.1, 3, 400)
plt.figure(figsize=(9, 6))
plt.plot(valores_x, np.log(valores_x), label='ln(x)', linewidth=2)
for grado in [1, 2, 3, 6]:
    plt.plot(valores_x, taylor_ln(valores_x, grado), label=f'P{grado}(x)')
plt.scatter([1], [0], label='Centro (1, 0)', zorder=5)
plt.ylim(-3, 2)
plt.xlabel('x')
plt.ylabel('Valor de la función')
plt.title('ln(x) y polinomios de Taylor alrededor de x0 = 1')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('grafica_1_taylor.png', dpi=180)
plt.close()

# Gráfica 2: error para x=1.5 y x=2.5, y cota en x=1.5
grados = np.arange(1, 31)
error_15 = [abs(np.log(1.5) - taylor_ln(1.5, int(n))) for n in grados]
error_25 = [abs(np.log(2.5) - taylor_ln(2.5, int(n))) for n in grados]
cota_15 = [0.5 ** (n + 1) / (n + 1) for n in grados]
plt.figure(figsize=(9, 6))
plt.semilogy(grados, error_15, 'o-', label='Error real en x = 1.5')
plt.semilogy(grados, error_25, 's-', label='Error real en x = 2.5')
plt.semilogy(grados, cota_15, '--', label='Cota del error en x = 1.5')
plt.xlabel('Grado n')
plt.ylabel('Error absoluto (escala logarítmica)')
plt.title('Error de los polinomios de Taylor de ln(x)')
plt.legend()
plt.grid(True, which='both')
plt.tight_layout()
plt.savefig('grafica_2_error.png', dpi=180)
plt.close()
