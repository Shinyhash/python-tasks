with open('6.5.f.txt', 'r') as file:
    s = file.readlines()

s = [int(b.strip()) for b in s]

c = sum(s)

print("Сумма квадратов чисел:", c)
