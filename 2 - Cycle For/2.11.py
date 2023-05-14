A = float(input("A (> 1): "))
N = 1
sum = 0

while sum < A:
    sum += 1/N
    N += 1

print("Наибольшее целое число N: ", N-1)
print("Сумма 1 + 1/2 + ... + 1/N: ", sum)
