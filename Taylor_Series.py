import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = sp.Symbol('x')
f = sp.sin(x)  

a = float(input("a = "))
n = int(input("terms = "))

T = f.series(x, a, n).removeO()

f1 = sp.lambdify(x, f, 'numpy')
T1 = sp.lambdify(x, T, 'numpy')

X = np.linspace(a - 10, a + 10, 400)
plt.plot(X, f1(X), label="f(x)")
plt.plot(X, T1(X), '--', label="Taylor")
plt.axvline(a, color='gray', ls=':')
plt.legend()
plt.grid()
plt.show()
