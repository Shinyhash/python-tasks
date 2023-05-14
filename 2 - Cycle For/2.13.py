n = int(input("Введите целое число N: "))

if n % 2 == 0:
    product = 1.0
    for i in range(2, n+1, 2):
        product *= i
else:
    product = 1.0
    for i in range(1, n+1, 2):
        product *= i

print(product)
