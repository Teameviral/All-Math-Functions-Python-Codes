from sympy import laplace_transform, symbols, exp, sin, cos, Heaviside

def laplace_transform_func(f, t, s):

    t, s = symbols('t s')

    return laplace_transform(f, t, s)

#Examples

t, s = symbols('t s')

#example 1

f = exp(-t)

print(laplace_transform_func(f, t, s))

#example 2

f = sin(t)

print(laplace_transform_func(f, t, s))

#example 3

f = cos(t)

print(laplace_transform_func(f, t, s))

#example 4

f = Heaviside(t)

print(laplace_transform_func(f, t, s))
