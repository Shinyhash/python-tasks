import math

with open('6.9.f.txt', 'r') as file:
    n = file.readlines()

n = [float(num.strip()) for num in n]

p = [num for num in n if num > 0]

g = math.prod(p) ** (1 / len(p))

print("Среднее геометрическое положительных чисел:", g)
