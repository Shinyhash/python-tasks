a = int(input("a: "))
b = int(input("b: "))

result = 1
for i in range(a, b+1):
    result *= i

print(a, "до", b, "равно", result)