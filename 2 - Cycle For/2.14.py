import math

N = int(input("Введите количество точек N: "))
A = float(input("Введите начальную точку A: "))
B = float(input("Введите конечную точку B: "))

H = (B - A) / (N - 1)

for i in range(N):
    x = A + i * H
    fx = 1 - math.sin(x)
    print(f"F({x}) = {fx}")
