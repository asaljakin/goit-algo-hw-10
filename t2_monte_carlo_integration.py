import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Введення даних від користувача
print("Введіть межі інтегрування:")
a = float(input("Нижня межа (a): "))
b = float(input("Верхня межа (b): "))

# Визначення функції
def f(x):
    return x ** 2

# Метод Монте-Карло
def monte_carlo_integration(f, a, b, num_samples=100000):
    x_random = np.random.uniform(a, b, num_samples)
    y_random = f(x_random)
    integral = (b - a) * np.mean(y_random)
    return integral

# Обчислення інтеграла методом Монте-Карло
mc_result = monte_carlo_integration(f, a, b)
print(f"\nІнтеграл (Монте-Карло): {mc_result}")

# Перевірка за допомогою SciPy
sp_result, error = spi.quad(f, a, b)
print(f"Інтеграл (SciPy quad): {sp_result}")

# Візуалізація
x = np.linspace(a - 0.5, b + 0.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
plt.grid()
plt.show()