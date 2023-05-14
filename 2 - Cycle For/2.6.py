import math

def f(x):
    return math.sin(x)

a = 0
b = math.pi
n = 10
dx = (b - a) / n

area = 0
for i in range(n):
    x = a + (i + 1) * dx
    h = f(x)
    area += dx * h

print(area)
