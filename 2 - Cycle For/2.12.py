N = int(input("N: "))
product = 1.0

for i in range(1, N+1):
    product *= i

print("Произведение чисел от 1 до", N, "равно", product)
