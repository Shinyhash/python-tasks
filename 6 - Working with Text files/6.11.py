b = 10

with open('6.11.f.txt', 'r') as file:
    n = file.readlines()

n = [float(num.strip()) for num in n]

p = 1

for num in n:
    if num < b:
        p *= num

print("Произведение чисел меньших", b,":", p)
