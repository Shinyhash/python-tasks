import math

PI = 3.14159265358979323846

def ballV(d):
    return (4.0 * PI / 3.0) * d ** 3

sum = 0.0
for i in range(12):
    sum += ballV(10.0 + i * 0.5)

print("Sum =", sum)
