with open('6.8.f.txt', 'r') as file:
    a = file.read()

c = a.count('p')

print("Количество букв 'p' в файле:", c)
