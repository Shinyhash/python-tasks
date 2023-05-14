A = float(input("A (> 1): "))
N = 1
sum = 1

while sum <= A:
    N += 1
    sum += 1/N

print("Наименьшее целое число N: ", N)
print("Сумма 1 + 1/2 + ... + 1/N: ", sum)
