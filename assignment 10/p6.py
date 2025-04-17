import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 6*x**2 + 11*x - 6  # Example polynomial

def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    updates = []
    for _ in range(max_iter):
        c = (a + b) / 2
        updates.append((a, b, c))
        if abs(func(c)) < tol or (b - a) / 2 < tol:
            break
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
    return np.array(updates)

a, b = np.random.uniform(-10, 0), np.random.uniform(0, 10)
while f(a) * f(b) > 0:
    a, b = np.random.uniform(-10, 0), np.random.uniform(0, 10)

updates = bisection_method(f, a, b)
x_vals = updates[:, 2]

x = np.linspace(-1, 5, 500)
plt.plot(x, f(x), label="f(x)")
plt.axhline(0, color='black', linewidth=0.5)
for i, c in enumerate(x_vals):
    plt.scatter(c, f(c), color='red', s=10)
plt.title("Bisection Method - Root Finding Process")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()