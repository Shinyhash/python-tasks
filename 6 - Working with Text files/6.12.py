with open('6.12.f.txt', 'r') as file:
    a = file.read()

b = a.replace('p', 'w')

with open('6.12.f.txt', 'w') as file:
    file.write(b)
