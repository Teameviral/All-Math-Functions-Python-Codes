from sympy import *

x = Symbol('x')

f = x**2

integral = integrate(f, x)

print(integral)
