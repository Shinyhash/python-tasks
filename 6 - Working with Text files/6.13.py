with open('6.13.f.txt', 'r') as file:
    n = file.readlines()

n = [float(num.strip()) for num in n]

m = 15.0

a = 0
while a < len(n) and m > n[a]:
    a += 1

n.insert(a, m)

with open('6.13.f.txt', 'w') as file:
    for number in n:
        file.write(str(number) + '\n')
