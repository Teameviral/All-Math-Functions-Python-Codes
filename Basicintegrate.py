from sympy import *

# Create a symbolic variable x

x = Symbol('x')

# Define the functions

f1 = x**2

f2 = exp(x)

f3 = sin(x)

f4 = cos(x)

# Compute the definite integrals of the functions

a, b = 1, 2 # limits of integration

integral1 = integrate(f1, (x, a, b))

integral2 = integrate(f2, (x, a, b))

integral3 = integrate(f3, (x, a, b))

integral4 = integrate(f4, (x, a, b))

# Print the results

print("The definite integral of x^2 from 1 to 2 is: ", integral1)

print("The definite integral of e^x from 1 to 2 is: ", integral2)

print("The definite integral of sin(x) from 1 to 2 is: ", integral3)

print("The definite integral of cos(x) from 1 to 2 is: ", integral4)

