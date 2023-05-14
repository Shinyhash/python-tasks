def f(x):
    return x**2

def g(x):
    return 5 + x/2

a = 0
b = 5
n = 10

dx = (b - a) / n

x = [a + i*dx for i in range(n+1)]
h = [f(xi) - g(xi) for xi in x]
A = [dx * hi for hi in h]
S = sum(A)

print("Приближенная площадь фигуры:", S)
