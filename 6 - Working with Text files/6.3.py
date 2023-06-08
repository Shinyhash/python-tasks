with open('6.3.f.txt', 'r') as file:
    n = [float(num) for num in file.readlines()]

m = min(n)

print("Наименьшее число:", m)
