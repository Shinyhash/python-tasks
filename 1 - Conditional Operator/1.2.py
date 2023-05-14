a = int(input())
b = int(input())
c = int(input())

if a < b < c:
    a = a ** 2
    b = b ** 2
    c = c ** 2
elif a > b > c:
    a = min(a, b, c)
    b = min(a, b, c)
    c = min(a, b, c)
else:
    a = -a
    b = -b
    c = -c

print("a =", a)
print("b =", b)
print("c =", c)