import sympy as sp 
import numpy as np
import matplotlib.pyplot as plt

x=sp.Symbol('x')

function = x**2 + 3*x + 1
derivative = sp.diff(function, x)

f = sp.lambdify(x, function, 'numpy') 
f_prime = sp.lambdify(x, derivative, 'numpy')
x_vals=np.linspace(-10, 10 , 400)

y_vals=f(x_vals)
y_prime_vals= f_prime(x_vals)

plt.plot(x_vals , y_vals, label='f(x)', color='blue')
plt.plot(x_vals , y_prime_vals, label='f(x)', color='red')

plt.title('Function and Its Derivative')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.grid(True)
plt.show()