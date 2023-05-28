import math

num, val = input().split()
num = int(num)
val = float(val)

if num == 1:
    a = val
    R1 = a / 2
    R2 = a * math.sqrt(3) / 3
    S = a ** 2 * math.sqrt(3) / 4
elif num == 2:
    R1 = val
    a = R1 * 2 * math.sqrt(3)
    R2 = a * math.sqrt(3) / 3
    S = a ** 2 * math.sqrt(3) / 4
elif num == 3:
    h = val
    a = h * 2 / math.sqrt(3)
    R1 = a / 2
    R2 = a * math.sqrt(3) / 3
    S = a ** 2 * math.sqrt(3) / 4
else:
    S = val
    a = math.sqrt(4 * S / math.sqrt(3))
    R1 = a / 2
    R2 = a * math.sqrt(3) / 3

print("{:.3f}".format(a))
print("{:.3f}".format(R1))
print("{:.3f}".format(R2))
print("{:.3f}".format(S))
