import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import sympy as sp

x = sp.Symbol('x')
f = x**3 - 6*x**2 + 9*x + 2
f_num = sp.lambdify(x, f, modules=['numpy'])

a = float(input("Enter starting x-value (a): "))
b = float(input("Enter ending x-value (b): "))

area, _ = quad(f_num, a, b)
print(f"Area between x = {a} and x = {b} is {area:.4f}")

x_vals = np.linspace(a - 2, b + 2, 400)
y_vals = f_num(x_vals)

plt.plot(x_vals, y_vals, label="f(x)", color='blue')  

x_shade = np.linspace(a, b, 200)
y_shade = f_num(x_shade)
plt.fill_between(x_shade, y_shade, color='lightblue', label="Area")

f_prime = sp.diff(f, x)
critical_points = sp.solve(f_prime)

f_double_prime = sp.diff(f_prime, x)
inflection_points = sp.solve(f_double_prime)

for pt in critical_points:
    if pt.is_real:
        y_val = f_num(float(pt))
        plt.plot(pt, y_val, 'ro')
        plt.text(pt, y_val, f"  Max/Min\n({pt:.1f}, {y_val:.1f})", color='red')

for pt in inflection_points:
    if pt.is_real:
        y_val = f_num(float(pt))
        plt.plot(pt, y_val, 'go')  
        plt.text(pt, y_val, f"  Inflection\n({pt:.1f}, {y_val:.1f})", color='green')

plt.title("Area Under Curve + Critical Points")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()